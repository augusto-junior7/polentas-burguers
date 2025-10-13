from abc import ABC, abstractmethod
from datetime import datetime

from exceptions.is_not_instance import IsNotInstanceError


class MenuItem(ABC):
    @abstractmethod
    def __init__(self, name: str, price: float, description: str):
        self._id = int(datetime.now().timestamp())
        self._name = None
        self._price = None
        self._description = None

        if isinstance(name, str):
            self._name = name
        else:
            raise IsNotInstanceError("Name must be a string")

        if isinstance(price, (int, float)):
            self._price = float(price)
        else:
            raise IsNotInstanceError("Price must be a number")

        if isinstance(description, str):
            self._description = description
        else:
            raise IsNotInstanceError("Description must be a string")

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Name must be a string")
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise IsNotInstanceError("Price must be a number")
        self._price = float(value)

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Description must be a string")
        self._description = value
