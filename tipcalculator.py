print("WELCOME TO TIP CALCULATOR")

# TIP CALCULATOR
try:
    total_BILL = float(input("enter the total bill amount :"))
     # float function makes calculation easy 
    no_of_people = int(input("enter how many people need to divide :"))
    tip_needed = int(input("enter how much tip you need to give :"))

    # tip can be your wish [NO LIMIT FOR TIP] as required

    tip_percentage = total_BILL*(tip_needed/100)

    # to calculate total amount initial step is to calculate the tip percentage

    tip_amount = total_BILL + tip_percentage

    print("so the total amount need to pay is :", tip_amount/no_of_people)

except:
    print("Invalid input. Please enter numerical values.")
    

    



