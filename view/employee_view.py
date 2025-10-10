from typing import Any, Dict, List

from model.employee import Employee


class EmployeeView:
    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_success_message(self, message: str) -> None:
        print(f"\n✅ SUCCESSO: {message}\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")

    def get_employee_data(self) -> Dict[str, Any]:
        print("--- Cadastro de Funcionário ---")
        name = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        phone = input("Telefone: ")
        employee_code = input("Código do Funcionário: ")
        position = input("Cargo: ")
        return {
            "name": name,
            "cpf": cpf,
            "email": email,
            "phone": phone,
            "employee_code": employee_code,
            "position": position,
        }

    def display_employees(self, employees: List[Employee]) -> None:
        print("--- Lista de Funcionários ---")
        if not employees:
            print("Nenhum funcionário encontrado.")
        for employee in employees:
            employee.display_info()
        print("-------------------")
