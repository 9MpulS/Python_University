import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, columns, num_mines):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines

        self.minefield = [[0] * columns for _ in range(rows)]
        self.hidden_buttons = [[None] * columns for _ in range(rows)]

        self.create_minefield()
        self.create_widgets()

    def create_minefield(self):
        # Place mines randomly
        mines = random.sample(range(self.rows * self.columns), self.num_mines)
        for mine in mines:
            row = mine // self.columns
            col = mine % self.columns
            self.minefield[row][col] = -1  # -1 represents a mine

        # Fill in the numbers around the mines
        for row in range(self.rows):
            for col in range(self.columns):
                if self.minefield[row][col] == -1:
                    continue

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < self.rows and 0 <= col + j < self.columns and self.minefield[row + i][col + j] == -1:
                            self.minefield[row][col] += 1

    def create_widgets(self):
        for row in range(self.rows):
            for col in range(self.columns):
                button = tk.Button(self.master, width=3, height=2, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.hidden_buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.minefield[row][col] == -1:
            self.reveal_mines()
            self.game_over()
        else:
            self.reveal_cell(row, col)

    def reveal_cell(self, row, col):
        if self.minefield[row][col] == 0:
            self.hidden_buttons[row][col].config(state=tk.DISABLED, relief=tk.SUNKEN)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < self.rows and 0 <= col + j < self.columns and \
                       self.minefield[row + i][col + j] != -1 and self.hidden_buttons[row + i][col + j]['state'] == tk.NORMAL:
                        self.reveal_cell(row + i, col + j)
        else:
            self.hidden_buttons[row][col].config(state=tk.DISABLED, relief=tk.SUNKEN)
            self.hidden_buttons[row][col].config(text=str(self.minefield[row][col]))

    def reveal_mines(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.minefield[row][col] == -1:
                    self.hidden_buttons[row][col].config(text="*", state=tk.DISABLED, relief=tk.SUNKEN)

    def game_over(self):
        tk.messagebox.showinfo("Game Over", "You hit a mine! Game over.")
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    minesweeper_game = Minesweeper(root, rows=8, columns=8, num_mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
