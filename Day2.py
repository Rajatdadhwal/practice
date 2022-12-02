# BMI CALCULATOR :::::

height = input("enter the weight in meters's : ")
weight = input("enter the height in kilogram's : ")

BMI = int(weight) / float(height) ** 2

print(int(BMI))

# YOUR LIFE IN WEEKS :::::

age = int(input("whats is your age : "))


years_remaining = 70 - age
month_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining  = years_remaining * 365

print(f"you have {years_remaining} years , {month_remaining} months , {weeks_remaining} weeks , {days_remaining} days remaining")



