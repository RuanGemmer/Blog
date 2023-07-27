from django.contrib import admin
from django.http.request import HttpRequest
from site_setup.models import MenuLink, SiteSetup
from django import forms


# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'id', 'text', 'url_or_path',
#     list_display_links = 'id', 'text', 'url_or_path',
#     search_files = 'id', 'text', 'url_or_path',


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'
        widgets = {
            'favicon': forms.FileInput(attrs={'accept': 'image/png'}),
        }


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = (MenuLinkInLine,)
    form = SiteSetupForm

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
