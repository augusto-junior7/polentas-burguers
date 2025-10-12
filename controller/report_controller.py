from collections import defaultdict

from controller.order_controller import OrderController
from view.report_view import ReportView


class ReportController:
    def __init__(self, order_controller: OrderController):
        self._order_controller = order_controller
        self._view = ReportView()

    def generate_product_sales_report(self):
        self._view.display_message(
            "Gerando Relatório de Vendas de Produtos..."
        )

        all_orders = self._order_controller._orders
        if not all_orders:
            self._view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de vendas de produtos."
            )
            return

        sales_data = defaultdict(lambda: {"quantity": 0, "revenue": 0.0})

        for order in all_orders:
            for item in order.items:
                product_name = item.menu_item.name
                sales_data[product_name]["quantity"] += item.quantity
                sales_data[product_name]["revenue"] += item.subtotal

        self._view.display_product_sales_report(dict(sales_data))
        self._view.display_product_sales_report(dict(sales_data))

    def generate_employee_report(self):
        self._view.display_message(
            "Gerando Relatório de Vendas por Funcionário..."
        )

        all_orders = self._order_controller._orders
        if not all_orders:
            self._view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de vendas por funcionário."
            )
            return

        sales_data = defaultdict(lambda: {"orders": 0, "revenue": 0.0})

        for order in all_orders:
            employee_name = order.employee.name
            sales_data[employee_name]["orders"] += 1
            sales_data[employee_name]["revenue"] += order.total

        self._view.display_employee_sales_report(dict(sales_data))

    def generate_client_report(self):
        self._view.display_message("Gerando Relatório de Clientes...")

        all_orders = self._order_controller._orders
        if not all_orders:
            self._view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de clientes."
            )
            return

        client_data = defaultdict(lambda: {"orders": 0, "revenue": 0.0})

        for order in all_orders:
            client_name = order.client.name
            client_data[client_name]["orders"] += 1
            client_data[client_name]["revenue"] += order.total

        self._view.display_client_report(dict(client_data))
