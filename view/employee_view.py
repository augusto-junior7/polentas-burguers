from typing import Any, Dict, List

from model.employee import Employee
from view.abstract_view import AbstractView


class EmployeeView(AbstractView):
    def display_employee_menu(self) -> str:
        print("\n--- Gestão de Funcionários ---")
        print("1: Adicionar Funcionário")
        print("2: Listar Funcionários")
        print("3: Buscar Funcionário por CPF")
        print("4: Atualizar Dados do Funcionário")
        print("5: Remover Funcionário")
        print("6: Gerar Relatório de Funcionários")
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def get_employee_data(self) -> Dict[str, Any]:
        print("--- Cadastro de Funcionário ---")
        name = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        phone = input("Telefone: ")
        position = input("Cargo: ")
        return {
            "name": name,
            "cpf": cpf,
            "email": email,
            "phone": phone,
            "position": position,
        }

    def display_employees(self, employees: List[Employee]) -> None:
        print("--- Lista de Funcionários ---")
        if not employees:
            print("Nenhum funcionário encontrado.")
        for employee in employees:
            employee.display_info()
        print("-------------------")

    def display_employee_sales_report(self, sales_data: dict) -> None:
        print("\n=== Relatório de Vendas por Funcionário ===")
        if not sales_data:
            print("Nenhum dado disponível.")
            return

        print(f"{'Funcionário':<30} {'Pedidos':<15} {'Receita (R$)':<15}")
        print("-" * 60)

        total_orders = 0
        total_revenue = 0.0

        for employee_name, data in sorted(sales_data.items()):
            orders = data["orders"]
            revenue = data["revenue"]
            total_orders += orders
            total_revenue += revenue
            print(f"{employee_name:<30} {orders:<15} {revenue:<15.2f}")

        print("-" * 60)
        print(f"{'TOTAL':<30} {total_orders:<15} {total_revenue:<15.2f}")
        print("=" * 60)
