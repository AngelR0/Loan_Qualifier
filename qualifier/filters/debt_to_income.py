"""Debt To Income Filter"""

# Filters the bank list by the max debt to income ratio allowed by the bank.


def filter_debt_to_income(monthly_debt_ratio, bank_list):
    debt_to_income_approval_list = []

    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            debt_to_income_approval_list.append(bank)
    return debt_to_income_approval_list
