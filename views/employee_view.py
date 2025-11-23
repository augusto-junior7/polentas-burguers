from typing import Any, Dict, List

import FreeSimpleGUI as sg

from models.employee import Employee
from views.abstract_view import AbstractView


class EmployeeView(AbstractView):
    def display_employee_menu(self) -> str:
        layout = [
            [sg.Text("Gestão de Funcionários", font=("Arial", 20))],
            [sg.Button("Adicionar Funcionário", key="1", size=(30, 2))],
            [sg.Button("Listar Funcionários", key="2", size=(30, 2))],
            [sg.Button("Buscar Funcionário por CPF", key="3", size=(30, 2))],
            [
                sg.Button(
                    "Atualizar Dados do Funcionário", key="4", size=(30, 2)
                )
            ],
            [sg.Button("Remover Funcionário", key="5", size=(30, 2))],
            [
                sg.Button(
                    "Gerar Relatório de Funcionários", key="6", size=(30, 2)
                )
            ],
            [sg.Button("Voltar ao Menu Principal", key="0", size=(30, 2))],
        ]
        window = sg.Window(
            "Menu Funcionários", layout, element_justification="c"
        )
        event, values = window.read()
        window.close()
        if event is None:
            return "0"
        return event

    def get_employee_data(self) -> Dict[str, Any]:
        layout = [
            [sg.Text("Cadastro de Funcionário", font=("Arial", 15))],
            [sg.Text("Nome:", size=(10, 1)), sg.InputText(key="name")],
            [sg.Text("CPF:", size=(10, 1)), sg.InputText(key="cpf")],
            [sg.Text("Email:", size=(10, 1)), sg.InputText(key="email")],
            [sg.Text("Telefone:", size=(10, 1)), sg.InputText(key="phone")],
            [sg.Text("Cargo:", size=(10, 1)), sg.InputText(key="position")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Cadastro de Funcionário", layout)
        event, values = window.read()
        window.close()
        if event == "Salvar":
            return values
        return {
            "name": "",
            "cpf": "",
            "email": "",
            "phone": "",
            "position": "",
        }

    def display_employees(self, employees: List[Employee]) -> None:
        if not employees:
            sg.popup("Nenhum funcionário encontrado.")
            return

        data = []
        for emp in employees:
            data.append(
                [emp.id, emp.cpf, emp.name, emp.email, emp.phone, emp.position]
            )

        layout = [
            [
                sg.Table(
                    values=data,
                    headings=[
                        "ID",
                        "CPF",
                        "Nome",
                        "Email",
                        "Telefone",
                        "Cargo",
                    ],
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification="left",
                    num_rows=min(25, len(data)),
                )
            ],
            [sg.Button("Fechar")],
        ]
        window = sg.Window("Lista de Funcionários", layout)
        window.read()
        window.close()

    def get_employee_cpf(self) -> str:
        return (
            sg.popup_get_text(
                "Informe o CPF do funcionário:", title="Buscar Funcionário"
            )
            or ""
        )

    def display_employee_sales_report(self, sales_data: dict) -> None:
        if not sales_data:
            sg.popup("Nenhum dado disponível.")
            return

        data = []
        total_orders = 0
        total_revenue = 0.0

        for employee_name, d in sorted(sales_data.items()):
            orders = d["orders"]
            revenue = d["revenue"]
            total_orders += orders
            total_revenue += revenue
            data.append([employee_name, orders, f"{revenue:.2f}"])

        data.append(["TOTAL", total_orders, f"{total_revenue:.2f}"])

        layout = [
            [
                sg.Text(
                    "Relatório de Vendas por Funcionário",
                    font=("Arial", 15),
                )
            ],
            [
                sg.Table(
                    values=data,
                    headings=["Funcionário", "Pedidos", "Receita (R$)"],
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
