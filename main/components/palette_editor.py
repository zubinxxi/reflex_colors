import reflex as rx
from main.state.palette_state import PaletteState
from .color_card import color_card_with_remove
from .styles import (
    CARD,
    BTN_BASE,
    BTN_PRIMARY,
    BTN_SUCCESS,
    BTN_GHOST,
    EDITOR_HEADER,
    EDITOR_SUBTITLE,
    EDITOR_TITLE,
    DIALOG_ACTIONS,
    DIALOG_CONTENT,
    DIALOG_DESC,
    DIALOG_INNER,
    DIALOG_TITLE,
    DIALOG_INPUT,

)

def palette_editor() -> rx.Component:
    return rx.box(
        # Ventanas modales de guardar y editar paletas
        rx.box(
            rx.box(
                rx.text("Paleta actual", class_name=EDITOR_TITLE),
                rx.text(
                    PaletteState.color_count.to_string() + " colores",
                    class_name=EDITOR_SUBTITLE,
                ),
                class_name="flex flex-col",
            ),

            rx.box(class_name="flex-1",),
            rx.box(
                rx.button(
                    rx.icon("shuffle", size=16),
                    "Aleatoria",
                    on_click=PaletteState.generate_random_palette(),
                    class_name=BTN_GHOST,
                ),
                rx.button(
                    rx.icon("plus", size=16),
                    "Agregar",
                    on_click=PaletteState.add_color(),
                    class_name=BTN_SUCCESS,
                ),
                class_name="flex items-center gap-2",
            ),
            class_name=EDITOR_HEADER,
        ),
        rx.box(
            rx.grid(
                rx.foreach(
                    PaletteState.current_colors,
                    lambda color, i: color_card_with_remove(color, i),
                ),
                columns="5",
                spacing="3",
                width="100%",
            ),
        ),
        class_name=CARD,
    )