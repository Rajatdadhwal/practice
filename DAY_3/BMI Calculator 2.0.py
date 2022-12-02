height = float(input("enter the height meter's : "))
weight = float(input("enter the weight in kilogram : "))
BMI = float(weight) / float(height) ** 2
if BMI >= 18.5 :
    print("you are Under Weight")
elif BMI  >= 25 :
    print("you have a normal weight")
elif BMI  >= 30 :
    print("you are over weight") 
elif BMI  >= 35 :
    print("you are obese")
else:
    print("you are clinically obese")
