def rightmost_set_bit(num):
    if num == 0:
        return 0  # No set bits in 0
    return num & -num  # Isolate the rightmost set bit

# Take input from user
num = int(input("Enter a number: "))

# Get the rightmost set bit
result = rightmost_set_bit(num)

# Print the result
print("Rightmost set bit is:", result)
