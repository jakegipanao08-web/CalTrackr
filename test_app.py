import pytest
from models import CalorieModel, FoodItem
from strategies import LimitBasedColorStrategy


class TestCalorieModel:
    """Test CalorieModel functionality."""

    def test_add_item(self):
        """Test adding a food item."""
        model = CalorieModel()
        model.add_item("Apple", 95)
        assert len(model.items) == 1
        assert model.items[0].calories == 95

    def test_get_total_consumed(self):
        """Test total calories calculation."""
        model = CalorieModel()
        model.add_item("Apple", 95)
        model.add_item("Banana", 105)
        assert model.get_total_consumed() == 200

    def test_get_remaining(self):
        """Test remaining calories calculation."""
        model = CalorieModel(limit=2000)
        model.add_item("Apple", 500)
        assert model.get_remaining() == 1500

    def test_reset(self):
        """Test reset clears all items."""
        model = CalorieModel()
        model.add_item("Apple", 95)
        model.reset()
        assert len(model.items) == 0


class TestColorStrategy:
    """Test LimitBasedColorStrategy."""

    def test_color_under_limit(self):
        """Test green color when under limit."""
        strategy = LimitBasedColorStrategy()
        assert strategy.get_progress_color(1000, 2000) == "#4CAF50"

    def test_color_over_limit(self):
        """Test red color when over limit."""
        strategy = LimitBasedColorStrategy()
        assert strategy.get_progress_color(2500, 2000) == "#D32F2F"
