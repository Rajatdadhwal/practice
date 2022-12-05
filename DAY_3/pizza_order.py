print("Welcome to the Python Pizza Delivrs")

size = input("what size pizza do you want : s , m , l  : ")
pepperoni = input("Do you pepperoni ? : y , n  : ")
extra_cheese = input("Do you want extra cheese ? : y , n : ")


bill = 0 


if size == "s" :
    bill += 15

elif size == "m" :
    bill += 20

else:
    bill += 25



if pepperoni == "y" :
    if size == "s":
        bill += 2

    else:
        bill += 3
    



if extra_cheese == "y" :
    bill += 1


print(f"your final bill {bill}")

   
                
    











      
   
    
    




            
