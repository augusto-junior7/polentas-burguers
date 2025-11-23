from typing import Any, Dict, List

import FreeSimpleGUI as sg

from models.client import Client
from views.abstract_view import AbstractView


class ClientView(AbstractView):
    def display_client_menu(self) -> str:
        layout = [
            [sg.Text("Gestão de Clientes", font=("Arial", 20))],
            [sg.Button("Adicionar Cliente", key="1", size=(30, 2))],
            [sg.Button("Listar Clientes", key="2", size=(30, 2))],
            [sg.Button("Buscar Cliente por CPF", key="3", size=(30, 2))],
            [sg.Button("Atualizar Dados do Cliente", key="4", size=(30, 2))],
            [sg.Button("Remover Cliente", key="5", size=(30, 2))],
            [sg.Button("Gerar Relatório de Clientes", key="6", size=(30, 2))],
            [sg.Button("Voltar ao Menu Principal", key="0", size=(30, 2))],
        ]
        window = sg.Window("Menu Clientes", layout, element_justification="c")
        event, values = window.read()
        window.close()
        if event is None:
            return "0"
        return event

    def get_client_data(self) -> Dict[str, Any]:
        layout = [
            [sg.Text("Cadastro de Cliente", font=("Arial", 15))],
            [sg.Text("Nome:", size=(10, 1)), sg.InputText(key="name")],
            [sg.Text("CPF:", size=(10, 1)), sg.InputText(key="cpf")],
            [sg.Text("Email:", size=(10, 1)), sg.InputText(key="email")],
            [sg.Text("Telefone:", size=(10, 1)), sg.InputText(key="phone")],
            [sg.Text("Endereço:", size=(10, 1)), sg.InputText(key="address")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Cadastro de Cliente", layout)
        event, values = window.read()
        window.close()
        if event == "Salvar":
            return values
        return {"name": "", "cpf": "", "email": "", "phone": "", "address": ""}

    def display_clients(self, clients: List[Client]) -> None:
        if not clients:
            sg.popup("Nenhum cliente encontrado.")
            return

        client_list = []
        for client in clients:
            client_list.append(
                [
                    client.id,
                    client.cpf,
                    client.name,
                    client.email,
                    client.phone,
                    client.address,
                ]
            )

        layout = [
            [
                sg.Table(
                    values=client_list,
                    headings=[
                        "ID",
                        "CPF",
                        "Nome",
                        "Email",
                        "Telefone",
                        "Endereço",
                    ],
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification="left",
                    num_rows=min(25, len(client_list)),
                )
            ],
            [sg.Button("Fechar")],
        ]
        window = sg.Window("Lista de Clientes", layout)
        window.read()
        window.close()

    def get_client_cpf(self) -> str:
        return (
            sg.popup_get_text(
                "Informe o CPF do cliente:", title="Buscar Cliente"
            )
            or ""
        )

    def get_client_update_data(self) -> Dict[str, Any]:
        layout = [
            [
                sg.Text(
                    "Novos Dados (deixe vazio para manter atual)",
                    font=("Arial", 15),
                )
            ],
            [sg.Text("Novo Nome:"), sg.InputText(key="name")],
            [sg.Text("Novo Email:"), sg.InputText(key="email")],
            [sg.Text("Novo Telefone:"), sg.InputText(key="phone")],
            [sg.Text("Novo Endereço:"), sg.InputText(key="address")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Atualizar Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "Salvar":
            return {k: v for k, v in values.items() if v}
        return {}

    def display_client_report(self, client_data: dict) -> None:
        if not client_data:
            sg.popup("Nenhum dado disponível.")
            return

        data = []
        total_orders = 0
        total_revenue = 0.0

        for client_name, d in sorted(client_data.items()):
            orders = d["orders"]
            revenue = d["revenue"]
            total_orders += orders
            total_revenue += revenue
            data.append([client_name, orders, f"{revenue:.2f}"])

        data.append(["TOTAL", total_orders, f"{total_revenue:.2f}"])

        layout = [
            [sg.Text("Relatório de Clientes", font=("Arial", 15))],
            [
                sg.Table(
                    values=data,
                    headings=["Cliente", "Pedidos", "Receita (R$)"],
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
