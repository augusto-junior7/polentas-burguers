from typing import List, Tuple

from exceptions.is_not_instance import IsNotInstanceError
from models.menu_item import MenuItem


class Menu:
    def __init__(self):
        self._items: List[MenuItem] = []

    @property
    def items(self) -> Tuple[MenuItem, ...]:
        return tuple(self._items)

    def add_item(self, item: MenuItem) -> None:
        if not isinstance(item, MenuItem):
            raise IsNotInstanceError("Item must be an instance of MenuItem")

        for existing_item in self._items:
            if existing_item.name.lower() == item.name.lower():
                raise ValueError(
                    f"Item with name '{item.name}' already exists in the menu."
                )

        self._items.append(item)

    def remove_item(self, item_name: str) -> bool:
        item_to_remove = self.get_item_by_name(item_name)
        if item_to_remove:
            self._items.remove(item_to_remove)
            return True
        return False

    def get_item_by_name(self, item_name: str) -> MenuItem | None:
        for item in self._items:
            if item.name.lower() == item_name.lower():
                return item
        return None
