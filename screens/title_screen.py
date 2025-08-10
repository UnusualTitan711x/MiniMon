from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer, Label
from textual.containers import Center

class TitleScreen(Screen):
    """ Title Screen for the MiniMon Game """
    

    def compose(self):
        yield Label("Welcome to MiniMon", id="welcome-message")
        yield Static("Press START to play", id="start-instruction")

        with Center():
            yield Button("Start", variant="success", id="start-button")

        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "start-button":
            self.app.push_screen("battle")
