import reflex as rx

from main.components.styles import (
    NAVBAR_WRAPPER,
    NAVBAR_INNER,
    NAVBAR_LOGO,
    NAVBAR_LOGO_ICON,
    NAVBAR_LOGO_TEXT,
    NAVBAR_ACTIONS,
    BTN_GHOST,
    BTN_PRIMARY
)

def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            #LOGO
            rx.box(
                rx.icon("palette", class_name=NAVBAR_LOGO_ICON, size=20),
                rx.text("Color Palette", class_name=NAVBAR_LOGO_TEXT),
                class_name=NAVBAR_LOGO,
            ),
            rx.box(class_name="flex-1"),

            #BOTONES
            rx.box(
                rx.button(
                    rx.icon("clipboard_copy", size=16),
                    "Copiar todos",
                    class_name=BTN_GHOST,
                ),
                rx.button(
                    rx.icon("bookmark", size=16),
                    "Guardar paleta",
                    class_name=BTN_PRIMARY,
                ),
                class_name=NAVBAR_ACTIONS,
            ),
            class_name=NAVBAR_INNER,
        ),
        class_name=NAVBAR_WRAPPER,
        style={
            "bacdrop_filter": "blur(20px)",
            "background": "rgba(255, 255, 255, 0.8)",
        },
    )