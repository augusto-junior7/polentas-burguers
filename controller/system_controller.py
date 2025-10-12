from controller.client_controller import ClientController
from controller.employee_controller import EmployeeController
from controller.menu_controller import MenuController
from controller.order_controller import OrderController
from controller.report_controller import ReportController
from view.system_view import SystemView


class SystemController:
    def __init__(self):
        self._view = SystemView()
        self._client_controller = ClientController()
        self._employee_controller = EmployeeController()
        self._menu_controller = MenuController()
        self._order_controller = OrderController(
            self._client_controller,
            self._employee_controller,
            self._menu_controller,
        )
        self._report_controller = ReportController(self._order_controller)

    def run(self):
        while True:
            option = self._view.display_main_menu()

            if option == "1":  # Client Management
                self.run_client_menu()
            elif option == "2":  # Employee Management
                self.run_employee_menu()
            elif option == "3":  # Menu Management
                self.run_menu_menu()
            elif option == "4":  # Order Management
                self.run_order_menu()
            elif option == "5":  # Reports
                self.run_report_menu()
            elif option == "0":
                self._view.display_message("Saindo do sistema. Até logo!")
                break
            else:
                self._view.display_error_message("Opção inválida.")

    def run_client_menu(self):
        while True:
            option = self._view.display_client_menu()
            if option == "1":
                self._client_controller.add_client()
            elif option == "2":
                self._client_controller.list_clients()
            elif option == "3":
                self._client_controller.search_client_by_cpf()
            elif option == "4":
                self._client_controller.update_client()
            elif option == "5":
                self._client_controller.remove_client()
            elif option == "0":
                break
            else:
                self._view.display_error_message("Opção inválida.")

    def run_employee_menu(self):
        while True:
            option = self._view.display_employee_menu()
            if option == "1":
                self._employee_controller.add_employee()
            elif option == "2":
                self._employee_controller.list_employees()
            elif option == "0":
                break
            else:
                self._view.display_error_message("Opção inválida.")

    def run_menu_menu(self):
        while True:
            option = self._menu_controller._view.display_menu_management_menu()
            if option == "1":
                self._menu_controller.add_menu_item()
            elif option == "2":
                self._menu_controller.list_menu_items()
            elif option == "0":
                break
            else:
                self._view.display_error_message("Opção inválida.")

    def run_order_menu(self):
        while True:
            option = self._view.display_order_menu()
            if option == "1":
                self._order_controller.create_order()
            elif option == "2":
                self._order_controller.list_orders()
            elif option == "3":
                self._order_controller.update_order()
            elif option == "4":
                self._order_controller.cancel_order()
            elif option == "0":
                break
            else:
                self._view.display_error_message("Opção inválida.")

    def run_report_menu(self):
        while True:
            option = self._report_controller._view.display_report_menu()
            if option == "1":
                self._report_controller.generate_product_sales_report()
            elif option == "2":
                self._report_controller.generate_employee_report()
            elif option == "3":
                self._report_controller.generate_client_report()
            elif option == "0":
                break
            else:
                self._view.display_error_message("Opção inválida.")
