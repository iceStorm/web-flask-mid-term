
class NavItem:
    href: str
    title: str
    is_active: bool

    def __init__(self, href: str, title: str, is_active: bool):
        self.href = href
        self.title = title
        self.is_active = is_active


class NavBarViewModel:
    user: any
    nav_items = []  # type: List[NavItem]

    def __init__(self, user: any, nav_items: [NavItem]):
        self.user = user
        self.nav_items = nav_items

    def set_active_nav_item(self, path: str):
        for item in self.nav_items:
            if item.href == path:
                item.is_active = True

