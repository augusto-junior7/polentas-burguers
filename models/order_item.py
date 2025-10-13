from models.menu_item import MenuItem

class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int):
        self._menu_item = None
        self._quantity = None

        if isinstance(menu_item, MenuItem):
            self._menu_item = menu_item
        else:
            raise IsNotInstanceError("Item must be an instance of MenuItem")
        
        if isinstance(quantity, int) and quantity > 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a positive integer")

    @property
    def menu_item(self) -> MenuItem:
        return self._menu_item

    @menu_item.setter
    def menu_item(self, value: MenuItem):
        if not isinstance(value, MenuItem):
            raise IsNotInstanceError("Item must be an instance of MenuItem")
        self._menu_item = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Quantity must be a positive integer")
        self._quantity = value

    @property
    def subtotal(self) -> float:
        return self.menu_item.price * self.quantity
