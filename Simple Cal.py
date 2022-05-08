from statistics import mean, median
print("Simple calculator made in python")

while True:
    try:
        num1 = float(input("Enter Number 1: "))
        num2 = float(input("Enter Number 2: "))
        break
    except ValueError: 
        print("Only Numbers allowed, please try again")
        continue

print(f"Sum of both the numbers: {num1+num2}")
print(f"Difference of both the numbers: {num1-num2}")
print(f"Product of both the numbers: {num1*num2}")
print(f"Quotient of both the numbers: {num1/num2}")
print(f"Mean of both the numbers: {mean([num1, num2])}")
print(f"Median of both the numbers: {median([num1, num2])}")
