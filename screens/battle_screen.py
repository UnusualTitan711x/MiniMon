from textual.widgets import Button, Header, Footer, Static, ProgressBar
from textual import work
from textual.screen import Screen
from textual.containers import Grid, Container, Horizontal, ScrollableContainer, VerticalScroll
from textual.reactive import reactive
from models.minimon import MiniMon
from game import Game
import time
import random
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
    
        

class TrainerDisplay(Container):
    """ The panel that contains the information about the MiniMon """

    def __init__(self, minimon:MiniMon, owner:str=None, trainer_name:str=None):
        super().__init__()
        self.minimon = minimon
        self.owner = owner
        self.trainer_name = trainer_name
    
    def compose(self):
        yield Static("", id="t-name")
        yield Static("", id="name")
        yield Static("", id="hp")
        yield Static("", id="status")
        yield ProgressBar(total=self.minimon.max_hp, show_eta=False, show_percentage=False, id="hp-bar")
        ascii_art = "ascii art comes here"
        yield Static(ascii_art, id="image")
    
    def on_mount(self, event):
        self.update_from_minimon()
    
    def update_from_minimon(self):
        if self.owner == "player":
            self.minimon = self.app.game.player.get_active_minimon()
        elif self.owner == "opponent":
            self.minimon = self.app.game.opponent.get_active_minimon()
        
        self.get_child_by_id("t-name").update(self.trainer_name.capitalize())
        self.get_child_by_id("name").update(self.minimon.name)
        self.get_child_by_id("status").update(f"Satus: {self.minimon.status}")
        self.get_child_by_id("hp").update(f"HP: {self.minimon.current_hp}/{self.minimon.max_hp}")
        self.query_one("#hp-bar").update(progress=self.minimon.current_hp, total=self.minimon.max_hp)
        self.get_child_by_id("image").update(self.minimon.image)

class BattleScreen(Screen):
    """ Here stays the options and descriptions of stuff """

    def __init__(self):
        super().__init__()

    def compose(self):
        yield Header(show_clock=True)

        yield Horizontal(
            TrainerDisplay(self.app.game.player.get_active_minimon(), owner="player", trainer_name=self.app.game.player.name),
            TrainerDisplay(self.app.game.opponent.get_active_minimon(), owner="opponent", trainer_name=self.app.game.opponent.name)
        )

        with VerticalScroll(id="battle-log-scroll"):
            yield Static("", id="battle-log")

        yield BattlePanel()
        

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

            if random.randint(0,1) == 0:
                self.app.game.turn = "player"
            self.app.game.opponent_turn()
            self.refresh_ui()
        elif button_id == "bag":
            self.refresh_ui()
            self.show_bag_buttons()
        elif button_id.startswith("use-"):
            index = int(button_id.split("-")[1])
            self.app.game.player.items[index].use(self.app.game.player.get_active_minimon())
            self.app.game.battle_log.append(f"{self.app.game.player.name} used {self.app.game.player.items[index].name} on {self.app.game.player.get_active_minimon().name}")
            del self.app.game.player.items[index]
            
            self.app.game.turn = "opponent"
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

    def show_bag_buttons(self):
        """ Show the available moves you from the active Minimon that you can choose from """

        items = self.app.game.player.items

        move_grid = self.query_one("#move-grid", Grid)
        move_grid.remove_children()

        if items == []:
            self.query_one("#prompt").update("No item left")
            self.query_one("#bag", Button).disabled = True
            return
        
        for i, m in enumerate(items):
            move_grid.mount(Button(m.name, id=f"use-{i}"))

        if move_grid.has_class("hidden"):
            move_grid.remove_class("hidden") 
        
        self.query_one("#bag", Button).disabled = True

    def update_log(self):
        state = self.app.game.get_state()
        
        log_widget = self.query_one("#battle-log", Static)

        log_widget.update("\n".join(state["log"]))
        log_widget.call_after_refresh(self.scroll_to_bottom)

    def scroll_to_bottom(self):
        s_container = self.query_one("#battle-log-scroll", VerticalScroll)
        s_container.scroll_end(animate=False)
        

    def refresh_ui(self):
        

        self.query(TrainerDisplay)[0].update_from_minimon()
        self.query(TrainerDisplay)[1].update_from_minimon()

        self.update_log()

        move_grid = self.query_one("#move-grid", Grid)
        move_grid.remove_children()

        if self.app.game.player.get_active_minimon().is_fainted():
            self.query_one("#fight", Button).disabled = True

            self.query(TrainerDisplay)[0].update_from_minimon()
            self.query(TrainerDisplay)[1].update_from_minimon()
        else:
            self.query_one("#fight", Button).disabled = False
        self.query_one("#minimon", Button).disabled = False
        self.query_one("#bag", Button).disabled = False

        if self.app.game.opponent.get_active_minimon().is_fainted():
            message = self.app.game.opponent.auto_switch_minimon()
            if message: self.app.game.battle_log.append(message)

            self.query(TrainerDisplay)[0].update_from_minimon()
            self.query(TrainerDisplay)[1].update_from_minimon()

        move_grid = self.query_one("#move-grid", Grid)

        if not move_grid.has_class("hidden"):
            move_grid.add_class("hidden") 
        
        if self.app.game.result == "win" or self.app.game.result == "lose":
                self.query_one("#action-grid", Grid).add_class("hidden")
                self.query_one("#prompt", Static).update(f"You {self.app.game.result}.")
        



