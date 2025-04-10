# Define the logic circuit
def logic_circuit(a, b, c):
    return (a & b) | c

# Example usage
a = 1
b = 0
c = 1

output = logic_circuit(a, b, c)
print("Last output:", output)
