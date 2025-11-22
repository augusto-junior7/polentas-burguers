import uuid
from datetime import datetime
from typing import List, Tuple

from exceptions.is_not_instance import IsNotInstanceError
from models.client import Client
from models.employee import Employee
from models.menu_item import MenuItem
from models.order_item import OrderItem


class Order:
    def __init__(self, client: Client, employee: Employee):
        self.__id = uuid.uuid4().int
        self.__client = None
        self.__employee = None
        self.__timestamp = datetime.now()
        self.__items: List[OrderItem] = []
        self.__total = 0.0
        self.__status = "Ativo"

        if isinstance(client, Client):
            self.__client = client
        else:
            raise IsNotInstanceError("Client must be an instance of Client")
        if isinstance(employee, Employee):
            self.__employee = employee
        else:
            raise IsNotInstanceError(
                "Employee must be an instance of Employee"
            )

    @property
    def id(self) -> int:
        return self.__id

    @property
    def client(self) -> Client:
        return self.__client

    @client.setter
    def client(self, value: Client):
        if not isinstance(value, Client):
            raise IsNotInstanceError("Client must be an instance of Client")
        self.__client = value

    @property
    def employee(self) -> Employee:
        return self.__employee

    @employee.setter
    def employee(self, value: Employee):
        if not isinstance(value, Employee):
            raise IsNotInstanceError(
                "Employee must be an instance of Employee"
            )
        self.__employee = value

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    @property
    def items(self) -> Tuple[OrderItem, ...]:
        return tuple(self.__items)

    @property
    def total(self) -> float:
        return self.__total

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Status must be a string")
        self.__status = value

    def add_item(self, menu_item: MenuItem, quantity: int) -> None:
        new_item = OrderItem(menu_item, quantity)
        self.__items.append(new_item)
        self._recalculate_total()

    def _recalculate_total(self) -> None:
        self.__total = sum(item.subtotal for item in self.__items)
