from typing import List

from model.employee import Employee
from view.employee_view import EmployeeView


class EmployeeController:
    def __init__(self):
        self.__employees: List[Employee] = []
        self.__view = EmployeeView()

    def add_employee(self) -> None:
        data = self.__view.get_employee_data()
        new_employee = Employee(
            name=data["name"],
            cpf=data["cpf"],
            email=data["email"],
            phone=data["phone"],
            position=data["position"],
        )
        # Verifica se o funcionário já existe na lista de funcionários
        self.__employees.append(new_employee)
        self.__view.display_success_message(
            "Funcionário cadastrado com sucesso!"
        )

    def list_employees(self) -> None:
        if not self.__employees:
            self.__view.display_message("Nenhum funcionário cadastrado.")
        else:
            self.__view.display_employees(self.__employees)

    @property
    def _employees(self) -> List[Employee]:
        return self.__employees