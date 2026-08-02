def present_value(cash_flow, rate, year):
    return cash_flow * (1 + rate) ** year   # <-- bug: should be division
