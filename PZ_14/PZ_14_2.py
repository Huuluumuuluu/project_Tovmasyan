# Разработать программу с tkinter, взяв любую задачу из ПЗ №1-9.
# Выбрана задача: "Конвертер температур" (перевод между °C и °F).

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Конвертер температур")
root.geometry("300x200")

tk.Label(root, text="Конвертер °C <-> °F", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root)
entry.pack()
var = tk.StringVar(value="CtoF")
tk.Radiobutton(root, text="Цельсий -> Фаренгейт", variable=var, value="CtoF").pack()
tk.Radiobutton(root, text="Фаренгейт -> Цельсий", variable=var, value="FtoC").pack()

def convert():
    try:
        val = float(entry.get())
        if var.get() == "CtoF":
            res = val * 9/5 + 32
            messagebox.showinfo("Результат", f"{val}°C = {res:.1f}°F")
        else:
            res = (val - 32) * 5/9
            messagebox.showinfo("Результат", f"{val}°F = {res:.1f}°C")
    except:
        messagebox.showerror("Ошибка", "Введите число")

tk.Button(root, text="Конвертировать", command=convert).pack(pady=10)
root.mainloop()
