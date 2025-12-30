def calculate_tax(income, brackets):
    """Calculate tax based on income and tax brackets."""
    tax = 0
    prev_limit = 0
    
    for rate, limit in brackets:
        if income <= prev_limit:
            break
        
        taxable_in_bracket = min(income, limit) - prev_limit
        tax += taxable_in_bracket * rate
        prev_limit = limit
        
        if income <= limit:
            break
    
    return tax

# Tax brackets for 2009 [rate, upper_limit]
tax_brackets = {
    0: [  # Single
        (0.10, 8350),
        (0.15, 33950),
        (0.25, 82250),
        (0.28, 171550),
        (0.33, 372950),
        (0.35, float('inf'))
    ],
    1: [  # Married Filing Jointly or Qualifying Widow(er)
        (0.10, 16700),
        (0.15, 67900),
        (0.25, 137050),
        (0.28, 208850),
        (0.33, 372950),
        (0.35, float('inf'))
    ],
    2: [  # Married Filing Separately
        (0.10, 8350),
        (0.15, 33950),
        (0.25, 68525),
        (0.28, 104425),
        (0.33, 186475),
        (0.35, float('inf'))
    ],
    3: [  # Head of Household
        (0.10, 11950),
        (0.15, 45500),
        (0.25, 117450),
        (0.28, 190200),
        (0.33, 372950),
        (0.35, float('inf'))
    ]
}

# Get user input
print("Federal Income Tax Calculator")
print("=" * 40)
print("Filing Status:")
print("0 - Single")
print("1 - Married Filing Jointly or Qualified Widow(er)")
print("2 - Married Filing Separately")
print("3 - Head of Household")
print()

status = int(input("Enter filing status (0-3): "))

if status not in [0, 1, 2, 3]:
    print("Invalid filing status. Please enter 0, 1, 2, or 3.")
else:
    income = float(input("Enter taxable income: $"))
    
    if income < 0:
        print("Income cannot be negative.")
    else:
        tax = calculate_tax(income, tax_brackets[status])
        
        print()
        print("=" * 40)
        print(f"Taxable Income: ${income:,.2f}")
        print(f"Total Tax: ${tax:,.2f}")
        
        if income > 0:
            effective_rate = (tax / income) * 100
            print(f"Effective Tax Rate: {effective_rate:.2f}%")