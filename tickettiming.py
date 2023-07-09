import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip
from PIL import Image, ImageTk

def create_ticket_timing_limit_tab(parent):
    def copy_to_clipboard(record):
        record = "TKTL"
        pyperclip.copy(record)
        messagebox.showinfo("Success", "Copied to clipboard!")
    
    def copy_to_clipboard_2(record):
        record = "RF TUAN; ER"
        pyperclip.copy(record)
        messagebox.showinfo("Success", "Copied to clipboard!")

    def copy_to_clipboard_3(record):
        record = "IEPJ-EML-hnnholidays@gmail.com"
        pyperclip.copy(record)
        messagebox.showinfo("Success", "Copied to clipboard!")

    title_label = tk.Label(parent, text="1. Ticket Timing Limit", font=("Arial", 8, "bold"))
    title_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")

    tktl_button = tk.Button(parent, text="Click to copy code", command=lambda: copy_to_clipboard(tktl_button.cget("text")))
    tktl_button.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    title_label = tk.Label(parent, text="2. Use Smart flow to assign agent", font=("Arial", 8, "bold"))
    title_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")

    title_label = tk.Label(parent, text="3. Receive From", font=("Arial", 8, "bold"))
    title_label.grid(row=2, column=0, padx=5, pady=10, sticky="w")

    tktl_button = tk.Button(parent, text="Click to copy code", command=lambda: copy_to_clipboard_2(tktl_button.cget("text")))
    tktl_button.grid(row=2, column=1, padx=5, pady=10, sticky="w")

    title_label = tk.Label(parent, text="4. Use Your Smart Flow => SSR CONTACT DETAILS", font=("Arial", 8, "bold"))
    title_label.grid(row=3, column=0, padx=5, pady=10, sticky="w")

    title_label = tk.Label(parent, text="5. Save Infor and Send Email", font=("Arial", 8, "bold"))
    title_label.grid(row=4, column=0, padx=5, pady=10, sticky="w")

    tktl_button = tk.Button(parent, text="Click to copy code", command=lambda: copy_to_clipboard_3(tktl_button.cget("text")))
    tktl_button.grid(row=4, column=1, padx=5, pady=10, sticky="w")
