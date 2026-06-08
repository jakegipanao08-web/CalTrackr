from dataclasses import dataclass
from typing import List

@dataclass
class FoodItem:
    name: str
    calories: int

class CalorieModel:
    def __init__(self, limit: int = 2000):
        self.limit = limit
        self.items: List[FoodItem] = []

    def add_item(self, name: str, calories: int) -> None:
        """Adds a food item to the list."""
        item = FoodItem(name=name.upper(), calories=calories)
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        """Removes a specific food item from the list."""
        if item in self.items:
            self.items.remove(item)

    def reset(self) -> None:
        """Clears all items."""
        self.items.clear()

    def get_total_consumed(self) -> int:
        """Calculates total calories consumed."""
        return sum(item.calories for item in self.items)

    def get_remaining(self) -> int:
        """Calculates remaining calories."""
        return self.limit - self.get_total_consumed()

    def set_limit(self, new_limit: int) -> None:
        """Updates the daily limit."""
        self.limit = new_limit