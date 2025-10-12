from typing import List

from model.client import Client
from view.client_view import ClientView


class ClientController:
    def __init__(self):
        self._clients: List[Client] = []
        self._view = ClientView()

    def add_client(self) -> None:
        client_data = self._view.get_client_data()
        if self._find_client_by_cpf(client_data["cpf"]):
            self._view.display_error_message("Cliente com este CPF já existe.")
            return
        new_client = Client(
            name=client_data["name"],
            cpf=client_data["cpf"],
            email=client_data["email"],
            phone=client_data["phone"],
            address=client_data["address"],
        )
        # Verificar se não existe antes de adicionar
        self._clients.append(new_client)
        self._view.display_success_message("Cliente cadastrado com sucesso!")

    def list_clients(self) -> None:
        if not self._clients:
            self._view.display_message("Não há clientes cadastrados.")
        else:
            self._view.display_clients(self._clients)

    def search_client_by_cpf(self) -> None:
        cpf = self._view.get_client_cpf()
        client = self._find_client_by_cpf(cpf)
        if client:
            self._view.display_clients([client])
        else:
            self._view.display_error_message("Cliente não encontrado.")

    def update_client(self) -> None:
        cpf = self._view.get_client_cpf()
        client = self._find_client_by_cpf(cpf)

        if client:
            new_data = self._view.get_client_update_data()
            if new_data.get("name"):
                client.username = new_data["name"]
            if new_data.get("email"):
                client.email = new_data["email"]
            if new_data.get("phone"):
                client.phone = new_data["phone"]
            if new_data.get("address"):
                client.address = new_data["address"]
            self._view.display_success_message(
                "Cliente atualizado com sucesso!"
            )
        else:
            self._view.display_error_message("Cliente não encontrado.")

    def delete_client(self) -> None:
        cpf = self._view.get_client_cpf()
        client = self._find_client_by_cpf(cpf)

        if client:
            self._clients.remove(client)
            self._view.display_success_message("Cliente removido com sucesso!")
        else:
            self._view.display_error_message("Cliente não encontrado.")

    def _find_client_by_cpf(self, cpf: str) -> Client | None:
        for client in self._clients:
            if client.cpf == cpf:
                return client
        return None
