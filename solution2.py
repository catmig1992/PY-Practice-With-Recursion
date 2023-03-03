# Write code for algorithm 2 below
def natural_numbers(to_number, from_number = 1):
    #print(f"Params for to_number {to_number}, from_number: {from_number}")
    if from_number > to_number:
        return
    else:
        print(from_number)
        natural_numbers(to_number, from_number +1)

natural_numbers(25)     

