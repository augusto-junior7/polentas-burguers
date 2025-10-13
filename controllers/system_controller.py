from controllers.client_controller import ClientController
from controllers.employee_controller import EmployeeController
from controllers.menu_controller import MenuController
from controllers.order_controller import OrderController
from views.system_view import SystemView


class SystemController:
    def __init__(self):
        self.__view = SystemView()
        self.__client_controller = ClientController()
        self.__employee_controller = EmployeeController()
        self.__menu_controller = MenuController()
        self.__order_controller = OrderController(
            self.__client_controller,
            self.__employee_controller,
            self.__menu_controller,
        )

    def run(self):
        while True:
            option = self.__view.display_main_menu()

            if option == "1":  # Client Management
                self.__client_controller.run_client_menu(self.__order_controller)
            elif option == "2":  # Employee Management
                self.__employee_controller.run_employee_menu(self.__order_controller)
            elif option == "3":  # Menu Management
                self.__menu_controller.run_menu_menu()
            elif option == "4":  # Order Management
                self.__order_controller.run_order_menu()
            elif option == "0":
                self.__view.display_message("Saindo do sistema. Até logo!")
                break
            else:
                self.__view.display_error_message("Opção inválida.")
