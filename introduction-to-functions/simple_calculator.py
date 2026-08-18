#Simple calculator that takes two numbers and performs addition, subtraction, division, and exponentiation.
def calculator(L_a, L_b):
    added = a+b
    subtracted = a-b
    divided = a/b
    powered = a**b
    return added, subtracted, divided, powered

#Get user input for two numbers
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(calculator(a,b))