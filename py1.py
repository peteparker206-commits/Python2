num = int(input("Enter you number: "))
fact=1

print(f"The number you entered is: {num}")
 
for i in range(1,num+1,1): 
    fact = fact*i



print(f"The factorial of a number{num} is: {fact} ")