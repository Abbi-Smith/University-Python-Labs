#Function to calculate user's BMI
def bmiCalculator(weight, height):
    bmi = weight/height**2
    final_bmi = round(float(bmi),1)
    return final_bmi

#Get user input for weight and height
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in metres: "))
print(bmiCalculator(weight, height))
