# Function converting from imperial to metric
def imperialToMetric(stones, pounds):
    kg = round((stones*14 + pounds)/2.2, 1)
    return kg 

# Get user input for stones and pounds
stones = int(input("Enter number of stones: "))
pounds = int(input("Enter number of pounds: "))
print(imperialToMetric(stones, pounds))

# Function converting from metric to imperial
def metricToImperial(kilograms):
    st = round((kilograms*2.2)//14, 0)
    lbs = round((kilograms*2.2)%14, 0)
    return st, lbs

# Get user input for kilograms
kilograms = float(input("Enter number of kilograms: "))
print(metricToImperial(kilograms))
