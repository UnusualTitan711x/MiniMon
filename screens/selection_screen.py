from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer, Label, Input
from textual.containers import Center

class SelectionScreen(Screen):
    """ Screen where the player will input their name and the minimons they will use. """

    def compose(self):
        yield Label("Player name")
        yield Input(placeholder="Enter your name", id="name_input")
        yield Button("Submit", id="submit")

    def on_button_pressef(self, event:Button.Pressed):
        button_id = event.button.id

        if button_id == "submit":
            name_result = self.query_one("#name-input").value
            self.app.game.player.name