#Function to return the smallest and largest numbers of the numbers inputted by the user.
def numbers(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return largest, smallest

#Get user input for three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
print(numbers(number1, number2, number3))