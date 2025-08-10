from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Vertical, Horizontal, Grid, Container
from screens.title_screen import TitleScreen
from screens.battle_screen import BattleScreen
from screens.selection_screen import SelectionScreen
from game import Game

# To switch easily between screens
# self.app.push_screen("screen_name") or
# self.app.switch_screen("screen_name")
        

class MiniMonGame(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]
    
    CSS = """
Pair {
    layout: horizontal;
}

BattlePanel {
    align: center middle;
    dock: bottom;
    background: $boost;
    min-width: 100;
    height: 30%;
    padding: 1 1;
}

TitleScreen, SelectionScreen {
    align: center middle;
    content-align: center middle;
    width: 100%;
}

#welcome-message {
    text-style: bold;
    align: center middle;
    text-align: center;
    width: 100%;
}

.center {
    align: center middle;
    text-align: center;
    width: 100%;
}

#name-input {
    align: center middle;
    text-align: center;
    width: 40%;
}

#submit {
    width: 3;
}

#start-button {
    margin: 1 1;
}

#action-grid {
    grid-size: 2;
    grid-gutter: 1 1;
    width: 40%;
    height: auto;
    content-align: center top;
    
    dock: right;
}

#minimon-grid {
    grid-size: 5;
    width: 90%;
    height: auto;
    content-align: center top;
    align: center middle;
}

#move-grid {
    grid-size: 2;
    grid-gutter: 1 1;
    width: 40%;
    height: auto;
    content-align: center top;
    dock: left;
}

#battle-log-scroll {
    height: 5;
    content-align: center bottom;
}

#prompt{
    dock: left;
    width: 60%;
}

.hidden{
    display: none;
}
"""

    def __init__(self):
        super().__init__()
        self.game = Game()
    
    def compose(self):
        """ The widgets that this app is composed of """
        
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self):
        self.install_screen(TitleScreen(), name="title")
        self.install_screen(BattleScreen(), name="battle")
        self.install_screen(SelectionScreen(), name="select")

        self.push_screen("title")

    
    # Action method here
    # Should always start with the word "action"
    def action_toggle_dark_mode(self):
        self.theme = ("textual-light" if self.theme == "textual-dark" else "textual-dark")
    