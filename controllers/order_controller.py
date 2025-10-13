from collections import defaultdict
from typing import List

from controllers.client_controller import ClientController
from controllers.employee_controller import EmployeeController
from controllers.menu_controller import MenuController
from models.order import Order
from views.order_view import OrderView


class OrderController:
    def __init__(
        self,
        client_controller: ClientController,
        employee_controller: EmployeeController,
        menu_controller: MenuController,
    ):
        self.__orders: List[Order] = []
        self.__view = OrderView()
        self.__client_controller = client_controller
        self.__employee_controller = employee_controller
        self.__menu_controller = menu_controller

    @property
    def orders(self) -> List[Order]:
        return self.__orders

    def run_order_menu(self):
        while True:
            option = self.__view.display_order_menu()
            if option == "1":
                self.create_order()
            elif option == "2":
                self.list_orders()
            elif option == "3":
                self.cancel_order()
            elif option == "4":
                self.generate_product_sales_report()
            elif option == "0":
                break
            else:
                self.__view.display_error_message("Opção inválida.")

    def create_order(self) -> None:
        self.__view.display_message("--- Iniciando Novo Pedido ---")

        self.__client_controller.list_clients()
        client_cpf = self.__view.get_client_cpf_for_order()
        client = self.__client_controller._find_client_by_cpf(client_cpf)
        if not client:
            self.__view.display_error_message(
                "Cliente não encontrado. Abortando pedido."
            )
            return

        if not self.__employee_controller.employees:
            self.__view.display_error_message(
                "Sem funcionários disponíveis. Abortando pedido."
            )
            return
        
        employee = self.__employee_controller.get_lowest_workload_employee(self.__orders)
        self.__view.display_message(
            f"O funcionário '{employee.name}' está atendendo o pedido."
        )

        new_order = Order(client=client, employee=employee)

        while True:
            self.__menu_controller.list_menu_items()
            item_name = self.__view.get_item_to_add()

            if item_name.lower() == "concluir" or item_name == "":
                break

            menu_item = self.__menu_controller.menu.get_item_by_name(item_name)
            if not menu_item:
                self.__view.display_error_message("Item não encontrado.")
                continue

            quantity = self.__view.get_quantity()
            if quantity > 0:
                new_order.add_item(menu_item, quantity)
                self.__view.display_current_order(new_order)
            else:
                self.__view.display_error_message("Quantidade inválida.")

        if not new_order.items:
            self.__view.display_message(
                "Pedido cancelado pois nenhum item foi adicionado."
            )
            return

        self.__orders.append(new_order)
        self.__view.display_final_order_summary(new_order)
        self.__view.display_success_message("Pedido criado com sucesso!")

    def list_orders(self) -> None:
        self.__view.display_order_list(self.__orders)

    def cancel_order(self) -> None:
        if not self.__orders:
            self.__view.display_message("Nenhum pedido para cancelar.")
            return

        self.list_orders()
        order_id = self.__view.get_order_id_for_update()
        order = self._find_order_by_id(order_id)
        if not order:
            self.__view.display_error_message("Pedido não encontrado.")
            return

        order.status = "Cancelado"
        self.__view.display_success_message("Pedido cancelado com sucesso!")

    def generate_product_sales_report(self) -> None:
        self.__view.display_message(
            "Gerando Relatório de Vendas de Produtos..."
        )

        if not self.__orders:
            self.__view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de vendas de produtos."
            )
            return

        sales_data = defaultdict(lambda: {"quantity": 0, "revenue": 0.0})

        for order in self.__orders:
            for item in order.items:
                product_name = item.menu_item.name
                sales_data[product_name]["quantity"] += item.quantity
                sales_data[product_name]["revenue"] += item.subtotal

        self.__view.display_product_sales_report(dict(sales_data))

    def _find_order_by_id(self, order_id: int) -> Order | None:
        for order in self.__orders:
            if order.id == order_id:
                return order
        return None