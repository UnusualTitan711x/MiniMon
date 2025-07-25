from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static

class Word(Static):
    """ Just a word """

class Pair(Static):
    """ Just something here """
    
    def compose(self):
        yield Button("Button 1", variant="success")
        yield Button("Button 2", variant="error")
        yield Word("Part")


class EndRunGame(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]
    
    CSS = """
    Pair{
        layout: horizontal;
    }
    """

    def compose(self):
        """ The widgets that this app is composed of """
        
        yield Header(show_clock=True)
        yield Footer()

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