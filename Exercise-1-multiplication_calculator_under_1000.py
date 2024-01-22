

# Pseudocode
# 1. Create a multiplication calculator
# 2. Product must be under 1000
# 3. If the product is higher than 1000, return the sum


# Multiplication Calculator

while True:
    first_value = input ("Enter your first integer:")
    
    if first_value.isdigit():
         first_value = int(first_value)
    else:
        print("Values must be numbers!")
        break

    second_value = input ("Enter your second integer:")

    if second_value.isdigit():
            second_value = int(second_value)
    else:
         print("Values must be numbers!")

    product = first_value * second_value
    sum = first_value + second_value

        
