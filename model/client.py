from typing import List, Tuple

from exceptions.is_not_instance import IsNotInstanceError
from model.order import Order
from model.user import User


class Client(User):
    def __init__(self, name: str, cpf: str, email: str, address: str):
        super().__init__(name, cpf, email)
        self._address = None
        self._orders: List[Order] = []

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

    @property
    def orders(self) -> Tuple[Order, ...]:
        return tuple(self._orders)

    def add_order(self, order: Order) -> None:
        if not isinstance(order, Order):
            raise IsNotInstanceError("Order must be an instance of Order")
        self._orders.append(order)

    def remove_order(self, order: Order) -> None:
        if order in self._orders:
            self._orders.remove(order)
        else:
            raise ValueError("Order not found in client's orders")

    def clear_orders(self) -> None:
        self._orders.clear()
