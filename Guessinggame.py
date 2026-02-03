import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < number:
            result_label.config(text="Too Low! Try again.", fg="blue")
        elif guess > number:
            result_label.config(text="Too High! Try again.", fg="orange")
        else:
            messagebox.showinfo(
                "Congratulations 🎉",
                f"You guessed the number correctly!\nTotal attempts: {attempts}"
            )
            root.destroy()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Main window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("350x250")
root.resizable(False, False)

# Title
tk.Label(root, text="🎯 Guessing Game", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Guess a number between 1 and 100").pack()

# Entry
entry_guess = tk.Entry(root, font=("Arial", 12))
entry_guess.pack(pady=10)

# Button
tk.Button(root, text="Check Guess", command=check_guess, width=15).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
