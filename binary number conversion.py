# Converting A Decimal to Binary Number

# Input from user
decimal = int(input("Enter a decimal number: "))

# Storing binary digits
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
