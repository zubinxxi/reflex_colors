"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.navbar import navbar
from .components.styles import (
    PAGE,
    CONTENT_WRAPPER,
    GRID_3_COLS,
    COL_SPAN_1,
    COL_SPAN_2,
)

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
                class_name=GRID_3_COLS,
            ),
            class_name=CONTENT_WRAPPER,
        ), 
        class_name=PAGE,
    )


app = rx.App()
app.add_page(index)
