from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer, Label, Input
from textual.containers import Center
from models.example_minimons import ex_minimons
import copy
from utils.data_loader import all_minimons

class MinimonCard(Button):
    """ Card showing the minimon you can choose """

class SelectionScreen(Screen):
    """ Screen where the player will input their name and the minimons they will use. """

    def compose(self):

        yield Label("Player Name", classes="center", id="name-label")

        with Center():
            yield Input(placeholder="Enter your name", id="name-input")

        with Center():
            yield Button("Submit", variant="primary", id="submit")

    def on_button_pressed(self, event:Button.Pressed):
        button_id = event.button.id

        if button_id == "submit":
            name_result = self.query_one("#name-input").value
            self.app.game.player.name = name_result
            self.query_one("#name-label").update(self.app.game.player.name)

            self.show_minimons()
    
    def show_minimons(self):
        minimons = all_minimons

        for m in minimons:
            data = f"""
Name: {m.name}
HP: {m.max_hp}
Attack: {m.attack}
Defense: {m.defense}
{m.image}
"""
            self.mount(Button(data)) 
