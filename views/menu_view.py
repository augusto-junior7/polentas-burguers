from typing import Any, Dict, List

import FreeSimpleGUI as sg

from models.burger import Burger
from models.drink import Drink
from models.menu_item import MenuItem
from views.abstract_view import AbstractView


class MenuView(AbstractView):
    def display_menu_menu(self) -> str:
        layout = [
            [sg.Text("Gestão de Cardápios", font=("Arial", 20))],
            [sg.Button("Adicionar Novo Item", key="1", size=(30, 2))],
            [sg.Button("Listar Todos os Itens", key="2", size=(30, 2))],
            [sg.Button("Remover Item do Cardápio", key="3", size=(30, 2))],
            [sg.Button("Voltar ao Menu Principal", key="0", size=(30, 2))],
        ]
        window = sg.Window("Menu Cardápio", layout, element_justification="c")
        event, values = window.read()
        window.close()
        if event is None:
            return "0"
        return event

    def get_menu_item_type(self) -> str | None:
        layout = [
            [sg.Text("Selecione o tipo de item:", font=("Arial", 15))],
            [sg.Button("Lanche", key="1", size=(20, 2))],
            [sg.Button("Bebida", key="2", size=(20, 2))],
            [sg.Button("Cancelar", key="0", size=(20, 2))],
        ]
        window = sg.Window("Tipo de Item", layout, element_justification="c")
        event, values = window.read()
        window.close()
        if event in ["1", "2"]:
            return event
        return None

    def get_common_item_data(self) -> Dict[str, Any]:
        layout = [
            [sg.Text("Dados do Item", font=("Arial", 15))],
            [sg.Text("Nome:"), sg.InputText(key="name")],
            [sg.Text("Preço:"), sg.InputText(key="price")],
            [sg.Text("Descrição:"), sg.InputText(key="description")],
            [sg.Button("Continuar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Dados do Item", layout)
        event, values = window.read()
        window.close()
        if event == "Continuar":
            try:
                price = float(values["price"])
                return {
                    "name": values["name"],
                    "price": price,
                    "description": values["description"],
                }
            except ValueError:
                sg.popup_error("Preço inválido!")
                return self.get_common_item_data()
        return {"name": "", "price": 0.0, "description": ""}

    def get_burger_specific_data(self) -> Dict[str, Any]:
        layout = [
            [sg.Text("Dados do Lanche", font=("Arial", 15))],
            [
                sg.Text("Tipo de Carne (ex: Carne, Frango, Peixe, Polenta):"),
                sg.InputText(key="patty_type"),
            ],
            [sg.Button("Salvar")],
        ]
        window = sg.Window("Dados do Lanche", layout)
        event, values = window.read()
        window.close()
        return {"patty_type": values["patty_type"]}

    def get_drink_specific_data(self) -> Dict[str, Any]:
        layout = [
            [sg.Text("Dados da Bebida", font=("Arial", 15))],
            [sg.Text("Volume (ml):"), sg.InputText(key="volume_ml")],
            [sg.Button("Salvar")],
        ]
        window = sg.Window("Dados da Bebida", layout)
        event, values = window.read()
        window.close()
        try:
            return {"volume_ml": int(values["volume_ml"])}
        except ValueError:
            return {"volume_ml": 0}

    def display_menu_items(self, items: List[MenuItem]) -> None:
        if not items:
            sg.popup("O cardápio está vazio.")
            return

        data = []
        for i, item in enumerate(items):
            details = ""
            if isinstance(item, Burger):
                details = f"Tipo: {item.patty_type}"
            elif isinstance(item, Drink):
                details = f"{item.volume_ml}ml"

            data.append(
                [
                    i + 1,
                    item.name,
                    f"R$ {item.price:.2f}",
                    item.description,
                    details,
                ]
            )

        layout = [
            [
                sg.Table(
                    values=data,
                    headings=["#", "Nome", "Preço", "Descrição", "Detalhes"],
                    auto_size_columns=True,
                    justification="left",
                    num_rows=min(25, len(data)),
                )
            ],
            [sg.Button("Fechar")],
        ]
        window = sg.Window("Cardápio", layout)
        window.read()
        window.close()

    def get_item_name(self) -> str:
        return (
            sg.popup_get_text("Digite o nome do item:", title="Remover Item")
            or ""
        )

    def get_item_index(self, max_index: int) -> int:
        idx_str = sg.popup_get_text(
            f"Digite o número do item desejado (1 a {max_index}):",
            title="Selecionar Item",
        )
        if idx_str:
            try:
                return int(idx_str) - 1
            except ValueError:
                return -1
        return -1
