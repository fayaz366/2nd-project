import tkinter as tk
from tkinter import messagebox

FONT_MAIN = ("Arial", 11, "bold italic")
FONT_TITLE = ("Arial", 18, "bold italic")

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isupper():
            base = ord('A')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        elif char.islower():
            base = ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def process():
    try:
        text = input_text.get("1.0", tk.END)
        shift = int(shift_entry.get())
        mode = action.get()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, caesar_cipher(text, shift, mode))
    except:
        messagebox.showerror("Error", "Enter valid shift value")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)

def copy_output():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        messagebox.showinfo("Copied", "Output copied to clipboard!\nPaste it anywhere.")
    else:
        messagebox.showwarning("Empty", "No output to copy")

def toggle_dark_mode():
    global dark
    dark = not dark

    bg = "#121212" if dark else "#E3F2FD"
    fg = "white" if dark else "black"
    box = "#1E1E1E" if dark else "white"

    root.configure(bg=bg)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

    input_text.configure(bg=box, fg=fg)
    output_text.configure(bg=box, fg=fg)
    shift_entry.configure(bg=box, fg=fg)

# ---------------- GUI ----------------
dark = False

root = tk.Tk()
root.title("Caesar Cipher App")
root.geometry("540x560")
root.configure(bg="#E3F2FD")
root.resizable(False, False)

tk.Label(root, text="Caesar Cipher Encryption",
         font=FONT_TITLE).pack(pady=10)

tk.Label(root, text="Enter Message", font=FONT_MAIN).pack(anchor="w", padx=15)
input_text = tk.Text(root, height=5, width=60, font=FONT_MAIN)
input_text.pack(padx=15)

tk.Label(root, text="Shift Value", font=FONT_MAIN).pack(anchor="w", padx=15, pady=(10, 0))
shift_entry = tk.Entry(root, width=10, font=FONT_MAIN)
shift_entry.pack(padx=15, anchor="w")

# Radio Buttons
action = tk.StringVar(value="encrypt")
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

tk.Radiobutton(radio_frame, text="Encrypt",
               variable=action, value="encrypt",
               font=FONT_MAIN).pack(side="left", padx=10)

tk.Radiobutton(radio_frame, text="Decrypt",
               variable=action, value="decrypt",
               font=FONT_MAIN).pack(side="left", padx=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Process",
          bg="#4CAF50", fg="white",
          width=12, font=FONT_MAIN,
          command=process).pack(side="left", padx=5)

tk.Button(btn_frame, text="Clear",
          bg="#F44336", fg="white",
          width=12, font=FONT_MAIN,
          command=clear_all).pack(side="left", padx=5)

tk.Button(btn_frame, text="Copy Output",
          bg="#2196F3", fg="white",
          width=12, font=FONT_MAIN,
          command=copy_output).pack(side="left", padx=5)

tk.Button(btn_frame, text="Dark Mode",
          bg="#333", fg="white",
          width=12, font=FONT_MAIN,
          command=toggle_dark_mode).pack(side="left", padx=5)

tk.Label(root, text="Output", font=FONT_MAIN).pack(anchor="w", padx=15)
output_text = tk.Text(root, height=5, width=60, font=FONT_MAIN)
output_text.pack(padx=15)

root.mainloop()
