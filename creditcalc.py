from math import ceil, log, floor
import argparse


def calculate_interest(i):
    return (i * 0.01) / 12


def calculate_periods(payment, principal, interest):
    interest = calculate_interest(interest)
    periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
    if 1 < periods <= 12:
        print(f"It will take {periods} months to repay this loan!")
    elif periods == 1:
        print("It will take 1 month to repay this loan!")
    else:  # TODO It will take 2 years and 0 months to repay this loan!
        print(f"It will take {periods // 12} years and {periods % 12} months to repay this loan!")
    calculate_overpayment(principal, periods, payment)


def calculate_annuity_payment(principal, periods, interest):
    interest = calculate_interest(interest)
    payment = ceil((principal * (interest * (1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    # last_payment = principal - (periods - 1) * payment
    # if last_payment > 0:
    #     print(f"Your monthly payment = {payment} and the last payment = {last_payment}")
    # else:
    print(f"Your annuity payment = {payment}")
    calculate_overpayment(principal, periods, payment)


def calculate_diff_payment(principal, periods, interest):
    interest = calculate_interest(interest)
    total_payments = 0
    for m in range(1, periods + 1):
        payment = ceil(principal / periods + interest * (principal - (principal * (m - 1)) / periods))
        print(f"Month {m}: payment is {payment}")
        total_payments += payment
    calculate_overpayment(principal, 1, total_payments)


def calculate_principal(payment, periods, interest):
    interest = calculate_interest(interest)
    principal = floor(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
    print(f"Your loan principal = {principal}!")
    calculate_overpayment(principal, periods, payment)


def calculate_overpayment(principal, periods, payment):
    overpayment = ceil(periods * payment - principal)
    print(f"Overpayment = {overpayment}")


def validate_input(args):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"], help="type diff / annuity")
parser.add_argument("--payment", help="payment 10000. Not valid with 'type diff'")
parser.add_argument("--principal", help="You can get its value if you know the interest,"
                                        " annuity payment, and number of months.")
parser.add_argument("--periods",)  # number of months needed to repay the loan. It's calculated based on the interest,
                                   # annuity payment, and principal.
parser.add_argument("--interest", help="it must always be provided")
args = parser.parse_args()

total_args = [args.type, args.payment, args.principal, args.periods, args.interest]

if not args.type or not args.interest:
    print("Incorrect parameters")
    print('1')
elif len(total_args) < 4:
    print("Incorrect parameters")
    print('2')
elif args.type == 'diff' and args.payment:
    print("Incorrect parameters")
    print('3')
elif not all([args]):
    print("Incorrect parameters")
    print('4')
else:
    loan_type = args.type
    payment = int(args.payment) if args.payment else False
    principal = int(args.principal) if args.principal else False
    periods = int(args.periods) if args.periods else False
    interest = float(args.interest)
    if principal and periods:
        if loan_type == "diff":
            calculate_diff_payment(principal, periods, interest)
        elif loan_type == "annuity":
            calculate_annuity_payment(principal, periods, interest)
    elif principal and payment:
        calculate_periods(payment, principal, interest)
    elif payment and periods:
        calculate_principal(payment, periods, interest)

#
# # calculate_periods(payment, principal, interest)
# # calculate_annuity_payment(principal, periods, interest)
# # calculate_diff_payment(principal, periods, interest)
# calculate_principal(payment, periods, interest)
#
#
# #
# # input choice
# choice = input("""
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# """)
#
# if choice == 'n':
#     principal = int(input("Enter the loan principal:"))
#     payment = float(input("Enter the monthly payment:"))
#     interest = float(input("Enter the loan interest:"))
#     interest = calculate_interest(interest)
#     months = ceil(log(payment / (payment - interest * principal), 1 + interest))
#     if 1 < months <= 12:
#         print(f"It will take {months} months to repay this loan!")
#     elif months == 1:
#         print("It will take 1 month to repay this loan!")
#     else:
#         print(f"It will take {months // 12} years and {months % 12} months to repay this loan!")
# elif choice == 'a':  # annuity monthly payment amount
#     principal = int(input("Enter the loan principal:"))
#     months = int(input("Enter the number of periods:"))
#     interest = float(input("Enter the loan interest:"))
#     interest = calculate_interest(interest)
#     payment = ceil((principal * (interest * (1 + interest) ** months)) / (((1 + interest) ** months) - 1))
#     last_payment = principal - (months - 1) * payment
#     if last_payment:
#         print(f"Your monthly payment = {payment} and the last payment = {last_payment}")
#     else:
#         print(f"Your monthly payment = {payment}")
# elif choice == 'p':
#     payment = float(input("Enter the annuity payment:"))
#     months = int(input("Enter the number of periods:"))
#     interest = float(input("Enter the loan interest:"))
#     interest = calculate_interest(interest)
#     principal = ceil(payment / ((interest * (1 + interest) ** months) / ((1 + interest) ** months - 1)))
#     print(f"Your loan principal = {principal}!")
# else:
#     print("Wrong input. Try again. " + choice)
