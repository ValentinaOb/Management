import tkinter as tk
from tkinter import filedialog, scrolledtext

def affine_encrypt(text, a, b):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыэюя"
    m = len(alphabet)
    encrypted_text = ""
    for char in text.lower():
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (a * idx + b) % m
            encrypted_text += alphabet[new_idx]
        else:
            encrypted_text += char
    return encrypted_text

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        encrypted_text.set(affine_encrypt(text, a, b))
    except ValueError:
        encrypted_text.set("Помилка: введіть числові значення a і b")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(encrypted_text.get())

def display_array():
    data_array = [f"Елемент {i+1}" for i in range(23)]
    array_label.config(text=", ".join(data_array))

# Створення головного вікна
root = tk.Tk()


# Відображення масиву у Label
array_label = tk.Label(root, text="")
array_label.grid(row=3, column=0, columnspan=6, padx=5, pady=5)
display_array()

root.mainloop()
