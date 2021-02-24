from django import forms
from django.core.paginator import Paginator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from home.abstract_models import AbstractBase
from home.models import AlignedParagraphBlock, ButtonBlock, EmphaticText, GeneralPage, ImageLinkList, Heading, \
    MultiColumnAlignedParagraphBlock


@register_snippet
class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)
    parent = models.ForeignKey(
        'self',
        blank=True, null=True,
        related_name="children",
        help_text=_("Unlike tags, categories can have a hierarchy so they can be more specifically organized."),
        on_delete=models.CASCADE
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('parent'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Event Category")
        verbose_name_plural = _("Event Categories")


@register_snippet
class PolicyLink(models.Model):
    """
    Model for maintaining links to policy pages that can be used on many pages
    """
    name = models.CharField(max_length=100, help_text=_("Create a name for this policy"))
    link_text = models.CharField(max_length=500, help_text=_("This text will link to the provided policy page"))
    policy_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('link_text'),
        PageChooserPanel('policy_page'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Policy Link"


class SingleListImage(blocks.StructBlock):
    image = ImageChooserBlock(
        label='Image',
    )
    title = blocks.CharBlock(
        label='Title',
        max_length=200,
        help_text=_("Displayed right of image in h2 tag, centered and uppercase")
    )
    sub_title = blocks.CharBlock(
        label='Subtitle',
        max_length=200,
        help_text=_("Displayed under title, centered and green")
    )
    text = blocks.RichTextBlock(
        label='Text',
        required=False,
        help_text=_("Optional text to be displayed alongside image")
    )
    link_url = blocks.URLBlock(
        label='Link URL',
        max_length=200,
        required=False,
        help_text=_("If provided, the link will be applied to the image")
    )


class ListWithImagesBlock(blocks.StructBlock):
    list_items = blocks.ListBlock(
        SingleListImage(),
        label="List Item",
        help_text=_("Images displayed with text to the right, all with a tan background")
    )

    class Meta:
        template = 'events/list_with_images.html'
        icon = 'fa-id-card-o'


class ImageRow(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock())

    class Meta:
        template = 'blocks/image_row.html'


BLOCK_TYPES = [
    ('button', ButtonBlock()),
    ('green_heading', Heading(classname='full title',
                              help_text=_('Text will be green and centered'))),
    ('emphatic_text', EmphaticText(required=False, help_text="Red italic text")),
    ('paragraph', AlignedParagraphBlock(required=True, classname='paragraph')),
    ('multi_column_paragraph', MultiColumnAlignedParagraphBlock()),
    ('image', ImageChooserBlock()),
    ('image_link_list', ImageLinkList()),
    ('html', blocks.RawHTMLBlock(required=False)),
    ('image_list', ListWithImagesBlock(required=False)),
    ('image_row', ImageRow()),
]


class EventIndexPage(RoutablePageMixin, AbstractBase):
    intro = RichTextField(blank=True)
    body = StreamField(BLOCK_TYPES + [('page_link', PageChooserBlock())], blank=True)

    content_panels = AbstractBase.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body', classname="full"),
    ]

    subpage_types = ['events.EventPage', 'events.EventGeneralPage', 'events.EventIndexPage']

    search_fields = AbstractBase.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    def get_event_items(self):
        # This returns a Django paginator of event items in this section
        return Paginator(self.get_children().live(), 10)

    def get_cached_paths(self):
        # Yield the main URL
        yield '/'

        # Yield one URL per page in the paginator to make sure all pages are purged
        for page_number in range(1, self.get_event_items().num_pages + 1):
            yield '/?page=' + str(page_number)

    @route(r'^$')
    def event_list(self, request, *args, **kwargs):
        self.events = self.get_children().live().order_by('-latest_revision_created_at')
        return AbstractBase.serve(self, request, *args, **kwargs)

    @route(r'^e-cat/(?P<event_category>[-\w]+)/$')
    def event_by_category(self, request, event_category, *args, **kwargs):
        self.search_type = 'event-category'
        self.search_term = event_category
        self.cat_title = event_category.replace('-', ' ').title()
        # We need to figure out which banner image to display based on the category
        banner_search = Image.objects.search(self.cat_title + ' banner')
        if banner_search:
            self.banner = banner_search[0]
        # We want to grab all events of the given category for each Page type that has event categories
        # We also want to exclude copies so we check the page has no alias
        events = []
        event_pages = EventPage.objects.live().filter(event_categories__slug=event_category, alias_of__isnull=True)
        for event in event_pages:
            events.append(event)
        event_general_pages = EventGeneralPage.objects.live().filter(event_categories__slug=event_category,
                                                                     alias_of__isnull=True)
        for event in event_general_pages:
            events.append(event)
        self.events = events
        return AbstractBase.serve(self, request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by order_date
        context = super().get_context(request, *args, **kwargs)
        context['events'] = self.events
        return context


class EventPage(AbstractBase):
    # TODO - Delete image once all existing pages have a thumbnail set
    #   TODO - When that's done, you can also delete the save override which tries to set thumbnail to image
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    location = models.CharField(max_length=100)
    additional_info = RichTextField(blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    member_cost = models.CharField(max_length=100, blank=True, null=True,
                                   help_text="Accepts numbers or text. e.g. Free!")
    public_cost = models.CharField(max_length=200, blank=True, null=True,
                                   help_text="Accepts numbers or text. e.g. $35")
    sub_heading = models.CharField(max_length=200, blank=True, help_text="e.g. 500,000 Blooming Bulbs")
    event_dates = models.CharField(max_length=200)
    event_categories = ParentalManyToManyField(EventCategory, blank=True)
    notes = RichTextField(blank=True,
                          help_text="Notes will appear on the thumbnail image of the event on the event index page")
    body = StreamField(BLOCK_TYPES)
    policy = models.ForeignKey(
        'events.PolicyLink',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = AbstractBase.content_panels + [
        FieldPanel('location'),
        FieldPanel('additional_info'),
        FieldPanel('instructor'),
        FieldPanel('member_cost'),
        FieldPanel('public_cost'),
        FieldPanel('sub_heading'),
        FieldPanel('event_dates'),
        FieldPanel('event_categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('notes'),
        StreamFieldPanel('body'),
        SnippetChooserPanel('policy', help_text=_("Optionally choose a policy link to include on the page"))
    ]

    parent_page_types = ['events.EventIndexPage', 'home.GeneralIndexPage']

    search_fields = AbstractBase.search_fields + [
        index.SearchField('instructor'),
        index.SearchField('sub_heading'),
        index.SearchField('event_dates'),
        index.SearchField('notes'),
        index.SearchField('body'),
    ]

    def save(self, clean=True, user=None, log_action=False, **kwargs):
        if self.thumbnail is None:
            self.thumbnail = self.image

        super().save(**kwargs)


class EventGeneralPage(GeneralPage):
    event_dates = models.CharField(max_length=200)
    notes = RichTextField(blank=True,
                          help_text="Notes will appear on the thumbnail image of the event on the event index page")
    image = GeneralPage.thumbnail  # just to match EventPage so the EventIndexPage template doesn't need to be changed
    event_categories = ParentalManyToManyField(EventCategory, blank=True)

    content_panels = GeneralPage.content_panels + [
        FieldPanel('event_dates'),
        FieldPanel('event_categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('notes'),
    ]

    parent_page_types = ['events.EventIndexPage', 'home.GeneralIndexPage']

    search_fields = GeneralPage.search_fields + [
        index.SearchField('event_dates'),
        index.SearchField('notes')
    ]
