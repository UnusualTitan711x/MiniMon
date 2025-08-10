from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer, Label, Input
from textual.containers import Center, Grid
from models.example_minimons import ex_minimons
import copy
from utils.data_loader import all_minimons

class MinimonCard(Button):
    """ Card showing the minimon you can choose """

class SelectionScreen(Screen):
    """ Screen where the player will input their name and the minimons they will use. """

    def compose(self):
        self.choices = 0

        yield Label("Player Name", classes="center", id="name-label")

        with Center():
            yield Input(placeholder="Enter your name", id="name-input")

        with Center():
            yield Button("Submit", variant="primary", id="submit")
        
        yield Grid(id="minimon-grid")

    def on_button_pressed(self, event:Button.Pressed):
        button_id = event.button.id

        if button_id == "submit":
            name_result = self.query_one("#name-input").value
            self.app.game.player.name = name_result
            self.query_one("#name-label").update("Choose 4 MiniMons to use in Battle")

            self.query_one("#submit").add_class("hidden")
            self.query_one("#name-input").add_class("hidden")

            self.show_minimons()
        if button_id.startswith("choose-"):
            index = int(button_id.split("-")[1])
            self.app.game.player.minimons.append(all_minimons[index])
            self.choices += 1
            self.query_one(f"#{button_id}").disabled = True
            if self.choices >= 4:
                self.app.push_screen("battle")
    
    def show_minimons(self):
        minimons = all_minimons

        minimon_grid = self.query_one("#minimon-grid", Grid)

        for i, m in enumerate(minimons):
            data = f"""
Name: {m.name}
HP: {m.max_hp}
Attack: {m.attack}
Defense: {m.defense}
{m.image}
"""
            minimon_grid.mount(Button(data, id=f"choose-{i}")) 
