import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master, rows, columns, num_mines):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines
        self.remaining_cells = rows * columns - num_mines

        self.minefield = [[0] * columns for _ in range(rows)]
        self.hidden_buttons = [[None] * columns for _ in range(rows)]
        self.flagged_cells = set()

        self.create_minefield()
        self.create_widgets()

    def create_minefield(self):
        mines = random.sample(range(self.rows * self.columns), self.num_mines)
        for mine in mines:
            row = mine // self.columns
            col = mine % self.columns
            self.minefield[row][col] = -1

        for row in range(self.rows):
            for col in range(self.columns):
                if self.minefield[row][col] == -1:
                    continue

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < self.rows and 0 <= col + j < self.columns and self.minefield[row + i][col + j] == -1:
                            self.minefield[row][col] += 1

    def create_widgets(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        menubar.add_cascade(label="Допомога", command=self.show_rules)
        menubar.add_cascade(label="Перезапуск", command=self.restart_game)
        menubar.add_cascade(label="Вихід", command=self.master.destroy)

        for row in range(self.rows):
            for col in range(self.columns):
                button = tk.Button(self.master, width=3, height=2, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.hidden_buttons[row][col] = button

                button.bind("<Button-3>", lambda event, r=row, c=col: self.on_right_click(event, r, c))

    def reset_game(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.hidden_buttons[row][col].config(text="", state=tk.NORMAL, relief=tk.RAISED, bg="SystemButtonFace")
        self.flagged_cells.clear()
        self.remaining_cells = self.rows * self.columns - self.num_mines
        self.create_minefield()

    def show_rules(self):
        rules = (
            "Правила гри 'Сапер':\n\n"
            "1. Гравець відкриває комірки, натискаючи на них лівою кнопкою миші.\n"
            "2. Якщо комірка містить міну, гра закінчується.\n"
            "3. Якщо комірка поруч із міною, вона показує кількість сусідніх мін.\n"
            "4. Гравець може помітити клітинки, де ймовірно є міна, правою кнопкою миші.\n"
            "5. Мета гри - відкрити всі комірки, крім тих, де є міни."
        )
        messagebox.showinfo("Правила гри", rules)

    def restart_game(self):
        self.reset_game()

    def on_button_click(self, row, col):
        if self.minefield[row][col] == -1:
            self.reveal_mines()
            self.game_over()
        else:
            self.reveal_cell(row, col)

    def on_right_click(self, event, row, col):
        if (row, col) in self.flagged_cells:
            self.hidden_buttons[row][col].config(text="", state=tk.NORMAL, relief=tk.RAISED, bg="SystemButtonFace")
            self.flagged_cells.remove((row, col))
        else:
            self.hidden_buttons[row][col].config(text="Х", state=tk.DISABLED, relief=tk.SUNKEN, bg="SystemButtonFace")
            self.flagged_cells.add((row, col))

    def reveal_cell(self, row, col):
        if self.minefield[row][col] == 0:
            self.hidden_buttons[row][col].config(state=tk.DISABLED, relief=tk.SUNKEN, bg="lightgray")
            self.remaining_cells -= 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < self.rows and 0 <= col + j < self.columns and \
                       self.minefield[row + i][col + j] != -1 and self.hidden_buttons[row + i][col + j]['state'] == tk.NORMAL:
                        self.reveal_cell(row + i, col + j)
        else:
            self.hidden_buttons[row][col].config(state=tk.DISABLED, relief=tk.SUNKEN, bg="lightgray")
            self.hidden_buttons[row][col].config(text=str(self.minefield[row][col]))
            self.remaining_cells -= 1

        if self.remaining_cells == 0:
            messagebox.showinfo("Congratulations", "You've won the game!")
            self.master.destroy()

    def reveal_mines(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.minefield[row][col] == -1:
                    self.hidden_buttons[row][col].config(text="*", state=tk.DISABLED, relief=tk.SUNKEN, bg="lightgray")

    def game_over(self):
        messagebox.showinfo("Game Over", "You hit a mine! Game over.")
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    Minesweeper(root, rows=8, columns=8, num_mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()