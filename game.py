from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Vertical, Horizontal, Grid, Container

class Word(Static):
    """ Just a word """

class Pair(Static):
    """ Just something here """
    
    def compose(self):
        yield Button("Button 1", variant="success")
        yield Button("Button 2", variant="error")
        yield Word("00:00:00.00")

class BattleScreen(Container):
    """ Here stays the options and descriptions of stuff """

    def compose(self):
            yield Static("Descriptions here: What should ... do?", id="prompt")

            yield Grid(
                Button("FIGHT"),
                Button("BAG"),
                Button("MINIMON"),
                Button("RUN"),
                id="move-grid"
            )
            
            #id="battle-panel"

            

class EndRunGame(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]
    
    CSS_PATH = "style.css"
    
    def compose(self):
        """ The widgets that this app is composed of """
        
        #self.push_screen(BattleScreen())
        
        yield Header(show_clock=True)
        yield Footer()

        yield BattleScreen()
        with ScrollableContainer(id="pairs"):
            yield Pair()
            yield Pair()
            yield Pair()

    
    # Action method here
    # Should always start with the word "action"
    def action_toggle_dark_mode(self):
        self.theme = ("textual-light" if self.theme == "textual-dark" else "textual-dark")
    


if __name__ == "__main__":
    EndRunGame().run()