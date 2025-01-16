# Note: used recursive approach just for fun, definitely not the most efficient approach. In addition, I included handling for edge cases(specifically when taxes owed would be $0)

def income_tax_calc(adj_gross_inc):

    if adj_gross_inc > 609350:
        tax_bracket = adj_gross_inc - 609350
        taxes = (tax_bracket) * 0.37
        return taxes + income_tax_calc(609350)
    
    elif adj_gross_inc > 243725:
        tax_bracket = adj_gross_inc - 243725
        taxes = (tax_bracket) * 0.35
        return taxes + income_tax_calc(243725)
    
    elif adj_gross_inc > 191950:
        tax_bracket = adj_gross_inc - 191950
        taxes = (tax_bracket) * 0.32
        return taxes + income_tax_calc(191950)
    
    elif adj_gross_inc > 100525:
        tax_bracket = adj_gross_inc - 100525
        taxes = (tax_bracket) * 0.24
        return taxes + income_tax_calc(100525)
    
    elif adj_gross_inc > 47150:
        tax_bracket = adj_gross_inc - 47150
        taxes = (tax_bracket) * 0.22
        return taxes + income_tax_calc(47150)
    
    elif adj_gross_inc > 11600:
        tax_bracket = adj_gross_inc - 11600
        taxes = (tax_bracket) * 0.12
        return taxes + income_tax_calc(11600)
    
    elif adj_gross_inc > 0:
        tax_bracket = adj_gross_inc - 0
        taxes = (tax_bracket) * 0.10
        return taxes
    else: 
        return 0

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

taxes_owed = income_tax_calc(adj_gross_inc)

print(f'Total taxes owed: ${taxes_owed:.2f}')
if taxes_owed == 0:
    print(f'Taxes as percentage of AGI: 0.00%')
    print(f'Taxes as percentage of Gross Income: 0.00%')
else:
    print(f'Taxes as percentage of AGI: {(taxes_owed / adj_gross_inc*100):.2f}%')
    print(f'Taxes as percentage of Gross Income: {(taxes_owed / gross_income*100):.2f}%')





