from datetime import datetime
from typing import List, Tuple

from exceptions.is_not_instance import IsNotInstanceError
from model.client import Client
from model.employee import Employee
from model.menu_item import MenuItem
from model.order_item import OrderItem


class Order:
    def __init__(self, client: Client, employee: Employee):

        self._id = None
        self._client = None
        self._employee = None
        self._timestamp = datetime.now()
        self._items: List[OrderItem] = []
        self._total = 0.0

        if isinstance(client, Client):
            self._client = client
        else:
            raise IsNotInstanceError("Client must be an instance of Client")
        if isinstance(employee, Employee):
            self._employee = employee
        else:
            raise IsNotInstanceError(
                "Employee must be an instance of Employee"
            )

    @property
    def id(self) -> int:
        return self._id

    @property
    def client(self) -> Client:
        return self._client

    @client.setter
    def client(self, value: Client):
        if not isinstance(value, Client):
            raise IsNotInstanceError("Client must be an instance of Client")
        self._client = value

    @property
    def employee(self) -> Employee:
        return self._employee

    @employee.setter
    def employee(self, value: Employee):
        if not isinstance(value, Employee):
            raise IsNotInstanceError(
                "Employee must be an instance of Employee"
            )
        self._employee = value

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def items(self) -> Tuple[OrderItem, ...]:
        return tuple(self._items)

    @property
    def total(self) -> float:
        return self._total

    def add_item(self, menu_item: MenuItem, quantity: int) -> None:
        new_item = OrderItem(menu_item, quantity)
        self._items.append(new_item)
        self._recalculate_total()

    def _recalculate_total(self) -> None:
        self._total = sum(item.subtotal for item in self._items)
