from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Grid, Container
from game import Game

class BattlePanel(Container):
    """ A container for the battle panel with buttons for actions """

    def compose(self):
        yield Static("Descriptions here: What should ... do?", id="prompt")

        yield Grid(
            Button("BITE", id="move-bite"),
            id="move-grid",
            classes="hidden"
        )

        yield Grid(
            Button("FIGHT", id="fight"),
            Button("BAG", id="bag"),
            Button("MINIMON", id="minimon"),
            #Button("RUN", id="run"),
            id="action-grid"
        )

    

class BattleScreen(Screen):
    """ Here stays the options and descriptions of stuff """

    def __init__(self):
        super().__init__()
        self.game = Game()

    def compose(self):
        yield Header(show_clock=True)

        yield Static("hello", id="battle-log")
        yield BattlePanel()

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == "fight":
            log_widget = self.query_one("#battle-log", Static)
            log_widget.update("tatakae")
            self.show_move_buttons()
    
    def show_move_buttons(self):
        """ Show the abailable moves you from the active Minimon that youcan choose from """

        state = self.game.get_state()
        moves = state["player"]["active"].moves

        move_grid = self.query_one("#move-grid", Grid)

        for move in moves:
            move_grid.mount(Button(move.name, id=f"move-{move.name.lower()}"))

        if move_grid.has_class("hidden"):
            move_grid.remove_class("hidden") 
        
        self.query_one("#fight", Button).disabled = True
        

