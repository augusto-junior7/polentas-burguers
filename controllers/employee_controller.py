from collections import defaultdict
from typing import List

from daos.employees_dao import EmployeesDAO
from models.employee import Employee
from models.order import Order
from views.employee_view import EmployeeView


class EmployeeController:
    def __init__(self):
        self.__employees_dao = EmployeesDAO()
        self.__view = EmployeeView()
        if not self.__employees_dao.get_all():
            self._add_initial_employees()

    @property
    def employees(self) -> List[Employee]:
        return self.__employees_dao.get_all()

    def run_employee_menu(self, order_controller):
        while True:
            option = self.__view.display_employee_menu()
            if option == "1":
                self.add_employee()
            elif option == "2":
                self.list_employees()
            elif option == "3":
                self.search_employee_by_cpf()
            elif option == "4":
                self.update_employee()
            elif option == "5":
                self.delete_employee()
            elif option == "6":
                self.generate_employee_report(order_controller.orders)
            elif option == "0":
                break
            else:
                self.__view.display_error_message("Opção inválida.")

    def add_employee(self) -> None:
        data = self.__view.get_employee_data()
        new_employee = Employee(
            name=data["name"],
            cpf=data["cpf"],
            email=data["email"],
            phone=data["phone"],
            position=data["position"],
        )
        for emp in self.__employees_dao.get_all():
            if emp.cpf == new_employee.cpf:
                self.__view.display_error_message(
                    "Funcionário com este CPF já existe."
                )
                return
        self.__employees_dao.add(new_employee)
        self.__view.display_success_message(
            "Funcionário cadastrado com sucesso!"
        )

    def list_employees(self) -> None:
        if not self.__employees_dao.get_all():
            self.__view.display_message("Nenhum funcionário cadastrado.")
        else:
            self.__view.display_employees(self.__employees_dao.get_all())

    def search_employee_by_cpf(self) -> None:
        cpf = self.__view.get_employee_cpf()
        if cpf == "":
            return
        employee = self._find_employee_by_cpf(cpf)
        if employee:
            self.__view.display_employee(employee)
        else:
            self.__view.display_error_message("Funcionário não encontrado.")

    def update_employee(self) -> None:
        cpf = self.__view.get_employee_cpf()
        if cpf == "":
            return
        employee = self._find_employee_by_cpf(cpf)
        if not employee:
            self.__view.display_error_message("Funcionário não encontrado.")
            return

        updated_data = self.__view.get_employee_data()
        for field in ("name", "email", "phone", "position"):
            value = updated_data.get(field, "")
            if value != "":
                setattr(employee, field, value)

        self.__employees_dao.update(employee)
        self.__view.display_success_message(
            "Dados do funcionário atualizados com sucesso!"
        )

    def delete_employee(self) -> None:
        cpf = self.__view.get_employee_cpf()
        if cpf == "":
            return
        employee = self._find_employee_by_cpf(cpf)
        if employee:
            self.__employees_dao.delete(employee.id)
            self.__view.display_success_message(
                "Funcionário removido com sucesso!"
            )
        else:
            self.__view.display_error_message("Funcionário não encontrado.")

    def get_lowest_workload_employee(self, orders) -> Employee:
        if not self.__employees_dao.get_all():
            raise ValueError("Nenhum funcionário disponível.")

        workload = {emp.cpf: 0 for emp in self.__employees_dao.get_all()}
        for order in orders:
            workload[order.employee.cpf] += 1

        lowest_workload_employee_cpf = min(workload, key=workload.get)
        return self._find_employee_by_cpf(lowest_workload_employee_cpf)

    def generate_employee_report(self, orders: List[Order]) -> None:
        if not orders:
            self.__view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de vendas por funcionário."
            )
            return

        sales_data = defaultdict(lambda: {"orders": 0, "revenue": 0.0})

        for order in orders:
            employee_name = order.employee.name
            sales_data[employee_name]["orders"] += 1
            sales_data[employee_name]["revenue"] += order.total

        self.__view.display_employee_sales_report(dict(sales_data))

    def _find_employee_by_cpf(self, cpf: str) -> Employee | None:
        for employee in self.__employees_dao.get_all():
            if employee.cpf == cpf:
                return employee
        return None

    def _add_initial_employees(self) -> None:
        initial_employees = [
            {
                "name": "Carlos Silva",
                "cpf": "15469663078",
                "email": "carlos.silva@example.com",
                "phone": "4991234-5678",
                "position": "Gerente",
            },
            {
                "name": "Maria Oliveira",
                "cpf": "58778936020",
                "email": "maria.oliveira@example.com",
                "phone": "4899123-4567",
                "position": "Atendente",
            },
        ]

        for e in initial_employees:
            new_employee = Employee(
                name=e["name"],
                cpf=e["cpf"],
                email=e["email"],
                phone=e["phone"],
                position=e["position"],
            )
            self.__employees_dao.add(new_employee)
