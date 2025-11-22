from daos.dao import DAO
from models.client import Client


class ClientsDAO(DAO):
    def __init__(self):
        super().__init__(datasource="clients.pkl")

    def add(self, client: Client):
        if client is not None and isinstance(client, Client):
            super().add(client)

    def get(self, client_id: int) -> Client | None:
        client = super().get(client_id)
        if client is not None and isinstance(client, Client):
            return client
        return None

    def update(self, client: Client):
        if client is not None and isinstance(client, Client):
            super().update(client.id, client)
