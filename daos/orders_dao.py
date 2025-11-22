from daos.dao import DAO
from models.order import Order


class OrdersDAO(DAO):
    def __init__(self):
        super().__init__(datasource="orders.pkl")

    def add(self, order: Order):
        if order is not None and isinstance(order, Order):
            super().add(order.id, order)

    def get(self, order_id: int) -> Order | None:
        order = super().get(order_id)
        if order is not None and isinstance(order, Order):
            return order
        return None

    def update(self, order: Order):
        if order is not None and isinstance(order, Order):
            super().add(order.id, order)

    def remove(self, order_id: int):
        super().remove(order_id)

    def get_all(self) -> list:
        return list(super().get_all())
