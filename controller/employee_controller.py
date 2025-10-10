from typing import List

from model.employee import Employee
from view.employee_view import EmployeeView


class EmployeeController:
    def __init__(self):
        self._employees: List[Employee] = []
        self._view = EmployeeView()

    def add_employee(self) -> None:
        data = self._view.get_employee_data()
        new_employee = Employee(
            name=data["name"],
            cpf=data["cpf"],
            email=data["email"],
            phone=data["phone"],
            employee_code=data["employee_code"],
            position=data["position"],
        )
        self._employees.append(new_employee)
        self._view.display_success_message("Funcionário cadastrado com sucesso!")

    def list_employees(self) -> None:
        if not self._employees:
            self._view.display_message("Nenhum funcionário cadastrado.")
        else:
            self._view.display_employees(self._employees)

    # Você pode adicionar 'update' e 'delete' depois, seguindo o exemplo do ClientController
