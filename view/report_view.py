from typing import Any, Dict


class ReportView:
    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")

    def display_report_menu(self) -> str:
        print("\n--- Menu de Relatórios ---")
        print("1: Relatório de Vendas de Produtos")
        print("2: Relatório de Funcionários")
        print("3: Relatório de Clientes")
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

    def display_product_sales_report(self, sales_data: Dict[str, Any]):
        print("\n--- Relatório de Vendas de Produtos ---")

        if not sales_data:
            print("Nenhum dado de venda disponível.")
            return

        sorted_items = sorted(
            sales_data.items(),
            key=lambda item: item[1]["revenue"],
            reverse=True,
        )

        for product_name, data in sorted_items:
            quantity = data["quantity"]
            revenue = data["revenue"]
            print(f"- {product_name}:")
            print(f"  > Quantidade vendida: {quantity}")
            print(f"  > Receita total: R$ {revenue:.2f}")

        print("--------------------------")

    def display_employee_sales_report(self, sales_data: Dict[str, Any]):
        print("\n--- Relatório de Vendas por Funcionário ---")

        if not sales_data:
            print("Nenhum dado de venda disponível.")
            return

        sorted_employees = sorted(
            sales_data.items(),
            key=lambda item: item[1]["revenue"],
            reverse=True,
        )

        for employee_name, data in sorted_employees:
            orders = data["orders"]
            revenue = data["revenue"]
            print(f"- {employee_name}:")
            print(f"  > Pedidos atendidos: {orders}")
            print(f"  > Receita total gerada: R$ {revenue:.2f}")

        print("--------------------------")

    def display_client_report(self, client_data: Dict[str, Any]):
        print("\n--- Relatório de Clientes ---")

        if not client_data:
            print("Nenhum dado de cliente disponível.")
            return

        sorted_clients = sorted(
            client_data.items(),
            key=lambda item: item[1]["revenue"],
            reverse=True,
        )

        for client_name, data in sorted_clients:
            orders = data["orders"]
            revenue = data["revenue"]
            print(f"- {client_name}:")
            print(f"  > Total de pedidos: {orders}")
            print(f"  > Total gasto: R$ {revenue:.2f}")

        print("--------------------------")
