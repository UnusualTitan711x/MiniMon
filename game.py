from textual.app import App
from textual.widgets import Button, Header, Footer

class EndRunGame(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]
    
    def compose(self):
        """ The widgets that this app is composed of """
        
        yield Header(show_clock=True)
        yield Footer()
        yield Button("Play")
        yield Button("Quit")
    
    # Action method here
    # Should always start with the word "action"
    def action_toggle_dark_mode(self):
        self.theme = ("textual-light" if self.theme == "textual-dark" else "textual-dark")

if __name__ == "__main__":
    EndRunGame().run()