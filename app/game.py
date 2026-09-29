import random
import tkinter as tk
from tkinter import messagebox

from app.card import create_card, mark_number
from app.lines import get_lines


class NumberGameApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Number Game")
        self.root.geometry("700x700")
        self.root.resizable(False, False)

        self.player_card = create_card()
        self.computer_card = create_card()

        self.player_marked = [
            [False for _ in range(5)]
            for _ in range(5)
        ]

        self.computer_marked = [
            [False for _ in range(5)]
            for _ in range(5)
        ]

        self.called_numbers = []

        self.player_completed_lines = []
        self.computer_completed_lines = []

        self.create_app()

    def create_app(self):

        title = tk.Label(
            self.root,
            text="NUMBER GAME",
            font=("Arial", 28, "bold"),
            fg="blue"
        )

        title.pack(pady=20)

        self.status_label = tk.Label(
            self.root,
            text="Choose a number",
            font=("Arial", 16)
        )

        self.status_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)

        self.buttons_frame.pack(pady=20)

        self.number_buttons = []

        for number in range(1, 26):

            button = tk.Button(
                self.buttons_frame,
                text=str(number),
                width=6,
                height=2,
                font=("Arial", 12, "bold"),
                command=lambda n=number: self.select_number(n)
            )

            row = (number - 1) // 5
            column = (number - 1) % 5

            button.grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )

            self.number_buttons.append(button)

        self.result_label = tk.Label(
            self.root,
            text=(
                "Your completed lines: 0\n"
                "Computer completed lines: 0"
            ),
            font=("Arial", 14)
        )

        self.result_label.pack(pady=20)

        restart_button = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            padx=20,
            pady=10,
            command=self.restart_game
        )

        restart_button.pack(pady=10)

    def select_number(self, number):

        if number in self.called_numbers:

            messagebox.showwarning(
                "Already Selected",
                "This number has already been selected."
            )

            return

        self.called_numbers.append(number)

        mark_number(
            self.player_card,
            self.player_marked,
            number
        )

        current_lines = get_lines(
            self.player_marked
        )

        for line in current_lines:

            if line not in self.player_completed_lines:

                self.player_completed_lines.append(line)

        self.number_buttons[number - 1].config(
            state=tk.DISABLED,
            bg="lightgray"
        )

        self.update_display()

        if len(self.player_completed_lines) >= 5:

            messagebox.showinfo(
                "Game Over",
                "Congratulations!\n"
                "You completed 5 lines!"
            )

            self.disable_buttons()

            return

        self.status_label.config(
            text="Computer is choosing..."
        )

        self.root.after(
            500,
            self.computer_turn
        )

    def computer_turn(self):

        available_numbers = [
            number
            for number in range(1, 26)
            if number not in self.called_numbers
        ]

        if not available_numbers:
            return

        computer_number = random.choice(
            available_numbers
        )

        self.called_numbers.append(
            computer_number
        )

        mark_number(
            self.computer_card,
            self.computer_marked,
            computer_number
        )

        mark_number(
            self.player_card,
            self.player_marked,
            computer_number
        )

        current_lines = get_lines(
            self.computer_marked
        )

        for line in current_lines:

            if line not in self.computer_completed_lines:

                self.computer_completed_lines.append(
                    line
                )

        self.number_buttons[
            computer_number - 1
        ].config(
            state=tk.DISABLED,
            bg="lightgray"
        )

        self.update_display()

        if len(self.computer_completed_lines) >= 5:

            messagebox.showinfo(
                "Game Over",
                "Computer completed 5 lines!"
            )

            self.disable_buttons()

            return

        self.status_label.config(
            text="Your turn - choose a number"
        )

    def update_display(self):

        self.result_label.config(
            text=(
                f"Your completed lines: "
                f"{len(self.player_completed_lines)}\n"
                f"Computer completed lines: "
                f"{len(self.computer_completed_lines)}"
            )
        )

    def disable_buttons(self):

        for button in self.number_buttons:

            button.config(
                state=tk.DISABLED
            )

    def restart_game(self):

        self.player_card = create_card()
        self.computer_card = create_card()

        self.player_marked = [
            [False for _ in range(5)]
            for _ in range(5)
        ]

        self.computer_marked = [
            [False for _ in range(5)]
            for _ in range(5)
        ]

        self.called_numbers = []

        self.player_completed_lines = []
        self.computer_completed_lines = []

        for button in self.number_buttons:

            button.config(
                state=tk.NORMAL,
                bg="SystemButtonFace"
            )

        self.status_label.config(
            text="Choose a number"
        )

        self.update_display()
