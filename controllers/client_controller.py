from collections import defaultdict
from typing import List

from daos.clients_dao import ClientsDAO
from models.client import Client
from models.order import Order
from views.client_view import ClientView


class ClientController:
    def __init__(self):
        self.__clients_dao = ClientsDAO()
        self.__view = ClientView()
        if not self.__clients_dao.get_all():
            self._add_initial_clients()

    @property
    def clients(self) -> List[Client]:
        return self.__clients_dao.get_all()

    def run_client_menu(self, order_controller):
        while True:
            option = self.__view.display_client_menu()
            if option == "1":
                self.add_client()
            elif option == "2":
                self.list_clients()
            elif option == "3":
                self.search_client_by_cpf()
            elif option == "4":
                self.update_client()
            elif option == "5":
                self.delete_client()
            elif option == "6":
                self.generate_client_report(order_controller.orders)
            elif option == "0":
                break
            else:
                self.__view.display_error_message("Opção inválida.")

    def add_client(self) -> None:
        client_data = self.__view.get_client_data()

        if client_data["cpf"] == "":
            return

        if self._find_client_by_cpf(client_data["cpf"]):
            self.__view.display_error_message(
                "Cliente com este CPF já existe."
            )
            return

        try:
            new_client = Client(
                name=client_data["name"],
                cpf=client_data["cpf"],
                email=client_data["email"],
                phone=client_data["phone"],
                address=client_data["address"],
            )
        except Exception as e:
            self.__view.display_error_message(f"Erro ao criar cliente: {e}")
            return

        self.__clients_dao.add(new_client)
        self.__view.display_success_message("Cliente cadastrado com sucesso!")

    def list_clients(self) -> None:
        clients = self.__clients_dao.get_all()
        if not clients:
            self.__view.display_message("Não há clientes cadastrados.")
        else:
            self.__view.display_clients(clients)

    def search_client_by_cpf(self) -> None:
        cpf = self.__view.get_client_cpf()
        if cpf == "":
            return
        client = self._find_client_by_cpf(cpf)
        if client:
            self.__view.display_clients([client])
        else:
            self.__view.display_error_message("Cliente não encontrado.")

    def update_client(self) -> None:
        cpf = self.__view.get_client_cpf()
        if cpf == "":
            return
        client = self._find_client_by_cpf(cpf)

        if client:
            updated_data = self.__view.get_client_update_data()
            for field in ("name", "email", "phone", "address"):
                value = updated_data.get(field, "")
                if value != "":
                    setattr(client, field, value)

            self.__clients_dao.update(client)
            self.__view.display_success_message(
                "Cliente atualizado com sucesso!"
            )
        else:
            self.__view.display_error_message("Cliente não encontrado.")

    def delete_client(self) -> None:
        cpf = self.__view.get_client_cpf()
        if cpf == "":
            return
        client = self._find_client_by_cpf(cpf)

        if client:
            self.__clients_dao.delete(client.id)
            self.__view.display_success_message(
                "Cliente removido com sucesso!"
            )
        else:
            self.__view.display_error_message("Cliente não encontrado.")

    def generate_client_report(self, orders: List[Order]) -> None:
        if not orders:
            self.__view.display_error_message(
                "Nenhum pedido encontrado para gerar um relatório de clientes."
            )
            return

        client_data = defaultdict(lambda: {"orders": 0, "revenue": 0.0})

        for order in orders:
            client_name = order.client.name
            client_data[client_name]["orders"] += 1
            client_data[client_name]["revenue"] += order.total

        self.__view.display_client_report(dict(client_data))

    def _find_client_by_cpf(self, cpf: str) -> Client | None:
        for client in self.__clients_dao.get_all():
            if client.cpf == cpf:
                return client
        return None

    def _add_initial_clients(self) -> None:
        initial_clients = [
            {
                "name": "Ana Silva",
                "cpf": "83072939012",
                "email": "ana.silva@example.com",
                "phone": "5791234-5678",
                "address": "Rua A, 123",
            },
            {
                "name": "Bruno Souza",
                "cpf": "08444686069",
                "email": "bruno.souza@example.com",
                "phone": "6391234-1234",
                "address": "Rua B, 456",
            },
        ]
        for c in initial_clients:
            new_client = Client(
                name=c["name"],
                cpf=c["cpf"],
                email=c["email"],
                phone=c["phone"],
                address=c["address"],
            )
            self.__clients_dao.add(new_client)
