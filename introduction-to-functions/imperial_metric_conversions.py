# Function converting from imperial to metric
def imperialToMetric(stones, pounds):
    kg = (stones*14 + pounds)/2.2
    return kg 

# Get user input for stones and pounds
stones = int(input("Enter number of stones: "))
pounds = int(input("Enter number of pounds: "))
print(imperialToMetric(stones, pounds))

