import tkinter as tk
from tkinter import messagebox, scrolledtext

TURKISH_ALPHABET = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"


def generate_key(msg, key):
    key = list(key)
    for i in range(len(msg) - len(key)):
        key.append(key[i % len(key)])
    return "".join(key)


def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)

    for i in range(len(msg)):
        char = msg[i]
        if char.upper() in TURKISH_ALPHABET:
            is_upper = char.isupper()
            msg_index = TURKISH_ALPHABET.index(char.upper())
            key_index = TURKISH_ALPHABET.index(key[i].upper())
            new_index = (msg_index + key_index) % len(TURKISH_ALPHABET)
            encrypted_char = TURKISH_ALPHABET[new_index]
            encrypted_text.append(encrypted_char if is_upper else encrypted_char.lower())
        else:
            encrypted_text.append(char)

    return "".join(encrypted_text)


def decrypt_vigenere(msg, key):
    
    decrypted_text = []
    key = generate_key(msg, key)

    for i in range(len(msg)):
        char = msg[i]
        if char.upper() in TURKISH_ALPHABET:
            is_upper = char.isupper()
            msg_index = TURKISH_ALPHABET.index(char.upper())
            key_index = TURKISH_ALPHABET.index(key[i].upper())
            new_index = (msg_index - key_index) % len(TURKISH_ALPHABET)
            decrypted_char = TURKISH_ALPHABET[new_index]
            decrypted_text.append(decrypted_char if is_upper else decrypted_char.lower())
        else:
            decrypted_text.append(char)

    return "".join(decrypted_text)


def encrypt_action():
    plaintext = plaintext_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if not plaintext or not key:
        messagebox.showerror("Hata", "Lütfen metin ve anahtar giriniz.")
        return
    ciphertext = encrypt_vigenere(plaintext, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, ciphertext)


def decrypt_action():
    ciphertext = ciphertext_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if not ciphertext or not key:
        messagebox.showerror("Hata", "Lütfen şifreli metin ve anahtar giriniz.")
        return
    plaintext = decrypt_vigenere(ciphertext, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, plaintext)


# GUI Setup
root = tk.Tk()
root.title("Vigenère Cipher")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# Key
tk.Label(root, text="Key:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
key_entry = tk.Entry(root, font=("Arial", 12), width=40)
key_entry.pack()

# Plain Text
tk.Label(root, text="Plain Text:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
plaintext_entry = scrolledtext.ScrolledText(root, font=("Arial", 12), width=50, height=3)
plaintext_entry.pack()

# Encrypt Button
tk.Button(root, text="Encrypt", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=encrypt_action).pack(
    pady=5)

# Cipher Text
tk.Label(root, text="Cipher Text:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
ciphertext_entry = scrolledtext.ScrolledText(root, font=("Arial", 12), width=50, height=3)
ciphertext_entry.pack()

# Decrypt
tk.Button(root, text="Decrypt", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=decrypt_action).pack(
    pady=5)

tk.Label(root, text="Result:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
result_text = scrolledtext.ScrolledText(root, font=("Arial", 12), width=50, height=3)
result_text.pack()

root.mainloop()
