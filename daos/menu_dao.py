from daos.dao import DAO
from models.menu import Menu


class MenuDAO(DAO):
    def __init__(self):
        super().__init__(datasource="menu.pkl")

    def save(self, menu: Menu):
        if menu is not None and isinstance(menu, Menu):
            super().add("menu", menu)

    def load(self) -> Menu | None:
        try:
            menu = super().get("menu")
            if menu is not None and isinstance(menu, Menu):
                return menu
            return None
        except Exception:
            return None
