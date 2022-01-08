import gi
from BASE import MCTS, Node, Connect4

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Popup(Gtk.Dialog):
    def __init__(self, parent, winner):
        super().__init__(title="Game Over", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)
        self.set_border_width(10)
        label = Gtk.Label(label=f"{self.WinnerString(winner)}")

        box = self.get_content_area()
        box.add(label)
        self.show_all()
    
    def WinnerString(self, winner):
        if(winner == 1):
            return "You win! Yay... You're smart"
        elif(winner == 2):
            return "AI wins!... You're a loser"
        else:
            return "Draw! geegee"

class GameScreen(Gtk.Window):
    def __init__(self):
        self.game = Connect4(6,5)
        self.mcts = MCTS(self.game, 1000, 2)

        super().__init__(title="Connect4")
        self.set_border_width(30)

        grid = Gtk.Grid()
        grid.set_hexpand(False)
        grid.set_vexpand(True)
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        self.add(grid)

        
        gamestate = self.game.get_state_flipped()
        
    
        self.labels = []
        for i in range(len(gamestate)):
            innerlabels = []
            for j in range(len(gamestate[i])):
                label = Gtk.Label(label="")
                label.set_text(str(gamestate[i][j]))
                label.set_markup(
                    f"<big><big><big>{label.get_text()}</big></big></big>"
                )
                label.set_line_wrap(True)
                grid.attach(label, j, i, 1, 1)
                innerlabels.append(label)
            self.labels.append(innerlabels)
        

        self.button0 = Gtk.Button(label="Column 0")
        self.button0.connect("clicked", self.on_button_clicked0)
        grid.attach(self.button0, 0, 6, 1, 1)

        self.button1 = Gtk.Button(label="Column 1")
        self.button1.connect("clicked", self.on_button_clicked1)
        grid.attach(self.button1, 1, 6, 1, 1)

        self.button2 = Gtk.Button(label="Column 2")
        self.button2.connect("clicked", self.on_button_clicked2)
        grid.attach(self.button2, 2, 6, 1, 1)

        self.button3 = Gtk.Button(label="Column 3")
        self.button3.connect("clicked", self.on_button_clicked3)
        grid.attach(self.button3, 3, 6, 1, 1)

        self.button4 = Gtk.Button(label="Column 4")
        self.button4.connect("clicked", self.on_button_clicked4)
        grid.attach(self.button4, 4, 6, 1, 1)

    def on_button_clicked0(self, widget):
        self.game.playMove(0, 1)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 1)[0]:
            dialog = Popup(self, 1)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        self.game.playMove(self.mcts.bestMove(self.game.state, 2), 2)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 2)[0]:
            dialog = Popup(self, 2)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
    
    def on_button_clicked1(self, widget):
        self.game.playMove(1, 1)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 1)[0]:
            dialog = Popup(self, 1)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        self.game.playMove(self.mcts.bestMove(self.game.state, 2), 2)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 2)[0]:
            dialog = Popup(self, 2)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
    
    def on_button_clicked2(self, widget):
        self.game.playMove(2, 1)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 1)[0]:
            dialog = Popup(self, 1)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        self.game.playMove(self.mcts.bestMove(self.game.state, 2), 2)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 2)[0]:
            dialog = Popup(self, 2)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
    
    def on_button_clicked3(self, widget):
        self.game.playMove(3, 1)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 1)[0]:
            dialog = Popup(self, 1)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        self.game.playMove(self.mcts.bestMove(self.game.state, 2), 2)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 2)[0]:
            dialog = Popup(self, 2)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
    
    def on_button_clicked4(self, widget):
        self.game.playMove(4, 1)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 1)[0]:
            dialog = Popup(self, 1)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        self.game.playMove(self.mcts.bestMove(self.game.state, 2), 2)
        self.update_board()
        if self.game.checkDraw(self.game.get_state()):
            dialog = Popup(self, 0)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
        if self.game.checkTerminalState(self.game.get_state(), 2)[0]:
            dialog = Popup(self, 2)
            response = dialog.run()
            dialog.destroy()
            self.newGame()
    
    def update_board(self):
        gamestate = self.game.get_state_flipped()
        for i in range(len(gamestate)):
            for j in range(len(gamestate[i])):
                self.labels[i][j].set_text(str(gamestate[i][j]))
                self.labels[i][j].set_markup(
                    f"<big><big><big>{self.labels[i][j].get_text()}</big></big></big>"
                )

    
    def newGame(self):
        self.game = Connect4(6,5)
        self.mcts = MCTS(self.game, 1000, 2)
        self.update_board()




window = GameScreen()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()