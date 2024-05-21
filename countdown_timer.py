import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 12))
        self.time_label.pack()

        self.time_entry = tk.Entry(root, font=("Helvetica", 12))
        self.time_entry.pack()

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack()

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer, font=("Helvetica", 12))
        self.reset_button.pack()

        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.countdown_label.pack()

        self.remaining_time = 0

    def start_timer(self):
        try:
            self.remaining_time = int(self.time_entry.get())
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def update_timer(self):
        if self.remaining_time > 0:
            self.countdown_label.config(text=str(self.remaining_time))
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.countdown_label.config(text="Time's up!")
            messagebox.showinfo("Countdown Timer", "Time's up!")

    def reset_timer(self):
        self.remaining_time = 0
        self.countdown_label.config(text="")
        self.time_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.mainloop()