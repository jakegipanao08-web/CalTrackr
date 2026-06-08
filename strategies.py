from abc import ABC, abstractmethod


class ColorStrategy(ABC):
    """Abstract base class for color strategies."""

    @abstractmethod
    def get_progress_color(self, consumed: int, limit: int) -> str:
        pass

    @abstractmethod
    def get_text_color(self, consumed: int, limit: int) -> str:
        pass


class LimitBasedColorStrategy(ColorStrategy):
    """Returns Green if under limit, Red if over limit."""

    def get_progress_color(self, consumed: int, limit: int) -> str:
        return "#4CAF50" if consumed <= limit else "#D32F2F"

    def get_text_color(self, consumed: int, limit: int) -> str:
        return "#333333" if consumed <= limit else "#D32F2F"