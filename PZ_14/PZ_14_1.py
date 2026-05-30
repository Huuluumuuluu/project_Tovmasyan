# Реализовать интерфейс по прототипу: https://studfile.net/html/2706/360/html_uTKKMTCo1E.hFYH/htmlconvdf-eYkCR62x1.jpg
# Максимально приближённо к оригиналу с помощью tkinter.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Регистрация")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Регистрация", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Имя:", bg="#f0f0f0").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Email:", bg="#f0f0f0").pack()
entry_email = tk.Entry(root)
entry_email.pack()
tk.Label(root, text="Пароль:", bg="#f0f0f0").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

def register():
    if entry_name.get() and entry_email.get() and entry_pass.get():
        messagebox.showinfo("Успех", f"Добро пожаловать, {entry_name.get()}!")
    else:
        messagebox.showerror("Ошибка", "Заполните все поля")

tk.Button(root, text="Зарегистрироваться", command=register, bg="#4CAF50", fg="white").pack(pady=20)
root.mainloop()
