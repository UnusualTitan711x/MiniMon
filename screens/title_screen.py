from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer

class TitleScreen(Screen):
    """ Title Screen for the MiniMon Game """

    def compose(self):
        yield Static("Welcome to MiniMon")
        yield Static("Press START to play")
        yield Button("Start", variant="success", id="start-button")

        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "start-button":
            self.app.push_screen("battle")
