import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json
import base64
import datetime
import os

# Function to decode the key from a base64-encoded string
def get_embedded_key():
    # Example part 1
    obfuscated_key_part1 = "WSzBGyUTm0N" 
    # Example part 2
    obfuscated_key_part2 = "nSJuS021tPw=="
    obfuscated_key = obfuscated_key_part1 + obfuscated_key_part2
    decoded_key = base64.b64decode(obfuscated_key)
    return decoded_key

key = get_embedded_key()

def decrypt_file(input_file, output_file):
    with open(input_file, 'r') as f:
        encrypted_data = json.load(f)

    iv = base64.b64decode(encrypted_data['iv'])
    ciphertext = base64.b64decode(encrypted_data['ciphertext'])
    encryption_date = datetime.datetime.strptime(encrypted_data['date'], "%Y-%m-%d %H:%M:%S")
    duration_hours = encrypted_data['duration_hours']

    current_date = datetime.datetime.now()
    available_date = encryption_date + datetime.timedelta(hours=duration_hours)

    if current_date < available_date:
        raise Exception(f"Please try again after: {available_date.strftime('%Y-%m-%d %H:%M:%S')}.")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

def select_encrypted_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        encrypted_file_entry.delete(0, tk.END)
        encrypted_file_entry.insert(0, file_path)
        display_decryption_date(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, file_path)

def display_decryption_date(file_path):
    try:
        with open(file_path, 'r') as f:
            encrypted_data = json.load(f)
        encryption_date = datetime.datetime.strptime(encrypted_data['date'], "%Y-%m-%d %H:%M:%S")
        duration_hours = encrypted_data['duration_hours']
        available_date = encryption_date + datetime.timedelta(hours=duration_hours)
        decryption_date_label.config(text=f"File can be decrypted after: {available_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        decryption_date_label.config(text=f"Error reading file: {str(e)}")

def decrypt():
    encrypted_file = encrypted_file_entry.get()
    output_file = output_file_entry.get()

    if not os.path.isfile(encrypted_file):
        messagebox.showerror("Error", "Please select a valid encrypted file.")
        return
    
    if not output_file:
        messagebox.showerror("Error", "Please select a valid output file.")
        return

    try:
        decrypt_file(encrypted_file, output_file)
        messagebox.showinfo("Success", "Decryption successful!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Decryption Tool")

tk.Label(root, text="Encrypted File:").grid(row=0, column=0, padx=10, pady=10)
encrypted_file_entry = tk.Entry(root, width=50)
encrypted_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_encrypted_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse...", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

decryption_date_label = tk.Label(root, text="File can be decrypted after: N/A")
decryption_date_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Decrypt", command=decrypt).grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()









