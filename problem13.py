# Work out the first ten digits of the sum of the following one-hundred 50-digit number.
def number_input():
    """ Return a list of all of the numbers. """
    numbers = []
    f = open("problem13.txt")

    # Collect all of the numbers.
    for line in f:
        number = int(line)
        numbers.append(number)
    
    f.close()
    return numbers

def summation(n):
    """ Return the sum of the digits of n. """
    total = 0

    for x in n:
        x = int(x)
        total += x
    
    return total

def main():
    """ Execute the main program. """
    numbers = number_input()
    total = sum(numbers)
    answer = str(total)
    answer = answer[:10]
    print(answer)

main()