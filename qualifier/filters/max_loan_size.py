"""Max Loan Size Filter"""

# Filters the bank list by the maximum allowed loan amount.


def filter_max_loan_size(loan_amount, bank_list):
    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
