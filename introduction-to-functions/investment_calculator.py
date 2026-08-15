# This function calculates the final value of an investment given the initial investment amount, the interest rate, and the number of years.
def investment(L_invest, L_interest, L_years):
    value = invest*(1 + interest/100)**years
    final_value = round(value, 2)
    return final_value

#Get user input for investment details
invest = float(input("Enter how many pounds have been invested: £"))
interest = float(input("Enter percentage interest: "))
years = float(input("Enter how many years: "))
print(investment(invest, interest, years))