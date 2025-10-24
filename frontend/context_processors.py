# frontend/context_processors.py
from django.db.models import Q, Prefetch
from frontend.models import Menu, SubMenu, ChildMenu

def frontend_menu(request):
    """
    Department-based menu context processor.
    Detects active menu/submenu/child based on current path.
    """
    path = request.path
    user = request.user
    user_dept = getattr(user, "department", None)

    if user.is_authenticated:
        menu_filter = Q(visibility='public') | Q(visibility='authenticated')
        if user_dept:
            menu_filter |= Q(visibility='department', departments=user_dept)
    else:
        menu_filter = Q(visibility='public')

    child_qs = ChildMenu.objects.filter(menu_filter).order_by("order")
    submenu_qs = SubMenu.objects.filter(menu_filter).prefetch_related(
        Prefetch("child_menus", queryset=child_qs, to_attr="child_list")
    ).order_by("order")
    menus = Menu.objects.filter(menu_filter).prefetch_related(
        Prefetch("submenus", queryset=submenu_qs, to_attr="submenu_list")
    ).order_by("order")

    # Determine active items
    active_menu_id = active_submenu_id = active_child_id = None
    for menu in menus:
        for submenu in getattr(menu, "submenu_list", []):
            for child in getattr(submenu, "child_list", []):
                if child.url and path.rstrip("/") == child.url.rstrip("/"):
                    active_menu_id = menu.id
                    active_submenu_id = submenu.id
                    active_child_id = child.id
                    break
            else:
                # if no child matched, check submenu match
                if submenu.url and path.rstrip("/") == submenu.url.rstrip("/"):
                    active_menu_id = menu.id
                    active_submenu_id = submenu.id
                    active_child_id = None
                    break
            # Break outer loop if found
            if active_submenu_id:
                break
        if active_menu_id:
            break

    return {
        "global_menus": menus,
        "active_menu_id": active_menu_id,
        "active_submenu_id": active_submenu_id,
        "active_child_id": active_child_id,
    }
