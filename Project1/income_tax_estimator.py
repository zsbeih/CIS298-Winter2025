def income_tax_calc(adj_gross_inc):

    taxes_37 = 0
    taxes_35 = 0
    taxes_32 = 0
    taxes_24 = 0
    taxes_22 = 0
    taxes_12 = 0
    taxes_10 = 0
    total_taxes = 0

    if adj_gross_inc > 609350:
        tax_bracket = adj_gross_inc - 609350
        taxes_37 = (tax_bracket) * 0.37
        total_taxes += taxes_37
        adj_gross_inc = 609350
    
    if adj_gross_inc > 243725:
        tax_bracket = adj_gross_inc - 243725
        taxes_35 = (tax_bracket) * 0.35
        total_taxes += taxes_35
        adj_gross_inc = 243725
    
    if adj_gross_inc > 191950:
        tax_bracket = adj_gross_inc - 191950
        taxes_32 = (tax_bracket) * 0.32
        total_taxes += taxes_32
        adj_gross_inc = 191950
    
    if adj_gross_inc > 100525:
        tax_bracket = adj_gross_inc - 100525
        taxes_24 = (tax_bracket) * 0.24
        total_taxes += taxes_24
        adj_gross_inc = 100525

    if adj_gross_inc > 47150:
        tax_bracket = adj_gross_inc - 47150
        taxes_22 = (tax_bracket) * 0.22
        total_taxes += taxes_22
        adj_gross_inc = 47150

    if adj_gross_inc > 11600:
        tax_bracket = adj_gross_inc - 11600
        taxes_12 = (tax_bracket) * 0.12
        total_taxes += taxes_12
        adj_gross_inc = 11600

    if adj_gross_inc > 0:
        tax_bracket = adj_gross_inc - 0
        taxes_10 = (tax_bracket) * 0.10
        total_taxes += taxes_10
    
    print(f"Taxes owed at 10% bracket: ${taxes_10:.2f}")
    print(f"Taxes owed at 12% bracket: ${taxes_12:.2f}")
    print(f"Taxes owed at 22% bracket: ${taxes_22:.2f}")
    print(f"Taxes owed at 24% bracket: ${taxes_24:.2f}")
    print(f"Taxes owed at 32% bracket: ${taxes_32:.2f}")
    print(f"Taxes owed at 35% bracket: ${taxes_35:.2f}")
    print(f"Taxes owed at 37% bracket: ${taxes_37:.2f}")

    return total_taxes

another_input = 'y'
counter = 1
gross_income = 0
gross_deduction = 0

while another_input == 'y':
    curr_income = input(f"Income {counter}: (input only the number, no commas or special symbols)")
    gross_income += int(curr_income)
    counter += 1
    another_input = input("Do you have another income? y/n").lower()

another_input = 'y'
counter = 1

while another_input == 'y':
    curr_deduction = input(f"Deduction {counter}: (input only the number, no commas or special symbols)")
    gross_deduction += int(curr_deduction)
    counter += 1
    another_input = input("Do you have another deduction? y/n").lower()

if gross_deduction < 14600:
    gross_deduction = 14600


adj_gross_inc = gross_income - gross_deduction


print(f'Gross Income: ${gross_income}')
print(f'Total Deductions: ${gross_deduction}')
print(f'Adjusted Gross Income: ${adj_gross_inc}')

taxes_owed = income_tax_calc(adj_gross_inc)


print(f'Total taxes owed: ${taxes_owed:.2f}')
if taxes_owed == 0:
    print(f'Taxes as percentage of AGI: 0.00%')
    print(f'Taxes as percentage of Gross Income: 0.00%')
else:
    print(f'Taxes as percentage of AGI: {(taxes_owed / adj_gross_inc*100):.2f}%')
    print(f'Taxes as percentage of Gross Income: {(taxes_owed / gross_income*100):.2f}%')





