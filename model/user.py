from abc import ABC, abstractmethod

from exceptions.invalid_cpf import InvalidCPFError
from exceptions.is_not_instance import IsNotInstanceError
from utils.cpf_checker import is_valid_cpf


class User(ABC):
    @abstractmethod
    def __init__(self, id: int, name: str, cpf: str, email: str):
        self._id = None
        self._name = None
        self._cpf = None
        self._email = None

        if isinstance(id, int):
            self._id = id
        if isinstance(name, str):
            self._name = name
        if isinstance(cpf, str):
            self._cpf = cpf
        if isinstance(email, str):
            self._email = email

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        if isinstance(value, int):
            self._id = value
        else:
            raise IsNotInstanceError("ID must be an integer")

    @property
    def username(self) -> str:
        return self._name

    @username.setter
    def username(self, value: str):
        if isinstance(value, str):
            self._name = value
        else:
            raise IsNotInstanceError("Username must be a string")

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if isinstance(value, str):
            if is_valid_cpf(value):
                self._cpf = value
            else:
                raise InvalidCPFError("Invalid CPF")
        else:
            raise IsNotInstanceError("CPF must be a string")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if isinstance(value, str):
            self._email = value
        else:
            raise IsNotInstanceError("Email must be a string")
