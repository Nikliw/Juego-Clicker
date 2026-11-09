import tkinter as tk
from pathlib import Path
import sys
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Juego Clicker")

score = 0

score_label = tk.Label(root, text=f"Puntuación: {score}", font=("Arial", 16))
score_label.pack(pady=30)

def handle_click():
    global score
    score += 1
    score_label.config(text=f"Puntuación: {score}")

base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
image_path = base_path / "mouse-left-click-icon-15066.jpg"
click_image = ImageTk.PhotoImage(Image.open(image_path))
image_button = tk.Button(root, image=click_image, command=handle_click)
image_button.pack(pady=20)

root.mainloop()