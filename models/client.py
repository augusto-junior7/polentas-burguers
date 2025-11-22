from exceptions.is_not_instance import IsNotInstanceError
from models.user import User


class Client(User):
    def __init__(
        self,
        name: str,
        cpf: str,
        email: str,
        phone: str,
        address: str,
    ):
        super().__init__(name, cpf, email, phone)
        self.__address = None

        if isinstance(address, str):
            self.__address = address
        else:
            raise IsNotInstanceError("Address must be a string")

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str):
        if isinstance(value, str):
            self.__address = value
        else:
            raise IsNotInstanceError("Address must be a string")

    def display_info(self):
        print(
            f"[Cliente] ID: {super().id} | CPF: {super().cpf} | Nome: {super().name} | Endereço: {self.__address}"
        )
