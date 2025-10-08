from abc import ABC, abstractmethod

from exceptions.invalid_cpf import InvalidCPFError
from exceptions.invalid_email import InvalidEmailError
from exceptions.invalid_phone import InvalidPhoneError
from exceptions.is_not_instance import IsNotInstanceError
from utils.cpf_checker import is_valid_cpf
from utils.email_checker import is_valid_email
from utils.phone_checker import is_valid_phone


class User(ABC):
    @abstractmethod
    def __init__(self, name: str, cpf: str, email: str, phone: str):
        self._id = None
        self._name = None
        self._cpf = None
        self._email = None
        self._phone = None

        if isinstance(name, str):
            self._name = name
        if isinstance(cpf, str):
            self._cpf = cpf
        if isinstance(email, str):
            self._email = email
        if isinstance(phone, str):
            self._phone = phone

    @property
    def id(self) -> int:
        return self._id

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
            if is_valid_email(value):
                self._email = value
            else:
                raise InvalidEmailError("Invalid email address")
        else:
            raise IsNotInstanceError("Email must be a string")

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if isinstance(value, str):
            if is_valid_phone(value):
                self._phone = value
            else:
                raise InvalidPhoneError("Invalid phone number")
        else:
            raise IsNotInstanceError("Phone must be a string")
