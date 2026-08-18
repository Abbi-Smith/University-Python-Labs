#Binary calculator that takes an integer between 8 and 15 and returns the binary representation as a tuple of four bits.
def binaryCalculator(number):
  p1 = 1
  p2 = int((number%8)//4)
  p3 = int((number%4)//2)
  p4 = int(number%2)
  return p1, p2, p3, p4

#Get user input for an integer between 8 and 15
number = int(input("Enter an integer between 8 and 15: "))