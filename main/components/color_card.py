import reflex as rx
from main.state.palette_state import PaletteState
from .styles import (
    COLOR_CARD,
    COLOR_CARD_ACTIONS,
    COLOR_CARD_BTN,
    COLOR_CARD_FOOTER,
    COLOR_CARD_HEX_CHIP,
    COLOR_CARD_HEX_TEXT,
    COLOR_CARD_REMOVE_BTN,
    COLOR_CARD_WRAPPER,
)

def _color_card(color: str, int: int) -> rx.Component:
    """Component to display a color card with actions.

    Args:
        color (str): The color value in hex format.
        palette_state (PaletteState): The state managing the palette.

    Returns:
        rx.Component: The color card component.
    """
    return rx.box(
        rx.box(
            rx.box(
                rx.text(color, class_name=COLOR_CARD_HEX_TEXT),
                class_name=COLOR_CARD_HEX_CHIP,
            ),

            #ICONO
            rx.box(
                rx.icon_button(
                    rx.icon("copy", size=16, size=24),
                    on_click=rx.set_clipboard(color),
                    variant="ghost",
                    class_name=COLOR_CARD_BTN,
                ),
                class_name=COLOR_CARD_ACTIONS,
            ),
            class_name=COLOR_CARD_FOOTER,
        ),

        style={"background_color": color},
        class_name=COLOR_CARD,
    )


def color_card_with_remove(color: str, index: int) -> rx.Component:
    """Component to display a color card with a remove button.

    Args:
        color (str): The color value in hex format.
        index (int): The index of the color in the palette.

    Returns:
        rx.Component: The color card component with a remove button.
    """
    return rx.box(
        _color_card(color, index),
        rx.cond(
            PaletteState.can_remove_color,
            rx.button(
                rx.icon("trash", size=12),
                "Eliminar",
                on_click=PaletteState.remove_color(index),
                class_name=COLOR_CARD_REMOVE_BTN,   
            ),  
            rx.box(height="28px"),  # Placeholder to maintain layout when the button is not shown  
         ),
        
        class_name=COLOR_CARD_WRAPPER,
    )