import datetime

from django.db import models
from django.db.models import BooleanField
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel, \
    FieldRowPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from home.abstract_models import AbstractBase
from home.models import Heading, EmphaticText, AlignedParagraphBlock

donor_table_options = {
    'minSpareRows': 0,
    'startRows': 3,
    'startCols': 6,
    'colHeaders': True,
    'rowHeaders': True,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 216,
    'language': 'en-US',
    'renderer': 'text',
    'autoColumnSize': False,
}

info_card_table_options = {
    'minSpareRows': 0,
    'startRows': 2,
    'startCols': 4,
    'colHeaders': True,
    'rowHeaders': True,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 216,
    'language': 'en-US',
    'renderer': 'text',
    'autoColumnSize': False,
}


class Sponsors(blocks.StructBlock):
    sponsor_title = blocks.CharBlock(
        label='Sponsor Title',
        max_length=200,
    )
    sponsor_url = blocks.URLBlock(
        label="URL to sponsor website"
    )
    sponsor_logo = ImageChooserBlock()


class SponsorList(blocks.StructBlock):
    list_items = blocks.ListBlock(
        Sponsors(),
        label="Sponsors"
    )

    class Meta:
        template = 'blocks/sponsor_list.html'


class ButtonTable(blocks.StructBlock):
    button_text = blocks.CharBlock(
        label="Button text"
    )
    table_list = blocks.StreamBlock([
        ('title', Heading()),
        ('table', TableBlock(table_options=donor_table_options,
                             help_text=_("Right-click to add/remove rows/columns"))),
    ])

    class Meta:
        template = 'blocks/button_table.html'


class TableInfoCard(blocks.StructBlock):
    body = blocks.StreamBlock([
        ('heading', Heading()),
        ('paragraph', AlignedParagraphBlock()),
        ('table', TableBlock(table_options=info_card_table_options))
    ])


class TableInfoCardList(blocks.StructBlock):
    list_items = blocks.ListBlock(
        TableInfoCard(),
        label="List of info cards with tables"
    )

    class Meta:
        template = 'blocks/table_info_card_list.html'


class ConcertPage(AbstractBase):
    banner_link = models.URLField(help_text=_("Where to direct the banner image link"),
                                  blank=True)
    intro = RichTextField(blank=True)
    donor_banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    button_one = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    button_two = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    button_three = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    button_four = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = AbstractBase.content_panels + [
        FieldPanel('banner_link'),
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('donor_banner'),
        PageChooserPanel('button_one'),
        PageChooserPanel('button_two'),
        PageChooserPanel('button_three'),
        PageChooserPanel('button_four'),
        InlinePanel('concerts', label='Concerts')
    ]


class Concert(Orderable):
    page = ParentalKey(ConcertPage, on_delete=models.CASCADE, related_name='concerts')
    band_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    virtual = BooleanField(default=False, help_text=_('Is this a virtual concert?'))
    canceled = BooleanField(default=False)
    postponed = BooleanField(default=False)
    sold_out = BooleanField(default=False)
    # Virtual concert will remain available on demand until this date
    available_until = models.DateField(blank=True, null=True,
                                       help_text=_('Date that on-demand virtual concert will remain available until'))
    # Band/opener names and url properties replaced with single RichTextField to account for wide variety in how the
    # bands info may be displayed
    band_info = RichTextField(help_text=_('Provide the names of the bands/openers and any other info here. Text will be'
                                          ' centered.'))

    concert_date = models.DateField(blank=True)
    gates_time = models.TimeField(default=datetime.time(hour=18), blank=True, null=True)
    show_time = models.TimeField(default=datetime.time(hour=19))
    member_price = models.CharField(default='$', max_length=100, blank=True, null=True)
    public_price = models.CharField(default='$', max_length=100)

    # Added a ticket URL for concerts that are sold from a non-standard URL
    ticket_url = models.URLField(default='https://redbuttegarden.ticketfly.com')

    panels = [
        ImageChooserPanel('band_img'),
        FieldRowPanel([
            FieldPanel('canceled'),
            FieldPanel('postponed'),
            FieldPanel('sold_out'),
        ]),
        FieldPanel('virtual'),
        FieldPanel('available_until'),
        FieldPanel('band_info'),

        FieldPanel('concert_date'),
        FieldPanel('gates_time'),
        FieldPanel('show_time'),
        FieldPanel('member_price'),
        FieldPanel('public_price'),
        FieldPanel('ticket_url'),
    ]

    @property
    def live_in_the_past(self):
        """
        Boolean indicating if the concert's live performance has already occurred.
        """
        return datetime.date.today() > self.concert_date

    @property
    def on_demand_expired(self):
        """
        Boolean indicating if the on-demand performance is still available.
        """
        if self.available_until:
            return datetime.date.today() > self.available_until


class DonorPackagePage(AbstractBase):
    body = StreamField(block_types=[
        ('heading', Heading(classname='full title',
                            help_text=_('Text will be green and centered'))),
        ('emphatic_text', EmphaticText(classname='full title',
                                       help_text=_('Text will be red, italic and centered'))),
        ('paragraph', AlignedParagraphBlock(required=True, classname='paragraph')),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('sponsor_list', SponsorList()),
        ('button_table', ButtonTable()),
        ('table_cards', TableInfoCardList()),
    ], blank=False)

    content_panels = AbstractBase.content_panels + [
        StreamFieldPanel('body'),
    ]
