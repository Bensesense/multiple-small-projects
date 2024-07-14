import tkinter as tk
from tkinter import ttk

def repeat_word():
    word = word_entry.get()
    try:
        number = int(number_entry.get())
        if 1 <= number <= 500:
            output = (word + '\n') * number
            output_text.delete(1.0, tk.END)  # Clear previous output
            output_text.insert(tk.END, output)
        else:
            output_text.delete(1.0, tk.END)  # Clear previous output
            output_text.insert(tk.END, "Please enter a number between 1 and 500.")
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a valid number.")

root = tk.Tk()
root.title("Word Repeater")

# Create and pack the word entry frame
word_frame = ttk.Frame(root, padding="10")
word_frame.pack(fill='x')
word_label = ttk.Label(word_frame, text="welches worti?")
word_label.pack(side='left')
word_entry = ttk.Entry(word_frame, width=30)
word_entry.pack(side='right')

# Create and pack the number entry frame
number_frame = ttk.Frame(root, padding="10")
number_frame.pack(fill='x')
number_label = ttk.Label(number_frame, text="bitte zahli eingeben bebi (1-500)")
number_label.pack(side='left')
number_entry = ttk.Entry(number_frame, width=30)
number_entry.pack(side='right')

# Create and pack the repeat button
repeat_button = ttk.Button(root, text="JETZT WORT MACHEN JUHUUUUU", command=repeat_word)
repeat_button.pack(pady=10)

# Create and pack the output text area
output_frame = ttk.Frame(root, padding="10")
output_frame.pack(fill='both', expand=True)
output_text = tk.Text(output_frame, height=10)
output_text.pack(fill='both', expand=True)

root.mainloop()