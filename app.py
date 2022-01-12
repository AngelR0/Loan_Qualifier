"""Loan Qualifier Application"""

# This command line Application pulls the functions from other locations to match the user with qualifying loans.


import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv, save_csv
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


# Asking for the file path to the latest bank data and load the CSV file.
def load_bank_data():
    csvpath = questionary.text(
        "Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    if not csvpath.exists():
        sys.exit(f"Cannot find this path you have entered: {csvpath} .")
    return load_csv(csvpath)


print("\n")


def get_applicant_info():  # Prompt dialog to get user's information

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text(
        "What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value):

    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"\nThe monthly debt to income ratio is {monthly_debt_ratio:.02f}.")

    loan_to_value_ratio = calculate_loan_to_value_ratio(
        loan_amount, home_value)
    print(f"The loan to income ratio is {loan_to_value_ratio:.02f}.\n")

    bank_data_filtered = filter_max_loan_size(loan_amount, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(
        monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(
        loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans! \n")

    return bank_data_filtered


def save_qualified_loans(qualifying_loans):

    csvpath = questionary.confirm(
        "Would you like to save the loans you qualify for?").ask()
    csvpath = Path("qualified_loans.csv")
    save_csv(csvpath, qualifying_loans)


def run():

    bank_data = load_bank_data()
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value)

    save_qualified_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
