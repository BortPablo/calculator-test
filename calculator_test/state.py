import reflex as rx
from src.medium_calculator import MediumCalculator

class State(rx.State):
    result = 0
    number = ""

    def add(self, x) -> str:
        self.number = self.number + x
        return self.number
