# Write code for algorithm 5 below
def is_palindrome(input_str):
    print(f"current input string: {input_str}")
    if len(input_str) <= 1:
        return True
    else:
        return (input_str[0] == input_str[-1] and is_palindrome(input_str[1:-1]))

print("Is tacocat a palindrome")
print(is_palindrome("tacocat"))

