# Write code for algorithm 4 below
def a_to_b(a, b):
    print(f"a: {a}, b: {b}")
    if b < 1:
        print("The exponent must be greater than 1")
    elif b == 1:
        return a
    else:
        return a * a_to_b(a, b-1)

print(f"The power result is {a_to_b(2, 4)}")

