from model.burger import Burger
from model.drink import Drink
from model.menu import Menu
from view.menu_view import MenuView


class MenuController:
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView()
        self._add_initial_items()

    def add_menu_item(self) -> None:
        item_type = self._view.get_menu_item_type()

        if not item_type:
            return

        common_data = self._view.get_common_item_data()

        try:
            if item_type == "1":  # Burger
                burger_data = self._view.get_burger_specific_data()
                new_item = Burger(
                    name=common_data["name"],
                    price=common_data["price"],
                    description=common_data["description"],
                    patty_type=burger_data["patty_type"],
                )
            elif item_type == "2":  # Drink
                drink_data = self._view.get_drink_specific_data()
                new_item = Drink(
                    name=common_data["name"],
                    price=common_data["price"],
                    description=common_data["description"],
                    volume_ml=drink_data["volume_ml"],
                )
            else:
                self._view.display_error_message("Invalid item type selected.")
                return

            self._menu.add_item(new_item)
            self._view.display_success_message("Menu item added successfully!")
        except Exception as e:
            self._view.display_error_message(f"Failed to add item: {e}")

    def list_menu_items(self) -> None:
        items = self._menu.items
        self._view.display_menu_items(items)

    def _add_initial_items(self):
        if not self._menu.get_item_by_name("X-Polenta"):
            b1 = Burger(
                "X-Polenta",
                25.50,
                "Pão, bife de polenta, queijo, alface e tomate",
                "Polenta",
            )
            self._menu.add_item(b1)
        if not self._menu.get_item_by_name("Polenta-Cola"):
            d1 = Drink("Polenta-Cola", 8.00, "Refrigerante sabor polenta", 350)
            self._menu.add_item(d1)
