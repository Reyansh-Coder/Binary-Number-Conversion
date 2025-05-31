# Convert a decimal number to binary using simple nested loops

decimal = int(input("Enter a decimal number: "))

# Find the highest power of 2 less than or equal to decimal
power = 0
while 2 ** power <= decimal:
    power += 1
power -= 1

binary = ""
for i in range(power, -1, -1):
    bit = 0
    temp = decimal
    # Nested loop to check if 2^i fits into the remaining number
    while temp >= 2 ** i:
        temp -= 2 ** i
        bit += 1
    binary += str(bit)
    decimal -= bit * (2 ** i)

print("Binary representation:", binary)

