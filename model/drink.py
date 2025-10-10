from exceptions.is_not_instance import IsNotInstanceError
from model.menu_item import MenuItem


class Drink(MenuItem):
    def __init__(
        self, name: str, price: float, description: str, volume_ml: int
    ):
        super().__init__(name, price, description)
        self._volume_ml = None
        self.volume_ml = volume_ml

    @property
    def volume_ml(self) -> int:
        return self._volume_ml

    @volume_ml.setter
    def volume_ml(self, value: int):
        if not isinstance(value, int):
            raise IsNotInstanceError("Volume must be an integer")
        self._volume_ml = value
