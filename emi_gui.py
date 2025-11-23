import tkinter as tk
from tkinter import messagebox


# ------------ EMI Calculation -------------
def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
          ((1 + monthly_rate) ** tenure_months - 1)

    return round(emi, 2)


# ------------ Budget Calculation -------------
def calculate_max_affordable_emi(monthly_income, essential_expenses):
    savings = monthly_income - essential_expenses
    max_emi = savings * 0.40  # 40% safe EMI rule
    return round(max_emi, 2)


# ------------ On Button Click -------------
def on_calculate():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        tenure = float(entry_tenure.get())
        income = float(entry_income.get())
        expenses = float(entry_expenses.get())

        emi = calculate_emi(principal, rate, tenure)
        max_emi = calculate_max_affordable_emi(income, expenses)

        emi_result.set(f"Calculated EMI: ₹{emi}")
        max_result.set(f"Max Affordable EMI: ₹{max_emi}")

        if emi <= max_emi:
            final_result.set("✔ You can afford this EMI.")
        else:
            final_result.set("⚠ This EMI is too high for your budget.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values!")


# ---------------- GUI SETUP ------------------

root = tk.Tk()
root.title("EMI & Budget Planner")
root.geometry("450x500")
root.config(bg="#F2F2F2")

title = tk.Label(root, text="EMI & Budget Calculator", font=("Arial", 18, "bold"), bg="#F2F2F2")
title.pack(pady=10)

# INPUT FRAME
frame = tk.Frame(root, bg="#F2F2F2")
frame.pack(pady=10)

labels = [
    "Loan Amount (₹):",
    "Interest Rate (%):",
    "Tenure (Years):",
    "Monthly Income (₹):",
    "Essential Expenses (₹):"
]

entries = []

for text in labels:
    lbl = tk.Label(frame, text=text, font=("Arial", 12), bg="#F2F2F2")
    lbl.pack(anchor="w", pady=2)

    ent = tk.Entry(frame, font=("Arial", 12), width=25)
    ent.pack(pady=2)
    entries.append(ent)

entry_principal, entry_rate, entry_tenure, entry_income, entry_expenses = entries

# BUTTON
btn = tk.Button(
    root,
    text="Calculate EMI",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    command=on_calculate
)
btn.pack(pady=15)

# OUTPUT LABELS
emi_result = tk.StringVar()
max_result = tk.StringVar()
final_result = tk.StringVar()

tk.Label(root, textvariable=emi_result, font=("Arial", 14), bg="#F2F2F2").pack(pady=8)
tk.Label(root, textvariable=max_result, font=("Arial", 14), bg="#F2F2F2").pack(pady=8)
tk.Label(root, textvariable=final_result, font=("Arial", 14, "bold"), bg="#F2F2F2").pack(pady=8)

root.mainloop()
