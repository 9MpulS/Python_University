import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master, rows, columns, num_mines):
        # Ініціалізація класу Minesweeper з параметрами гри
        self.master = master
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines
        self.remaining_cells = rows * columns - num_mines

        # Ініціалізація поля гри, кнопок та інших змінних
        self.minefield = [[0] * columns for _ in range(rows)]
        self.hidden_buttons = [[None] * columns for _ in range(rows)]
        self.flagged_cells = set()

        # Генерація мін та їхнього оточення
        self.create_minefield()

        # Відображення таймера
        self.timer_label = tk.Label(self.master, text="Час: 0 с")
        self.timer_label.grid(row=self.rows, columnspan=self.columns)

        self.elapsed_time_s = 0
        self.elapsed_time_m = 0
        self.timer_running = False
        self.timer_id = None

        # Створення графічного інтерфейсу
        self.create_widgets()

    def create_minefield(self):
        # Генерація випадкового розташування мін та підрахунок сусідів
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

    def update_timer(self):
        # Оновлення та відображення гри
        if self.timer_running:
            self.elapsed_time_s += 1
            if self.elapsed_time_s == 60:
                self.elapsed_time_m += 1
                self.elapsed_time_s = 0
            if self.elapsed_time_m == 0:
                self.timer_label.config(text=f"Час: {self.elapsed_time_s}с")
            if self.elapsed_time_m >= 1:
                self.timer_label.config(text=f"Час: {self.elapsed_time_m}хв {self.elapsed_time_s}с")

            self.timer_id = self.master.after(1000, self.update_timer)

    def start_timer(self):
        # Запуск таймера
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        # Зупинка таймера
        if self.timer_running:
            self.timer_running = False
            if self.timer_id:
                self.master.after_cancel(self.timer_id)

    def create_widgets(self):
        # Створення меню та кнопок для гри
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        menubar.add_cascade(label="Пауза", command=self.toggle_pause)
        menubar.add_cascade(label="Перезапуск", command=self.reset_game)
        menubar.add_cascade(label="Допомога", command=self.show_rules)
        menubar.add_cascade(label="Вихід", command=self.master.destroy)

        for row in range(self.rows):
            for col in range(self.columns):
                # Створення кнопок для клітинок гри
                button = tk.Button(self.master, width=3, height=2, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.hidden_buttons[row][col] = button

                # Зв'язування правого кліку мишею з функцією
                button.bind("<Button-3>", lambda event, r=row, c=col: self.on_right_click(r, c))

        # Зв'язування клавіш з функціями
        self.master.bind("<space>", lambda event: self.toggle_pause())
        self.master.bind("<r>", lambda event: self.reset_game())
        self.master.bind("<e>", lambda event: self.show_rules())

    def toggle_pause(self):
        # Пауза або продовження гри
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()

    def reset_game(self):
        # Скидання гри та розпочаток нової
        for r in range(self.rows):
            for c in range(self.columns):
                self.hidden_buttons[r][c].config(text="", state=tk.NORMAL, relief=tk.RAISED, bg="SystemButtonFace")
        self.flagged_cells.clear()

        self.minefield = [[0] * self.columns for _ in range(self.rows)]
        self.remaining_cells = self.rows * self.columns - self.num_mines
        self.create_minefield()

        self.elapsed_time_s = 0
        self.stop_timer()

        self.timer_label.config(text="Час: 0с")

    def show_rules(self):
        # Виведення вікна з правилами гри
        self.stop_timer()

        rules_hotkeys = (
            "Правила гри 'Сапер':\n\n"
            "1. Гравець відкриває комірки, натискаючи на них лівою кнопкою миші.\n"
            "2. Якщо комірка містить міну, гра закінчується.\n"
            "3. Якщо комірка поруч із міною, вона показує кількість сусідніх мін.\n"
            "4. Гравець може помітити клітинки, де ймовірно є міна, правою кнопкою миші.\n"
            "5. Мета гри - відкрити всі комірки, крім тих, де є міни.\n\n"
            "Гарячі клавіші:\n\n"
            "Space Пауза/Продовжити гру\n"
            "R Перезапуск гри\n"
            "E Показати інформацію про гру"
        )

        try:
            messagebox.showinfo("Правила гри/ Гарячі клавіші", rules_hotkeys)

        except tk.TclError:
            pass

    def on_button_click(self, row, col):
        # Обробка кліку лівою кнопкою миші
        if not self.timer_running:
            self.start_timer()
        if self.minefield[row][col] == -1:
            for r in range(self.rows):
                for c in range(self.columns):
                    if self.minefield[r][c] == -1:
                        self.hidden_buttons[r][c].config(text="*", state=tk.DISABLED, relief=tk.SUNKEN, bg="lightgray")
            self.stop_timer()
            messagebox.showinfo("Game Over", f"Ти натрапив на міну! Гру завершено \nЧас гри: {self.elapsed_time_m}хв {self.elapsed_time_s}с")
            self.reset_game()
        else:
            self.reveal_cell(row, col)

    def on_right_click(self, row, col):
        # Обробка правого кліку мишею
        if self.hidden_buttons[row][col]['state'] == tk.NORMAL:
            if (row, col) in self.flagged_cells:
                self.hidden_buttons[row][col].config(text="", state=tk.NORMAL, relief=tk.RAISED, bg="SystemButtonFace")
                self.flagged_cells.remove((row, col))
            else:
                self.hidden_buttons[row][col].config(text="🚩", state=tk.NORMAL, relief=tk.RAISED, bg="SystemButtonFace")
                self.flagged_cells.add((row, col))

    def reveal_cell(self, row, col):
        # Рекурсивна функція для розгортання комірок
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
            messagebox.showinfo("Congratulations", f"Ти знайшов всі міни! Втаю \nЧас гри: {self.elapsed_time_m}хв {self.elapsed_time_s}с")
            self.master.destroy()

def main():
    # Запуск головної функції
    root = tk.Tk()
    root.title("Minesweeper")
    Minesweeper(root, rows=8, columns=8, num_mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
