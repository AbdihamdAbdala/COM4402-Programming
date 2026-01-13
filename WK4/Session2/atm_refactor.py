def deposit(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount needs to be above 0")
    return float(balance + amount)

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount needs to be above 0")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return float(balance - amount)

def show_balance(balance: float) -> str:
    return f"Current balance: £{format(balance, '.2f')}"