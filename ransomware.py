import tkinter as tk
from tkinter import scrolledtext
import random
import platform

PASSWORD = "Mypass1234@"

root = tk.Tk()
root.title("SYSTEM ENCRYPTION")

# Fullscreen
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="black")

# Disable close button
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Main frame
main = tk.Frame(root, bg="black")
main.pack(expand=True)

# Header
tk.Label(
    main,
    text="⚠ CRITICAL SYSTEM BREACH DETECTED ⚠",
    font=("Consolas", 22, "bold"),
    fg="red",
    bg="black"
).pack(pady=10)

tk.Label(
    main,
    text=f"Device: {platform.node()} | OS: {platform.system()}",
    font=("Consolas", 12),
    fg="orange",
    bg="black"
).pack()

# Log box
log = scrolledtext.ScrolledText(
    main,
    width=80,
    height=18,
    bg="black",
    fg="lime",
    font=("Consolas", 10)
)
log.pack(pady=15)

# Progress
progress_label = tk.Label(
    main,
    text="Initializing...",
    font=("Consolas", 14, "bold"),
    fg="red",
    bg="black"
)
progress_label.pack()

progress_canvas = tk.Canvas(
    main,
    width=600,
    height=25,
    bg="#222",
    highlightthickness=0
)
progress_canvas.pack(pady=10)

progress_fill = progress_canvas.create_rectangle(
    0, 0, 0, 25,
    fill="red"
)

# Password area
input_frame = tk.Frame(main, bg="black")

tk.Label(
    input_frame,
    text="PASSWORD:",
    fg="white",
    bg="black",
    font=("Consolas", 12)
).pack(side="left", padx=5)

password_entry = tk.Entry(
    input_frame,
    show="*",
    font=("Consolas", 14),
    width=20
)
password_entry.pack(side="left", padx=5)

# Fake files
fake_files = [
    "Documents/report.docx",
    "Desktop/passwords.txt",
    "Photos/family.jpg",
    "Banking/accounts.xlsx",
    "Downloads/resume.pdf",
    "Work/project.zip"
]

progress = 0

def unlock():
    if password_entry.get() == PASSWORD:
        log.insert(tk.END, "\nACCESS GRANTED\n")
        log.insert(tk.END, "Prank complete.\n")
        root.after(2000, root.destroy)
    else:
        log.insert(tk.END, "\nWRONG PASSWORD\n")
        password_entry.delete(0, tk.END)

unlock_btn = tk.Button(
    input_frame,
    text="UNLOCK",
    command=unlock
)
unlock_btn.pack(side="left", padx=5)

password_entry.bind("<Return>", lambda e: unlock())

def update():
    global progress

    if progress < 100:
        file = random.choice(fake_files)

        log.insert(
            tk.END,
            f"Encrypting {file}...\n"
        )
        log.see(tk.END)

        progress += random.randint(2, 5)

        if progress > 100:
            progress = 100

        width = 600 * progress / 100

        progress_canvas.coords(
            progress_fill,
            0, 0,
            width, 25
        )

        progress_label.config(
            text=f"{progress}% COMPLETE"
        )

        root.after(150, update)

    else:
        progress_label.config(
            text="SYSTEM LOCKED"
        )

        log.insert(
            tk.END,
            "\nEnter password to restore access.\n"
        )

        input_frame.pack(pady=20)

        root.after(
            100,
            lambda: password_entry.focus_force()
        )

# Start
root.after(500, update)

root.mainloop()