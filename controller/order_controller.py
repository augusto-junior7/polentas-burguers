from typing import List

from controller.client_controller import ClientController
from controller.employee_controller import EmployeeController
from controller.menu_controller import MenuController
from model.order import Order
from view.order_view import OrderView


class OrderController:
    def __init__(
        self,
        client_controller: ClientController,
        employee_controller: EmployeeController,
        menu_controller: MenuController,
    ):
        self._orders: List[Order] = []
        self._view = OrderView()
        self._client_controller = client_controller
        self._employee_controller = employee_controller
        self._menu_controller = menu_controller

    def create_order(self) -> None:
        self._view.display_message("--- Starting New Order ---")

        self._client_controller.list_clients()
        client_cpf = self._view.get_client_cpf_for_order()
        client = self._client_controller._find_client_by_cpf(client_cpf)
        if not client:
            self._view.display_error_message(
                "Client not found. Aborting order."
            )
            return

        if not self._employee_controller._employees:
            self._view.display_error_message(
                "No employees available. Aborting order."
            )
            return
        employee = self._employee_controller._employees[0]
        self._view.display_message(
            f"Employee '{employee.name}' is handling the order."
        )

        new_order = Order(client=client, employee=employee)

        while True:
            self._menu_controller.list_menu_items()
            item_name = self._view.get_item_to_add()

            if item_name.lower() == "done":
                break

            menu_item = self._menu_controller._menu.get_item_by_name(item_name)
            if not menu_item:
                self._view.display_error_message("Item not found.")
                continue

            quantity = self._view.get_quantity()
            if quantity > 0:
                new_order.add_item(menu_item, quantity)
                self._view.display_current_order(new_order)
            else:
                self._view.display_error_message("Invalid quantity.")

        # Etapa 4: Finalizar o Pedido
        if not new_order.items:
            self._view.display_message(
                "Order cancelled as no items were added."
            )
            return

        self._orders.append(new_order)
        self._view.display_final_order_summary(new_order)
        self._view.display_success_message("Order created successfully!")

    def list_orders(self) -> None:
        self._view.display_order_list(self._orders)
