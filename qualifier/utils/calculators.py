"""Financial Calculators
    To determine loan qualifications.
"""


# Calculates users monthly debt to income ratio
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):

    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


# Calculates users loan to value ratio based on inputs
def calculate_loan_to_value_ratio(loan_amount, home_value):

    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
