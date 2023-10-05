import tkinter as tk
from tkinter import ttk, Frame, simpledialog, colorchooser, font
import obuchalka.settings_module as settings

def on_button_click():
    print("Кнопка нажата!")

def change_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        settings.set_background_color(root, color)
        style_config["background_color"] = color
        settings.save_style_config(style_config)

def change_header_font():
    font_win = tk.Toplevel(root)
    font_win.title("Выбор шрифта")
    font_win.geometry("300x150")

    # Стилизация окна выбора шрифта
    font_win_frame = ttk.Frame(font_win, padding="10")
    font_win_frame.pack(fill=tk.BOTH, expand=True)
    
    label = ttk.Label(font_win_frame, text="Выберите шрифт:")
    label.grid(row=0, column=0, pady=10, sticky=tk.W)
    
    font_families = list(tk.font.families())
    combobox = ttk.Combobox(font_win_frame, values=font_families, state="readonly")
    combobox.grid(row=1, column=0, pady=10, sticky=tk.W)
    combobox.set(style_config["header_font"][0])

    def apply_font_choice():
        family = combobox.get()
        if family in font_families:
            size = style_config["header_font"][1]
            style_config["header_font"] = [family, size, "bold"]
            settings.save_style_config(style_config)
            settings.set_header_font(header_label, style_config["header_font"])
            font_win.destroy()

    apply_button = ttk.Button(font_win_frame, text="Применить", command=apply_font_choice)
    apply_button.grid(row=2, column=0, pady=10)

root = tk.Tk()
settings.set_window_style(root)

# Загрузка сохраненных настроек стиля
style_config = settings.load_style_config()
settings.set_background_color(root, style_config["background_color"])

# Создание выпадающего меню
menu = tk.Menu(root)
root.config(menu=menu)

# Пункты меню
settings_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Настройки", menu=settings_menu)
settings_menu.add_command(label="Изменить цвет фона", command=change_background_color)
settings_menu.add_command(label="Изменить шрифт заголовка", command=change_header_font)

# Шапка
header_frame = Frame(root, bg="lightgray", height=100, relief=tk.RAISED, bd=2)
header_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

header_label = ttk.Label(header_frame, text="Добро пожаловать в обучалку v2.0", font=style_config["header_font"])
header_label.place(x=200, y=30)

# Центральная область
center_frame = ttk.Frame(root)
center_frame.pack(pady=200)

# Подвал
footer_frame = Frame(root, bg="lightgray", height=100, relief=tk.RAISED, bd=2)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

button_style = ttk.Style()
button_style.configure('TButton', font=("Arial", 12), relief=tk.RAISED, bd=4)
button = ttk.Button(footer_frame, text="К модулю конструктов основного интерфейса пользователя", command=on_button_click, style='TButton')
button.place(x=200, y=30)

root.mainloop()
