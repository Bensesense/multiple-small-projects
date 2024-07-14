import tkinter as tk
from tkinter import messagebox

def calculate_selling_price(event=None):
    try:
        einkaufspreis = float(entry_einkaufspreis.get())
        if einkaufspreis >= 50:
            faktor = 2
        elif 20 <= einkaufspreis < 50:
            faktor = 2.5
        elif 10 <= einkaufspreis < 20:
            faktor = 3
        elif 1 <= einkaufspreis < 10:
            faktor = 3.5
        else:
            messagebox.showerror("Error", "Einkaufspreis is too low to be considered.")
            return

        verkaufspreis = einkaufspreis * faktor
        label_verkaufspreis.config(text=f"Der Verkaufspreis beträgt: {verkaufspreis:.2f} €")
    except ValueError:
        messagebox.showerror("Error", "Bitte geben Sie einen gültigen Preis ein.")

app = tk.Tk()
app.title("Wine Price Calculator")

tk.Label(app, text="Einkaufspreis:").pack(pady=10)
entry_einkaufspreis = tk.Entry(app)
entry_einkaufspreis.pack(pady=5)
entry_einkaufspreis.bind('<Return>', calculate_selling_price)  # Bind the Enter key to the function

tk.Button(app, text="Calculate", command=calculate_selling_price).pack(pady=20)

label_verkaufspreis = tk.Label(app, text="")
label_verkaufspreis.pack(pady=10)

app.geometry("300x200")
app.mainloop()