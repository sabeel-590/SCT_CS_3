import tkinter as tk
from tkinter import ttk
import re

# ----------------------------
# Password Strength Function
# ----------------------------

def check_password():

    password = password_entry.get()

    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    progress["value"] = score * 20

    if score <= 1:
        strength = "Very Weak"
        color = "#ef4444"

    elif score == 2:
        strength = "Weak"
        color = "#f97316"

    elif score == 3:
        strength = "Medium"
        color = "#facc15"

    elif score == 4:
        strength = "Strong"
        color = "#22c55e"

    else:
        strength = "Very Strong"
        color = "#16a34a"

    result_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    if feedback:
        suggestions.config(
            text="\n".join(feedback),
            fg="#d1d5db"
        )
    else:
        suggestions.config(
            text="Excellent Password Security!",
            fg="#22c55e"
        )


def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_btn.config(text="Show")


# ----------------------------
# Main Window
# ----------------------------

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("900x600")
root.configure(bg="#0f172a")

# Heading

title = tk.Label(
    root,
    text="PASSWORD STRENGTH CHECKER",
    bg="#0f172a",
    fg="white",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="SkillCraft Technology - Cyber Security Internship",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Arial", 14)
)
subtitle.pack()

# Frame

frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=40,
    pady=40
)
frame.pack(pady=40)

tk.Label(
    frame,
    text="Enter Password",
    bg="#1e293b",
    fg="white",
    font=("Arial", 16, "bold")
).pack(pady=10)

password_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 16),
    show="*"
)
password_entry.pack(pady=10)

show_btn = tk.Button(
    frame,
    text="Show",
    command=toggle_password,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold")
)
show_btn.pack(pady=5)

check_btn = tk.Button(
    frame,
    text="Check Strength",
    command=check_password,
    bg="#22c55e",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20
)
check_btn.pack(pady=20)

progress = ttk.Progressbar(
    frame,
    length=400,
    mode="determinate"
)
progress.pack(pady=10)

result_label = tk.Label(
    frame,
    text="",
    bg="#1e293b",
    fg="white",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=10)

suggestions = tk.Label(
    frame,
    text="",
    bg="#1e293b",
    fg="#cbd5e1",
    font=("Arial", 12),
    justify="left"
)
suggestions.pack(pady=10)

root.mainloop()
