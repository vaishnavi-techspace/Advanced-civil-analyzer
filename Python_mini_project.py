import tkinter as tk
from tkinter import messagebox

def update_fields(*args):
    for widget in field_frame.winfo_children():
        widget.destroy()

    global entries, ranges
    entries = {}
    ranges = {}

    material = material_var.get()

    # Define ranges (min, max)
    if material == "Concrete":
        fields = {
            "Compressive Strength": (20, 40, "MPa"),
            "Tensile Strength": (2, 5, "MPa"),
            "Durability": (5, 10, ""),
            "Workability": (25, 100, "mm")
        }

    elif material == "Steel":
        fields = {
            "Tensile Strength": (400, 600, "MPa"),
            "Yield Strength": (250, 500, "MPa"),
            "Ductility": (10, 25, "%"),
            "Hardness": (120, 200, "HB")
        }

    elif material == "Brick":
        fields = {
            "Compressive Strength": (7, 20, "MPa"),
            "Water Absorption": (10, 20, "%"),
            "Hardness": (5, 10, ""),
            "Shape Quality": (5, 10, "")
        }

    elif material == "Cement":
        fields = {
            "Compressive Strength": (20, 50, "MPa"),
            "Setting Time": (30, 600, "min"),
            "Fineness": (225, 400, ""),
            "Soundness": (0, 10, "mm")
        }

    # Create fields with range display
    for f, (min_val, max_val, unit) in fields.items():
        tk.Label(field_frame,
                 text=f"{f} ({min_val} - {max_val} {unit})",
                 bg="#1e293b", fg="white").pack(anchor="w")

        entry = tk.Entry(field_frame)
        entry.pack(fill="x", pady=5)

        entries[f] = entry
        ranges[f] = (min_val, max_val)


def analyze():
    try:
        material = material_var.get()
        result = "PASS"
        messages = []

        for key, entry in entries.items():
            value = float(entry.get())
            min_val, max_val = ranges[key]

            if value < min_val or value > max_val:
                result = "FAIL"
                messages.append(f"{key} out of range ({min_val}-{max_val})")

        if result == "PASS":
            result_label.config(
                text=f"{material} is SAFE ✅",
                fg="lightgreen"
            )
        else:
            msg = "\n".join(messages)
            result_label.config(
                text=f"{material} is NOT SAFE ❌\n\nProblems:\n{msg}",
                fg="red"
            )

    except:
        messagebox.showerror("Error", "Enter valid numeric values")


# GUI Window
root = tk.Tk()
root.title("Advanced Civil Analysis")
root.geometry("400x600")
root.config(bg="#0f172a")

tk.Label(root, text="Civil Analysis System",
         font=("Arial", 18, "bold"),
         bg="#0f172a", fg="white").pack(pady=10)

# Material Selection
material_var = tk.StringVar(value="Concrete")
material_var.trace("w", update_fields)

tk.OptionMenu(root, material_var,
              "Concrete", "Steel", "Brick", "Cement").pack(pady=10)

# Dynamic Fields
field_frame = tk.Frame(root, bg="#1e293b")
field_frame.pack(padx=20, pady=10, fill="both")

update_fields()

# Analyze Button
tk.Button(root, text="Analyze", command=analyze,
          bg="blue", fg="white").pack(pady=10)

# Result Label
result_label = tk.Label(root, text="",
                        bg="#0f172a",
                        fg="white",
                        font=("Arial", 11),
                        justify="left")
result_label.pack(pady=20)

root.mainloop()