import reflex as rx
import random

def _random_hex() -> str:
    """Generates a random hex color code."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

class ColorState(rx.State):
    """State for managing colors in the app."""

    current_colors: list[str] = [_random_hex() for _ in range(5)]  # Initialize with 5 random colors
    active_palette_id: int = -1  # No active palette initially

    @rx.var
    def color_count(self) -> int:
        """Returns the number of colors in the current palette."""
        return len(self.current_colors)

    @rx.var
    def can_remove_color(self) -> bool:
        """Returns True if there are colors to remove."""
        return len(self.current_colors) > 3
    
    @rx.var
    def all_colors_text(self) -> str:
        """Returns a string with all colors."""
        return ", ".join(self.current_colors)
    
    @rx.event
    def generate_random_palette(self):
        """Generates a new random palette of colors."""
        self.current_colors = [_random_hex() for _ in range(5)]
        self.active_palette_id = -1  # Reset active palette when generating a new one

    @rx.event
    def add_color(self):
        """Adds a new random color to the palette."""
        self.current_colors = self.current_colors + [_random_hex()]

    @rx.event
    def remove_color(self, index: int):
        """Removes a color from the palette by index."""
        if len(self.current_colors) > 3:
            colors = list(self.current_colors)
            colors.pop(index)
            self.current_colors = colors

    @rx.event
    def notify_copied_all(self):
        """Notifies that all colors have been copied."""
        # This method can be used to trigger a notification in the UI
        return rx.toast.success(f"Copiados: {self.all_colors_text}", duration=3000)
    
    