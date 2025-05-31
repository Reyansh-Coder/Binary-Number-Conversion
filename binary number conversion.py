# Decimal to Binary using nested loop

# Input from user
decimal = int(input("Enter a decimal number: "))

# Store binary digits
binary = ""

# Outer loop (only runs once, for demonstration of nesting)
for i in range(1):  
    num = decimal

    # Inner loop to convert to binary
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

# If input was 0
if decimal == 0:
    binary = "0"

print("Binary number:", binary)
