# TIP CALCULATOR

print("WELCOME TO THE TIP CALCULATOR")

amount = float(input("enter the amount of bill : "))
tip = int(input("enter the tip percentage value 10 , 12 ,14 ? "))
split = int(input("enter the number in which the bill can split into ? "))

calculation = round(((tip / amount * 100) +  amount) / split  , 2)
print(f"your total amount is {amount} and tip percentage is {tip} and after spliting into {split} your each share is {calculation}")
print("thanks")

