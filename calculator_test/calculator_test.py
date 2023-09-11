import reflex as rx
from calculator_test import style
from calculator_test.state import State


def index() -> rx.Component:
    return rx.vstack(
        rx.text("Example Calculator", style=style.heading_style),
        rx.container(
            rx.text(State.number, style=style.message_style),
            rx.hstack(
                rx.button(
                    "C", style=style.button_style
                ),
                rx.button(
                    "CE", style=style.button_style
                    ),
                rx.button(
                    "DEL", style=style.button_style
                    ),
                rx.button(
                    "/", style=style.button_style
                    ),
            ),
            rx.hstack(
                rx.button(
                    "7",
                    style=style.button_style,
                    ),
                rx.button(
                    "8", style=style.button_style
                    ),
                rx.button(
                    "9", style=style.button_style
                    ),
                rx.button(
                    "+", style=style.button_style
                    ),
            ),
            rx.hstack(
                rx.button(
                    "4", style=style.button_style
                    ),
                rx.button(
                    "5", style=style.button_style
                    ),
                rx.button(
                    "6", style=style.button_style
                    ),
                rx.button(
                    "-", style=style.button_style
                    ),
            ),
            rx.hstack(
                rx.button(
                    "1", style=style.button_style
                    ),
                rx.button(
                    "2", style=style.button_style
                    ),
                rx.button(
                    "3", style=style.button_style
                    ),
                rx.button(
                    "*", style=style.button_style
                    ),
            ),
            rx.hstack(
                rx.button(
                    "sqrt", style=style.button_style
                    ),
                rx.button(
                    "0", style=style.button_style
                    ),
                rx.button(
                    ".", style=style.button_style
                    ),
                rx.button(
                    "=", style=style.button_style
                    ),
            ),
            width="50%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index, title="Calculator")
app.compile()
