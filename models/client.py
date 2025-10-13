from exceptions.is_not_instance import IsNotInstanceError
from models.user import User


class Client(User):
    def __init__(
        self,
        id: int,
        name: str,
        cpf: str,
        email: str,
        phone: str,
        address: str,
    ):

        super().__init__(id, name, cpf, email, phone)
        self._address = None

        if isinstance(address, str):
            self._address = address
        else:
            raise IsNotInstanceError("Address must be a string")

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        if isinstance(value, str):
            self._address = value
        else:
            raise IsNotInstanceError("Address must be a string")

    def display_info(self):
        print(
            f"[Cliente] ID: {self._id} | CPF: {self._cpf} | Nome: {self._name} | Endereço: {self._address}"
        )
