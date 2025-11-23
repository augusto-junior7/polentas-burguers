import uuid
from abc import ABC, abstractmethod

from exceptions.is_not_instance import IsNotInstanceError


class MenuItem(ABC):
    @abstractmethod
    def __init__(self, name: str, price: float, description: str):
        self.__id = uuid.uuid4().int
        self.__name = None
        self.__price = None
        self.__description = None

        if isinstance(name, str):
            self.__name = name
        else:
            raise IsNotInstanceError("Name must be a string")

        if isinstance(price, (int, float)):
            self.__price = float(price)
        else:
            raise IsNotInstanceError("Price must be a number")

        if isinstance(description, str):
            self.__description = description
        else:
            raise IsNotInstanceError("Description must be a string")

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Name must be a string")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise IsNotInstanceError("Price must be a number")
        self.__price = float(value)

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Description must be a string")
        self.__description = value
