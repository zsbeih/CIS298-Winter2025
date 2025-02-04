import csv
def yearly_bond_stock_rates(file_name):

    with open(file_name) as bonds_and_stocks_file:
        bonds_and_stocks_reader = csv.reader(bonds_and_stocks_file)
        next(bonds_and_stocks_reader) 
        bond_stock_rates = []
        for row in bonds_and_stocks_reader:
            bond_stock_rates.append({'stocks': float(row[1].strip('%'))/100, 'bonds':  float(row[2].strip('%'))/100})

    return bond_stock_rates

bond_stock_rates = yearly_bond_stock_rates('BondsAndStocksAnnualReturn.csv')

user_age = int(input("Current age: "))
retirement_age = int(input("Expected retirement age: "))

print("\nInitial Balances:")

balance_dict = {}
balance_dict[0] = {}
year_counter = 0

# Initial balances
mattress_savings = float(input("    Money stored under a mattress: "))
balance_dict[year_counter]['mattress'] = mattress_savings

bank_savings = float(input("    Money stored in a bank: "))
balance_dict[year_counter]['bank'] = bank_savings

bonds_savings = float(input("    Money stored in bonds: "))
balance_dict[year_counter]['bonds'] = bonds_savings

stocks_savings = float(input("    Money stored in stocks: "))
balance_dict[year_counter]['stocks'] = stocks_savings

print(f"\n    Initial Total Balance: ${sum(balance_dict[year_counter].values()):,.2f}\n")


years = retirement_age - user_age

for year_counter in range(1, years + 1):
    
    balance_dict[year_counter] = {}
    print(f'Age {user_age + year_counter} ')
    
    print(f"Additional contributions:")

    # Updating balance based on new contributions
    mattress_savings = float(input("    Money stored under a mattress: "))
    balance_dict[year_counter]['mattress'] =  balance_dict[year_counter - 1]['mattress'] + mattress_savings

    bank_savings = float(input("    Money stored in a bank: "))
    balance_dict[year_counter]['bank'] = balance_dict[year_counter - 1]['bank'] + bank_savings

    bonds_savings = float(input("    Money stored in bonds: "))
    balance_dict[year_counter]['bonds'] =  balance_dict[year_counter - 1]['bonds'] +  bonds_savings

    stocks_savings = float(input("    Money stored in stocks: "))
    balance_dict[year_counter]['stocks'] =  balance_dict[year_counter - 1]['stocks'] + stocks_savings

    # Applying rates 
    balance_dict[year_counter]['mattress'] = balance_dict[year_counter]['mattress'] * 1
    balance_dict[year_counter]['bank'] = balance_dict[year_counter]['bank'] * 1.02
    balance_dict[year_counter]['bonds'] = balance_dict[year_counter]['bonds'] * (1 + bond_stock_rates[year_counter - 1]['bonds'])
    balance_dict[year_counter]['stocks'] = balance_dict[year_counter]['stocks'] * (1 + bond_stock_rates[year_counter - 1]['stocks'])

    

    print("\nCurrent total balances for each savings account:")

    print(f'    Mattress savings: ${balance_dict[year_counter]["mattress"]:,.2f}')
    print(f'    Bank savings: ${balance_dict[year_counter]["bank"]:,.2f}')
    print(f'    Bond savings: ${balance_dict[year_counter]["bonds"]:,.2f}')
    print(f'    Stock savings: ${balance_dict[year_counter]["stocks"]:,.2f}\n')
    print(f"    Total retirement savings: ${sum(balance_dict[year_counter].values()):,.2f}\n")


# Final savings and adjusted savings based on inflation
inflation = 1 / (1.02 ** years)
print("Final totals for retirement savings accounts:")
print(f'    Mattress savings: ${balance_dict[year_counter]["mattress"]:,.2f}')
print(f'    Bank savings: ${balance_dict[year_counter]["bank"]:,.2f}')
print(f'    Bond savings: ${balance_dict[year_counter]["bonds"]:,.2f}')
print(f'    Stock savings: ${balance_dict[year_counter]["stocks"]:,.2f}\n')
print(f"Total retirement savings: ${sum(balance_dict[year_counter].values()):,.2f}")
print(f"Adjusted retirement balance for inflation: ${sum(balance_dict[year_counter].values()) * inflation:,.2f}")


# Write balances to csv
with open('YearlyReturnsOnRetirementPlan.csv', 'w') as yearly_retirement_plan:
    retirement_plan_writer = csv.writer(yearly_retirement_plan)
    retirement_plan_writer.writerow(['Age', 'Mattress', 'Bank', 'Bonds', 'Stocks', 'Total'])
    
    for year in balance_dict:
        total = sum(balance_dict[year].values())
        retirement_plan_writer.writerow([
            user_age + year,
            f"${balance_dict[year]['mattress']:,.2f}",
            f"${balance_dict[year]['bank']:,.2f}",
            f"${balance_dict[year]['bonds']:,.2f}",
            f"${balance_dict[year]['stocks']:,.2f}",
            f"${total:,.2f}"
        ])






