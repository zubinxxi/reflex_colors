import reflex as rx
from datetime import datetime
import json
import sqlmodel

from .color_state import ColorState


class PaletteState(ColorState):
    """State for managing palettes in the app."""

    show_save_dialog: bool = False  # Flag to show/hide the save palette dialog
    
    