from typing import List, Dict, Any
from model.menu_item import MenuItem
from model.burger import Burger
from model.drink import Drink


class MenuView:
    def display_menu_management_menu(self) -> str:
        print("\n--- Gestão de Cardápios ---")
        print("1: Adicionar Novo Item")
        print("2: Listar Todos os Itens")
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def get_menu_item_type(self) -> str | None:
        print("Selecione o tipo de item a ser adicionado:")
        print("1: Lanche")
        print("2: Bebida")
        print("0: Cancelar")
        choice = input("Opção: ")
        if choice in ["1", "2"]:
            return choice
        return None

    def get_common_item_data(self) -> Dict[str, Any]:
        name = input("Nome: ")
        price = float(input("Preço: "))
        description = input("Descrição: ")
        return {"name": name, "price": price, "description": description}

    def get_burger_specific_data(self) -> Dict[str, Any]:
        patty_type = input("Tipo de Carne (ex: Carne, Frango, Polenta): ")
        return {"patty_type": patty_type}

    def get_drink_specific_data(self) -> Dict[str, Any]:
        volume_ml = int(input("Volume (ml): "))
        return {"volume_ml": volume_ml}

    def display_menu_items(self, items: List[MenuItem]) -> None:
        print("\n--- Menu Completo ---")
        if not items:
            print("O cardápio está vazio.")
        for item in items:
            base_info = (
                f"- {item.name} (R$ {item.price:.2f}): {item.description}"
            )
            if isinstance(item, Burger):
                print(f"{base_info} [Tipo: {item.patty_type}]")
            elif isinstance(item, Drink):
                print(f"{base_info} [{item.volume_ml}ml]")
            else:
                print(base_info)
        print("-----------------")

    def display_success_message(self, message: str) -> None:
        print(f"\n✅ SUCESSO: {message}\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")
