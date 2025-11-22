from exceptions.is_not_instance import IsNotInstanceError
from models.menu_item import MenuItem


class Burger(MenuItem):
    def __init__(
        self,
        name: str,
        price: float,
        description: str,
        patty_type: str = "Carne bovina",
    ):
        super().__init__(name, price, description)
        self.__patty_type = None

        if isinstance(patty_type, str):
            self.__patty_type = patty_type

    @property
    def patty_type(self) -> str:
        return self.__patty_type

    @patty_type.setter
    def patty_type(self, value: str):
        if not isinstance(value, str):
            raise IsNotInstanceError("Patty type must be a string")
        self.__patty_type = value
