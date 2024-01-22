

# Pseudocode
# 1. Create a multiplication calculator
# 2. Product must be under 1000
# 3. If the product is higher than 1000, return the sum


# Multiplication Calculator

while True:

# Making sure that the input for the first value only accepts integers
    first_value = input ("Enter your first integer:")
    
    if first_value.isdigit():
         first_value = int(first_value)
    else:
        print("Values must be numbers!")
        break

# Making sure that the input for the second value only accepts integers
    second_value = input ("Enter your second integer:")

    if second_value.isdigit():
            second_value = int(second_value)
    else:
         print("Values must be numbers!")

# Operators that will be used for the desired outcomes
    product = first_value * second_value
    sum = first_value + second_value

# Making sure that it prints the product if it's (< 1000) and the sum if it's (< 1000)
    if product < 1000:
        print(product)
        break
    else:
        print(sum)
        break

        
