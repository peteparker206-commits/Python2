import math

def sqrt(choice):
    s = math.sqrt(choice)
    print(f"The square root is: {s}")

def log(choice):
    l = math.log(choice)
    print(f"The logarithm is: {l}")

def sin(choice):
    i = math.sin(choice)
    print(f"The sine is: {i}")

num=float(input("Enter your number: "))
print("Welcome \nChoose any 1 from below||")
print("Pick 1 for Square root")
print("Pick 2 for Logarithm ")
print("Pick 3 for sine")
print("Pick 4 for doing all \n")

choice= int(input("Enter your choice: "))

match choice:
    case 1:
        sqrt(num)
    
    case 2:
        log(num)

    case 3:
        sin(num)
        
    case 4:
        sqrt(num)
        log(num)
        sin(num)
        
    case _:
        print("Please enter a valid choice!")



    
