from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Grid, Container

class BattlePanel(Container):
    """ A container for the battle panel with buttons for actions """

    def compose(self):
        yield Static("Descriptions here: What should ... do?", id="prompt")

        yield Grid(
            Button("FIGHT"),
            Button("BAG"),
            Button("MINIMON"),
            Button("RUN"),
            id="move-grid"
        )

class BattleScreen(Screen):
    """ Here stays the options and descriptions of stuff """

    def compose(self):
            yield Header(show_clock=True)

            yield BattlePanel()

            yield Footer()
