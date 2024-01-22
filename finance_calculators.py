import math

# menu to choose between investment or bond

menu_choice = input ('''investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: ''').lower()

# elif structure that diverges based on the previous choice, first goes through calculations if investment is chosen

if menu_choice == "investment":
    deposit = int ( input ('''You've chosen investment
    What is your deposit amount? ''') )
    interest_rate = int ( input ("What is your interest rate (%) ") )
    years = int ( input ("How many years do you plan on investing? ") )
    interest_type = input ("Do you want to calculate simple or compound interest? ").lower()

# sub-elif to do separate calculations based on the choice between simple or compound interest

    if interest_type == "simple": 
        amount =  round ( deposit * ( 1 + ( interest_rate / 100 ) * years ) , 2 )
        
    elif interest_type == "compound":
        amount = round ( deposit * math.pow ( ( 1 + ( interest_rate / 100 ) ) , years ) , 2 )
    print (f"Your total return will be £{amount}")

# elif structure that continues for the bond choice

elif menu_choice == "bond":
    house_value = int ( input ('''You've chosen bond
    What is the current value of your house? ''') )
    interest_rate = int ( input ("What is the interest rate (%)? ") )
    repay_months = int ( input ("In how many months do you want to repay the debt? ") )
    interest_rate_div = (interest_rate / 100 ) / 12 # modified interest rate for later formula use
    repayment_per_month = round ( ( interest_rate_div * house_value ) / (1 - ( 1 + interest_rate_div) ** ( - repay_months)) , 2 )
    print (f"Your repayments will be £{repayment_per_month} per month.")


# invalid input at line 5 

else :
    print ("Invalid input, start over and please select 'investment' or 'bond'")


