from django.contrib.admin import ModelAdmin, register

from .models import Menu, MenuItem

ModelAdmin.empty_value_display = '-пусто-'


@register(Menu)
class MenuAdmin(ModelAdmin):
    list_display = ('menu_name',)
    search_fields = ('menu_name',)


@register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = ('item_name',)
    list_filter = ('main_menu', 'parent_item')
    search_fields = ('main_menu', 'parent_item')
    prepopulated_fields = {'item_url': ('item_name',)}
