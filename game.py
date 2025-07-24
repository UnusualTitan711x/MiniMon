from textual.app import App
from textual.widgets import Button, Header, Footer

class EndRunGame(App):
    def compose(self):
        """ The widgets that this app is composed of """

        self.ansi_theme_dark = False

        yield Header(show_clock=True)
        yield Footer()
        yield Button("Play")
        yield Button("Quit")
    pass

if __name__ == "__main__":
    EndRunGame().run()