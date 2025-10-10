from typing import Any, Dict, List

from model.client import Client


class ClientView:
    def display_message(self, message: str) -> None:
        print(f"\n--- {message} ---\n")

    def display_success_message(self, message: str) -> None:
        print(f"\n✅ SUCESSO: {message}\n")

    def display_error_message(self, message: str) -> None:
        print(f"\n❌ ERRO: {message}\n")

    def get_client_data(self) -> Dict[str, Any]:
        print("--- Cadastro de Cliente ---")
        name = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        phone = input("Telefone: ")
        address = input("Endereço: ")
        return {
            "name": name,
            "cpf": cpf,
            "email": email,
            "phone": phone,
            "address": address,
        }

    def display_clients(self, clients: List[Client]) -> None:
        print("--- Lista de Clientes ---")
        if not clients:
            print("Nenhum cliente encontrado.")
        for client in clients:
            client.display_info()
        print("--------------------------")

    def get_client_cpf(self) -> str:
        return input("Informe o CPF do cliente: ")

    def get_client_update_data(self) -> Dict[str, Any]:
        print("--- Novos Dados (vazio mantém atual) ---")
        name = input("Novo Nome: ")
        email = input("Novo Email: ")
        phone = input("Novo Telefone: ")
        address = input("Novo Endereço: ")

        data = {}
        if name:
            data["name"] = name
        if email:
            data["email"] = email
        if phone:
            data["phone"] = phone
        if address:
            data["address"] = address
        return data
