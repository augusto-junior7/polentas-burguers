from typing import List

import FreeSimpleGUI as sg

from models.order import Order
from views.abstract_view import AbstractView


class OrderView(AbstractView):
    def display_order_menu(self) -> str:
        layout = [
            [sg.Text("Menu de Pedidos", font=("Arial", 20))],
            [sg.Button("Criar Pedido", key="1", size=(30, 2))],
            [sg.Button("Listar Pedidos", key="2", size=(30, 2))],
            [sg.Button("Finalizar Pedido", key="3", size=(30, 2))],
            [sg.Button("Cancelar Pedido", key="4", size=(30, 2))],
            [sg.Button("Gerar Relatório de Vendas", key="5", size=(30, 2))],
            [sg.Button("Voltar ao Menu Principal", key="0", size=(30, 2))],
        ]
        window = sg.Window("Menu Pedidos", layout, element_justification="c")
        event, values = window.read()
        window.close()
        if event is None:
            return "0"
        return event

    def get_client_cpf_for_order(self) -> str:
        return (
            sg.popup_get_text(
                "Digite o CPF do cliente para este pedido:",
                title="Cliente do Pedido",
            )
            or ""
        )

    def get_order_id_for_update(
        self, orders: List[Order], message: str = "modificar"
    ) -> int:
        if not orders:
            sg.popup("Não há pedidos disponíveis.")
            return 0

        data = []
        for order in orders:
            data.append(
                [
                    order.id,
                    order.client.name,
                    f"R$ {order.total:.2f}",
                    order.status,
                ]
            )

        layout = [
            [
                sg.Text(
                    f"Selecione um pedido para {message}:",
                    font=("Arial", 12),
                )
            ],
            [
                sg.Table(
                    values=data,
                    headings=["ID", "Cliente", "Total", "Status"],
                    auto_size_columns=True,
                    justification="left",
                    num_rows=min(15, len(data)),
                    key="-TABLE-",
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                )
            ],
            [sg.Button("Selecionar"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Selecionar Pedido", layout)

        selected_id = 0

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Cancelar"):
                break

            if event == "Selecionar":
                if values["-TABLE-"]:
                    row_index = values["-TABLE-"][0]
                    selected_id = data[row_index][0]
                    break
                else:
                    sg.popup_error("Por favor, selecione um pedido na lista.")

        window.close()
        return selected_id

    def get_item_and_quantity(self, menu_items: List) -> tuple[int, int]:
        if not menu_items:
            sg.popup("O cardápio está vazio.")
            return -1, 0

        data = []
        for i, item in enumerate(menu_items):
            data.append(
                [i + 1, item.name, f"R$ {item.price:.2f}", item.description]
            )

        layout = [
            [sg.Text("Selecione um item do cardápio:", font=("Arial", 15))],
            [
                sg.Table(
                    values=data,
                    headings=["#", "Nome", "Preço", "Descrição"],
                    auto_size_columns=True,
                    justification="left",
                    num_rows=min(15, len(data)),
                    key="-TABLE-",
                )
            ],
            [
                sg.Text("Número do Item:"),
                sg.InputText(key="item_idx", size=(5, 1)),
                sg.Text("Quantidade:"),
                sg.InputText(key="quantity", size=(5, 1), default_text="1"),
            ],
            [sg.Button("Adicionar"), sg.Button("Concluir Pedido")],
        ]

        window = sg.Window("Adicionar Item ao Pedido", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Concluir Pedido"):
                window.close()
                return -1, 0

            if event == "Adicionar":
                try:
                    idx = int(values["item_idx"]) - 1
                    qty = int(values["quantity"])

                    if 0 <= idx < len(menu_items) and qty > 0:
                        window.close()
                        return idx, qty
                    else:
                        sg.popup_error("Item ou quantidade inválidos!")
                except ValueError:
                    sg.popup_error("Por favor, digite números válidos.")

    def display_current_order(self, order: Order) -> None:
        items_str = ""
        for item in order.items:
            items_str += f"- {item.quantity}x {item.menu_item.name}\n"

        sg.popup(
            f"Pedido Atual:\n\n{items_str}\nTotal Atual: R$ {order.total:.2f}",
            title="Pedido em Andamento",
        )

    def display_final_order_summary(self, order: Order) -> None:
        items_str = ""
        for item in order.items:
            items_str += f"- {item.quantity}x {item.menu_item.name} (Sub: R$ {item.subtotal:.2f})\n"

        sg.popup(
            f"Resumo do Pedido #{order.id}\nCliente: {order.client.name}\n\n{items_str}\nTOTAL FINAL: R$ {order.total:.2f}",
            title="Pedido Criado",
        )

    def display_order_list(self, orders: List[Order]) -> None:
        if not orders:
            sg.popup("Não há pedidos registrados.")
            return

        data = []
        for order in orders:
            data.append(
                [
                    order.id,
                    order.client.name,
                    f"R$ {order.total:.2f}",
                    order.status,
                ]
            )

        layout = [
            [
                sg.Table(
                    values=data,
                    headings=["ID", "Cliente", "Total", "Status"],
                    auto_size_columns=True,
                    justification="left",
                    num_rows=min(25, len(data)),
                )
            ],
            [sg.Button("Fechar")],
        ]
        window = sg.Window("Lista de Pedidos", layout)
        window.read()
        window.close()

    def display_product_sales_report(self, sales_data: dict) -> None:
        if not sales_data:
            sg.popup("Nenhum dado disponível.")
            return

        data = []
        total_quantity = 0
        total_revenue = 0.0

        for product_name, d in sorted(sales_data.items()):
            qty = d["quantity"]
            rev = d["revenue"]
            total_quantity += qty
            total_revenue += rev
            data.append([product_name, qty, f"{rev:.2f}"])

        data.append(["TOTAL", total_quantity, f"{total_revenue:.2f}"])

        layout = [
            [sg.Text("Relatório de Vendas de Produtos", font=("Arial", 15))],
            [
                sg.Table(
                    values=data,
                    headings=["Produto", "Quantidade", "Receita (R$)"],
                    auto_size_columns=True,
                    justification="left",
                    num_rows=min(25, len(data)),
                )
            ],
            [sg.Button("Fechar")],
        ]
        window = sg.Window("Relatório", layout)
        window.read()
        window.close()

        for product, data in sorted(sales_data.items()):
            quantity = data["quantity"]
            revenue = data["revenue"]
            total_quantity += quantity
            total_revenue += revenue
