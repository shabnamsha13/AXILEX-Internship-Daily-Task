class LowBalanceError(Exception):
    pass

try:
    balance = int(input("Enter your account balance: "))

    if balance < 1000:
        raise LowBalanceError("Balance is too low! Minimum balance should be 1000.")

    print("Transaction allowed. Your balance is:", balance)

except LowBalanceError as e:
    print("Custom Error:", e)

except ValueError:
    print("Please enter a valid amount.")
