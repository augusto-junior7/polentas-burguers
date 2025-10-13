from model.burger import Burger
from model.drink import Drink
from model.menu import Menu
from view.menu_view import MenuView


class MenuController:
    def __init__(self):
        self.__menu = Menu()
        self.__view = MenuView()
        self._add_initial_items()

    @property
    def menu(self) -> Menu:
        return self.__menu

    def run_menu_menu(self):
        while True:
            option = self.__view.display_menu_menu()
            if option == "1":
                self.add_menu_item()
            elif option == "2":
                self.list_menu_items()
            elif option == "3":
                self.remove_menu_item()
            elif option == "0":
                break
            else:
                self.__view.display_error_message("Opção inválida.")

    def add_menu_item(self) -> None:
        item_type = self.__view.get_menu_item_type()

        if not item_type:
            return

        common_data = self.__view.get_common_item_data()

        try:
            if item_type == "1":  # Burger
                burger_data = self.__view.get_burger_specific_data()
                new_item = Burger(
                    name=common_data["name"],
                    price=common_data["price"],
                    description=common_data["description"],
                    patty_type=burger_data["patty_type"],
                )
            elif item_type == "2":  # Drink
                drink_data = self.__view.get_drink_specific_data()
                new_item = Drink(
                    name=common_data["name"],
                    price=common_data["price"],
                    description=common_data["description"],
                    volume_ml=drink_data["volume_ml"],
                )
            else:
                self.__view.display_error_message("Tipo de item inválido.")
                return

            self.__menu.add_item(new_item)
            self.__view.display_success_message(
                "Item do menu adicionado com sucesso!"
            )
        except Exception as e:
            self.__view.display_error_message(f"Falha ao adicionar item: {e}")

    def list_menu_items(self) -> None:
        items = self.__menu.items
        self.__view.display_menu_items(items)

    def remove_menu_item(self) -> None:
        item_name = self.__view.get_item_name()

        if self.__menu.remove_item(item_name):
            self.__view.display_success_message(
                f"Item '{item_name}' removido do cardápio com sucesso!"
            )
        else:
            self.__view.display_error_message(
                "Item não encontrado no cardápio."
            )

    def _add_initial_items(self):
        initial_burgers = [
            Burger(
                "X-Polenta",
                25.50,
                "Pão, bife de polenta, queijo, alface e tomate",
                "Polenta",
            ),
            Burger(
                "X-Frango",
                27.50,
                "Pão, bife de frango, queijo, alface e tomate",
                "Frango",
            ),
            Burger(
                "X-Peixe",
                29.50,
                "Pão, filé de peixe, queijo, alface e tomate",
                "Peixe",
            ),
        ]

        for b in initial_burgers:
            self.__menu.add_item(b)

        initial_drinks = [
            Drink("Polenta-Cola", 8.00, "Refrigerante sabor polenta", 350),
            Drink("Suco de Laranja", 6.00, "Suco natural de laranja", 450),
            Drink("Água Mineral", 4.00, "Água mineral sem gás", 500),
        ]

        for d in initial_drinks:
            self.__menu.add_item(d)
