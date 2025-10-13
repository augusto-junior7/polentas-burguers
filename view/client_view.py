from typing import Any, Dict, List

from model.client import Client
from view.abstract_view import AbstractView


class ClientView(AbstractView):
    def display_client_menu(self) -> str:
        print("\n--- Gestão de Clientes ---")
        print("1: Adicionar Cliente")
        print("2: Listar Clientes")
        print("3: Buscar Cliente por CPF")
        print("4: Atualizar Dados do Cliente")
        print("5: Remover Cliente")
        print("6: Gerar Relatório de Clientes")
        print("0: Voltar ao Menu Principal")
        return input("Escolha uma opção: ")

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

    def display_client_report(self, client_data: dict) -> None:
        """Exibe relatório de vendas por cliente."""
        print("\n=== Relatório de Clientes ===")
        if not client_data:
            print("Nenhum dado disponível.")
            return

        print(f"{'Cliente':<30} {'Pedidos':<15} {'Receita (R$)':<15}")
        print("-" * 60)

        total_orders = 0
        total_revenue = 0.0

        for client_name, data in sorted(client_data.items()):
            orders = data["orders"]
            revenue = data["revenue"]
            total_orders += orders
            total_revenue += revenue
            print(f"{client_name:<30} {orders:<15} {revenue:<15.2f}")

        print("-" * 60)
        print(f"{'TOTAL':<30} {total_orders:<15} {total_revenue:<15.2f}")
        print("=" * 60)
