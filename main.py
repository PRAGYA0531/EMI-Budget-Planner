from utils import get_float_input
from emi_calculator import calculate_emi
from budget_planner import calculate_max_affordable_emi, check_loan_affordability


def main():
    print("\n===== EMI & Monthly Budget Planner =====")

    # Loan calculation inputs
    principal = get_float_input("Enter loan amount (₹): ")
    annual_rate = get_float_input("Enter annual interest rate (%): ")
    tenure_years = get_float_input("Enter loan tenure (years): ")

    # EMI calculation
    emi = calculate_emi(principal, annual_rate, tenure_years)
    print(f"\nYour calculated EMI: ₹{emi}")

    # Budget inputs
    monthly_income = get_float_input("\nEnter your monthly income (₹): ")
    essential_expenses = get_float_input("Enter your monthly essential expenses (₹): ")

    max_emi = calculate_max_affordable_emi(monthly_income, essential_expenses)
    print(f"\nMax EMI you can afford safely: ₹{max_emi}")

    # Result
    result = check_loan_affordability(emi, max_emi)
    print(f"\n📌 RESULT: {result}\n")


if __name__ == "__main__":
    main()
