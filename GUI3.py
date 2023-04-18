import tkinter as tk
from tkinter import messagebox
from TicTacToe import TicTacToe


class TicTacToeGUI:
    BOARD_SIZE = 3
    FONT_FAMILY = "Arial"
    FONT_SIZE_LARGE = 24
    FONT_SIZE_MEDIUM = 16
    BUTTON_WIDTH = 5
    BUTTON_HEIGHT = 2

    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.board_frame = tk.Frame(master)
        self.board_frame.pack()

        self.board_buttons = [[None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                button = tk.Button(self.board_frame, text=" ", font=(self.FONT_FAMILY, self.FONT_SIZE_LARGE),
                                   width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT,
                                   command=lambda row=row, col=col: self._button_click(row, col))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.board_buttons[row][col] = button

        self.reset_button = tk.Button(master, text="Reset", font=(self.FONT_FAMILY, self.FONT_SIZE_MEDIUM),
                                      width=10, command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.status_label = tk.Label(master, text="Player X's turn", font=(self.FONT_FAMILY, self.FONT_SIZE_MEDIUM))
        self.status_label.pack(pady=10)

        self.game = TicTacToe()
        self.game.scores = {player: 0 for player in self.game.players}

        menubar = tk.Menu(master)
        master.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Game", command=self.reset_game)
        filemenu.add_command(label="Quit", command=master.quit)

        gamemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=gamemenu)
        gamemenu.add_command(label="Show Scores", command=self._show_scores)

    def reset_game(self):
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self.board_buttons[row][col].config(text=" ", state="normal")
        self.status_label.config(text="Player X's turn")
        self.reset_button.config(state="disabled")
        self.game.reset_game_state()

    def _button_click(self, row, col):
        try:
            if self.game.make_move(row, col):
                self.board_buttons[row][col].config(text=self.game.players[self.game.current_player])
                winner = self.game.check_win()
                if winner:
                    self._game_over(winner)
                elif self.game.is_game_over():
                    self._game_over(None)
                else:
                    self.game.current_player = (self.game.current_player + 1) % len(self.game.players)
                    self._update_status_label()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _update_status_label(self):
        self.status_label.config(text="Player {}'s turn".format(self.game.players[self.game.current_player]))

    def _game_over(self, winner):
        if winner:
            self.status_label.config(text="Player {} wins!".format(winner))
        else:
            self.status_label.config(text="It's a draw!")
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                self.board_buttons[row][col].config(state="disabled")
        self.reset_button.config(state="normal")
        self.game.update_scores(winner)

    def _show_scores(self):
        scores_str = "Scores:\n"
        for player, score in self.game.scores.items():
            scores_str += "{}: {}\n".format(player, score)
        messagebox.showinfo("Scores", scores_str)

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()