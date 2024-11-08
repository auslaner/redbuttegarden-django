from wagtail.users.views.users import UserViewSet as WagtailUserViewSet

from .forms import CustomUserCreationForm, CustomUserEditForm


class UserViewSet(WagtailUserViewSet):
    create_template_name = "custom_user/users/create.html"
    edit_template_name = "custom_user/users/edit.html"

    # This replaces the WAGTAIL_USER_EDIT_FORM and WAGTAIL_USER_CREATION_FORM settings
    def get_form_class(self, for_update=False):
        if for_update:
            return CustomUserEditForm
        return CustomUserCreationForm