from daos.dao import DAO
from models.employee import Employee


class EmployeesDAO(DAO):
    def __init__(self):
        super().__init__(datasource="employees.pkl")

    def add(self, employee: Employee):
        if employee is not None and isinstance(employee, Employee):
            super().add(employee)

    def get(self, employee_id: int) -> Employee | None:
        employee = super().get(employee_id)
        if employee is not None and isinstance(employee, Employee):
            return employee
        return None

    def update(self, employee: Employee):
        if employee is not None and isinstance(employee, Employee):
            super().update(employee.id, employee)
