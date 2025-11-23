def calculate_max_affordable_emi(monthly_income, essential_expenses):
    savings = monthly_income - essential_expenses
    # 40% rule for safe EMI
    max_emi = savings * 0.40
    return round(max_emi, 2)


def check_loan_affordability(calculated_emi, max_emi):
    if calculated_emi <= max_emi:
        return "GOOD! You can afford this EMI safely."
    else:
        return "WARNING! This EMI is too high for your budget."
