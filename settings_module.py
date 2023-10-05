import tkinter as tk
from tkinter import messagebox
import json

STYLE_CONFIG_FILE = "style_config.json"

def set_window_style(root):
    root.title("Обучалка v2.0")
    root.geometry("800x600")

def load_style_config():
    try:
        with open(STYLE_CONFIG_FILE, "r") as file:
            return json.load(file)
    except:
        return {"background_color": "#F0F0F0"}

def save_style_config(config):
    with open(STYLE_CONFIG_FILE, "w") as file:
        json.dump(config, file)

def set_background_color(root, color="#F0F0F0"):
    if tk.messagebox.askyesno("Подтверждение", "Вы хотите применить этот стиль?"):
        root.configure(bg=color)
        save_style_config({"background_color": color})

def set_header_font(label, font):
    label.config(font=font)
