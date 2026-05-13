

def validate_email(email) -> bool:
     length = len(email)
     if length <8:
          return False
     if "@" not in email:
          return False
     first_character = email[0]
     last_character = email[length-1]

     if first_character == "@" or last_character == "@":
        return False

     return True


print(validate_email("123456789@"))


def calculate_balance(transactions):
     balance =0
     length = len(transactions)
     if length == 0:
          return 0
     for transaction in transactions:
          balance += transaction
     return balance

print(calculate_balance([5,-10]))


def is_strong_password(password) -> bool:
     length = len(password)
     if length <8:
          return False
     return True

print(is_strong_password("12345678"))


def apply_intrest(balance,rate,years):
     if rate < 0 or years < 1:
          raise ValueError("Invalid inputs")
     interest = balance *(1+rate)**years
     return interest
          
def get_transaction_summary(transactions):

    credit = 0
    debit = 0
    transaction_count = 0

    for transaction in transactions:

        transaction_type = transaction[0]
        amount = transaction[1]

        if transaction_type == "credit":
            credit += amount

        elif transaction_type == "debit":
            debit += amount

        transaction_count += 1

    result = {
        "total_credits": credit,
        "total_debit": debit,
        "net_balance": credit - debit,
        "transaction_count": transaction_count
    }

    return result

print(get_transaction_summary([

                         ["credit", 2000],["debit",500],["credit", 300]
          ]
))














