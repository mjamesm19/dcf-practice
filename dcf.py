import numpy as np
import pandas as pd

# --- Assumptions ---
base_fcf   = 100.0   # last actual free cash flow ($M)
growth     = 0.08    # projection-window growth
wacc       = 0.10    # discount rate
terminal_g = 0.025   # perpetual growth rate
years      = 5
net_debt   = 300.0
shares     = 100.0

# --- Project & discount ---
year            = np.arange(1, years + 1)
fcf             = base_fcf * (1 + growth) ** year
discount_factor = 1 / (1 + wacc) ** year
pv_fcf          = fcf * discount_factor

# --- Terminal value ---
terminal_value    = fcf[-1] * (1 + terminal_g) / (wacc - terminal_g)
pv_terminal_value = terminal_value / (1 + wacc) ** years

# --- Valuation ---
enterprise_value = pv_fcf.sum() + pv_terminal_value
equity_value     = enterprise_value - net_debt
price_per_share  = equity_value / shares * 1

print(pd.DataFrame({
    "Year": year, "FCF": fcf.round(2),
    "Discount Factor": discount_factor.round(4), "PV of FCF": pv_fcf.round(2),
}).to_string(index=False))
print(f"\nEnterprise value: {enterprise_value:,.2f}")
print(f"Equity value    : {equity_value:,.2f}")
print(f"Price per share : {price_per_share:,.2f}")
