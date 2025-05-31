# Converting A Decimal to Binary Number

# Taking Input from User
decimal = int(input("Enter a decimal number: "))

# Storing Binary Digits
binary = ""

# Outer loop 
for i in range(1):  
    num = decimal

    # Inner Loop 
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

# If Input = 0 
if decimal == 0:
    binary = "0"

print("Binary Number:", binary)
