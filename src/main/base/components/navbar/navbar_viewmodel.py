
class NavItem:
    href: str
    title: str
    is_active: bool

    def __init__(self, href: str, title: str, is_active: bool):
        self.href = href
        self.title = title
        self.is_active = is_active


class NavBarViewModel:
    is_user_logged_in = False
    nav_items: [NavItem]

    def __init__(self, is_user_logged_in: bool, nav_items: [NavItem]):
        self.is_user_logged_in = is_user_logged_in
        self.nav_items = nav_items
