import tkinter as tk
from tkinter import filedialog, scrolledtext

def affine_encrypt(text, a, b):
    alphabet = "A B C D E F G H I K L M N O P Q R S T V X Y Z"
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
        encrypted_text.set("Error")

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

# Створення головного вікна
root = tk.Tk()
root.title("Шифрування")
root.geometry("600x400")

tk.Label(root, text="Number of symbols").grid(row=0, column=0, padx=5, pady=5, sticky='w')
tk.Entry(root, width=5, justify='center', state='disabled', textvariable=tk.StringVar(value='23')).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Параметри шифрування").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="a=").grid(row=0, column=3, padx=2, pady=5, sticky='e')
a_entry = tk.Entry(root, width=3, justify='center')
a_entry.grid(row=0, column=4, padx=5, pady=5)
tk.Label(root, text="b=").grid(row=0, column=5, padx=2, pady=5, sticky='e')
b_entry = tk.Entry(root, width=3, justify='center')
b_entry.grid(row=0, column=6, padx=5, pady=5)

tk.Button(root, text="Відкрити вихідний файл", command=open_file).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text="Зашифрувати", command=encrypt).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Зберегти зашифрований файл", command=save_file).grid(row=1, column=2, padx=5, pady=5)

# Поля введення та виводу
input_text = scrolledtext.ScrolledText(root, width=40, height=10)
input_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

encrypted_text = tk.StringVar()
output_text = scrolledtext.ScrolledText(root, width=40, height=10)
output_text.grid(row=2, column=3, columnspan=3, padx=5, pady=5)
output_text.insert("1.0", encrypted_text.get())
output_text.config(state='disabled')

root.mainloop()
