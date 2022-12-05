print("welcome to the Roller coster")

height = float(input("enter your height in centimeter's : "))

if height >= 120 :
    print("you can Ride the Roller Coster !")
    
    age = int(input("enter your age : "))
    
    if age <= 12 :

        bill = 5

         
        print ("your ticket is 5 rupees")
        
        bill = 5

    elif age <= 18 :

        bill = 7

        print("your ticket is 7 rupees")
        

    else:
        
        bill = 12 

        print("your ticket is 12 rupees")
        
want_picture = input("you want picture : y or n : ")

if want_picture == "y":

    bill += 3

print(f"your final bill is {bill}")    
    



