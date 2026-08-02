def present_value(cash_flow, rate, year):
    return cash_flow / (1 + rate) ** year   # discount: divide to bring future cash to present value
