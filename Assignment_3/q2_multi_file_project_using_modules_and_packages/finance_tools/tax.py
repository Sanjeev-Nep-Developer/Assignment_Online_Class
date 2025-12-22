def calculate_tax(income):
    if income <= 500000:
        return income * 0.01
    else:
        return income * 0.1
