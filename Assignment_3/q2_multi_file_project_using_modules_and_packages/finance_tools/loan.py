def calculate_emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    months = time * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)
    return emi
