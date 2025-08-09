from textual.widgets import Button, Header, Footer, Static
from textual.screen import Screen
from textual.containers import Grid, Container
from game import Game

class BattlePanel(Container):
    """ A container for the battle panel with buttons for actions """

    def compose(self):
        yield Static("What will you do?", id="prompt")

        yield Grid(
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

    def compose(self):
        yield Header(show_clock=True)

        yield Static("", id="battle-log")
        yield BattlePanel()

        # footer was here

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == "fight":
            self.refresh_ui()
            self.show_move_buttons()
        elif button_id.startswith("move-"):
            move_name = event.button.label
            result = self.app.game.player_turn(move_name)
            self.refresh_ui()

            if result != "win":
                self.app.game.opponent_turn()
                self.refresh_ui()
        elif button_id == "minimon":
            self.refresh_ui()
            self.show_minimon_buttons()
        elif button_id.startswith("switch-"):
            index = int(button_id.split("-")[1])
            message = self.app.game.player.switch_minimon(index)
            if message: self.app.game.battle_log.append(message)

            self.app.game.opponent_turn()
            self.refresh_ui()
    
    def show_move_buttons(self):
        """ Show the abailable moves you from the active Minimon that you can choose from """

        state = self.app.game.get_state()
        moves = state["player"]["active"].moves

        move_grid = self.query_one("#move-grid", Grid)

        move_grid.remove_children()
        
        for move in moves:
            move_grid.mount(Button(move.name, id=f"move-{move.name.lower()}"))

        if move_grid.has_class("hidden"):
            move_grid.remove_class("hidden") 
        
        self.query_one("#fight", Button).disabled = True
    
    def show_minimon_buttons(self):
        """ Show the available moves you from the active Minimon that you can choose from """

        minimons = self.app.game.player.minimons

        move_grid = self.query_one("#move-grid", Grid)
        move_grid.remove_children()
        
        for i, m in enumerate(minimons):
            move_grid.mount(Button(m.name, id=f"switch-{i}"))

            if self.app.game.player.active_index == i or self.app.game.player.minimons[i].is_fainted():
                self.query_one(f"#switch-{i}", Button).disabled = True

        if move_grid.has_class("hidden"):
            move_grid.remove_class("hidden") 
        
        self.query_one("#minimon", Button).disabled = True


    def refresh_ui(self):
        state = self.app.game.get_state()

        log_widget = self.query_one("#battle-log", Static)
        log_widget.update("\n".join(state["log"]))

        move_grid = self.query_one("#move-grid", Grid)
        move_grid.remove_children()

        if self.app.game.player.get_active_minimon().is_fainted():
            self.query_one("#fight", Button).disabled = True
        else:
            self.query_one("#fight", Button).disabled = False
        self.query_one("#minimon", Button).disabled = False

        if self.app.game.opponent.get_active_minimon().is_fainted():
            message = self.app.game.opponent.auto_switch_minimon()
            if message: self.app.game.battle_log.append(message)

        move_grid = self.query_one("#move-grid", Grid)

        if not move_grid.has_class("hidden"):
            move_grid.add_class("hidden") 
        
        if self.app.game.result == "win" or self.app.game.result == "lose":
                self.query_one("#action-grid", Grid).add_class("hidden")
                self.query_one("#prompt", Static).update(f"You {self.app.game.result}.")



