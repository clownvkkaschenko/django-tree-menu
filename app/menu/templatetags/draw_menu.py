from django import template

from ..models import MenuItem

register = template.Library()


def serializer(menuItems):
    result = []
    for item in menuItems:
        result.append({
            'id': item.id,
            'title': item.item_name,
            'parent': item.parent_item,
            'menu_url': item.item_url,
            'first_level': False,
            'lower_level_children': [],
            'open': False,
            'active': False,
            'active_child': None
        })
    return result


def recursive_open_parents(current_item, list_of_item):
    parent = current_item['parent']
    for item in list_of_item:
        if parent and item['id'] == parent.id:
            item['open'] = True
            item['active_child'] = current_item
            if item['parent']:
                return recursive_open_parents(item, list_of_item)


def activeItems(item, list_of_item):
    for nested_item in list_of_item:
        if (
            nested_item['parent']
            and nested_item['parent'].id == item['id']
        ):
            item['lower_level_children'].append(nested_item)
            nested_item['open'] = True
        if item['parent']:
            recursive_open_parents(item, list_of_item)


@register.inclusion_tag('template_tags/menu.html', takes_context=True)
def draw_menu(context, menu_title):
    menu = MenuItem.objects.filter(main_menu__menu_name=menu_title)
    menuItems = serializer(menu)
    tree_menu = list()
    for item in menuItems:
        if not item['parent']:
            item['first_level'] = True
        item['active'] = item['menu_url'] == context.request.path[1:-1]
        if item['active']:
            activeItems(item, menuItems)
    for item in menuItems:
        if item['first_level']:
            tree_menu.append(item)
            while item['active_child']:
                tree_menu.append(item['active_child'])
                item = item['active_child']
            for i in item['lower_level_children']:
                tree_menu.append(i)
    return {'tree_menu': tree_menu}
