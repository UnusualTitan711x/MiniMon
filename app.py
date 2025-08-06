from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Vertical, Horizontal, Grid, Container
from screens.title_screen import TitleScreen
from screens.battle_screen import BattleScreen

# To switch easily between screens
# self.app.push_screen("screen_name") or
# self.app.switch_screen("screen_name")
        

class MiniMonGame(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]
    
    CSS_PATH = "style.css"
    
    def compose(self):
        """ The widgets that this app is composed of """
        
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self):
        self.install_screen(TitleScreen(), name="title")
        self.install_screen(BattleScreen(), name="battle")

        self.push_screen("title")

    
    # Action method here
    # Should always start with the word "action"
    def action_toggle_dark_mode(self):
        self.theme = ("textual-light" if self.theme == "textual-dark" else "textual-dark")
    