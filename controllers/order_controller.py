from collections import defaultdict
from typing import List

from controllers.client_controller import ClientController
from controllers.employee_controller import EmployeeController
from controllers.menu_controller import MenuController
from daos.orders_dao import OrdersDAO
from models.order import Order
from views.order_view import OrderView


class OrderController:
    def __init__(
        self,
        client_controller: ClientController,
        employee_controller: EmployeeController,
        menu_controller: MenuController,
    ):
        self.__orders_dao = OrdersDAO()
        self.__view = OrderView()
        self.__client_controller = client_controller
        self.__employee_controller = employee_controller
        self.__menu_controller = menu_controller

    @property
    def orders(self) -> List[Order]:
        return self.__orders_dao.get_all()

    def run_order_menu(self):
        while True:
            option = self.__view.display_order_menu()
            if option == "1":
                self.create_order()
            elif option == "2":
                self.list_orders()
            elif option == "3":
                self.finish_order()
            elif option == "4":
                self.cancel_order()
            elif option == "5":
                self.generate_product_sales_report()
            elif option == "0":
                break
            else:
                self.__view.display_error_message("Opção inválida.")

    def create_order(self) -> None:
        client_cpf = self.__view.get_client_cpf_for_order()
        if client_cpf == "":
            return
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

        employee = self.__employee_controller.get_lowest_workload_employee(
            self.__orders_dao.get_all()
        )
        self.__view.display_message(
            f"O funcionário '{employee.name}' está atendendo o pedido."
        )

        new_order = Order(client=client, employee=employee)

        while True:
            items = list(self.__menu_controller.menu.items)
            index, quantity = self.__view.get_item_and_quantity(items)

            if index == -1:
                break

            menu_item = items[index]
            new_order.add_item(menu_item, quantity)
            self.__view.display_current_order(new_order)

        if not new_order.items:
            self.__view.display_message(
                "Pedido cancelado pois nenhum item foi adicionado."
            )
            return

        self.__orders_dao.add(new_order)
        self.__view.display_final_order_summary(new_order)
        self.__view.display_success_message("Pedido criado com sucesso!")

    def list_orders(self) -> None:
        self.__view.display_order_list(self.__orders_dao.get_all())

    def finish_order(self) -> None:
        if not self.__orders_dao.get_all():
            self.__view.display_message("Nenhum pedido para finalizar.")
            return

        orders = self.__orders_dao.get_all()
        order_id = self.__view.get_order_id_for_update(orders, "finalizar")
        if order_id == 0:
            return
        order = self._find_order_by_id(order_id)
        if not order:
            self.__view.display_error_message("Pedido não encontrado.")
            return

        order.status = "Concluído"
        self.__orders_dao.update(order)
        self.__view.display_success_message("Pedido finalizado com sucesso!")

    def cancel_order(self) -> None:
        if not self.__orders_dao.get_all():
            self.__view.display_message("Nenhum pedido para cancelar.")
            return

        orders = self.__orders_dao.get_all()
        order_id = self.__view.get_order_id_for_update(orders, "cancelar")
        if order_id == 0:
            return
        order = self._find_order_by_id(order_id)
        if not order:
            self.__view.display_error_message("Pedido não encontrado.")
            return

        order.status = "Cancelado"
        self.__orders_dao.update(order)
        self.__view.display_success_message("Pedido cancelado com sucesso!")

    def generate_product_sales_report(self) -> None:
        orders = [
            order
            for order in self.__orders_dao.get_all()
            if order.status == "Concluído"
        ]

        if not orders:
            self.__view.display_error_message(
                "Nenhum pedido concluído encontrado para gerar um relatório de vendas de produtos."
            )
            return

        sales_data = defaultdict(lambda: {"quantity": 0, "revenue": 0.0})

        for order in orders:
            for item in order.items:
                product_name = item.menu_item.name
                sales_data[product_name]["quantity"] += item.quantity
                sales_data[product_name]["revenue"] += item.subtotal

        self.__view.display_product_sales_report(dict(sales_data))

    def _find_order_by_id(self, order_id: int) -> Order | None:
        for order in self.__orders_dao.get_all():
            if order.id == order_id:
                return order
        return None
