# This code demonstrates the use of MODULES and PACKAGES

from simple_calculator import arithmetic

# Prompt user to enter two digits
num1 = float(input("Ievadiet pirmo skaitli: "))
num2 = float(input("Ievadiet otro skaitli: "))

# Perform simple operations (+, -, *, /)
sum_result = arithmetic.add(num1, num2)
difference_result = arithmetic.subtract(num1, num2)
product_result = arithmetic.multiply(num1, num2)
division_result = arithmetic.divide(num1, num2)

# Print results
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference_result}")
print(f"{num1} * {num2} = {product_result}")
print(f"{num1} / {num2} = {division_result}")