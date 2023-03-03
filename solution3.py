# Write code for algorithm 3 below
def nth_fibonacci(num):
    if num <= 0:
        print("Can't do a fibonacci number for zero")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return nth_fibonacci(num - 1) + nth_fibonacci (num - 2)

print("Fib: 4")        
print(nth_fibonacci(4))

