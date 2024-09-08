def divisible(a, b):
    """ Return True if a is divisible by b. """
    remainder = a % b

    if remainder == 0:
        return True
    else:
        return False

def main():
    """ Execute the main program. """
    total = 0

    for x in range(1, 1000):
        check = divisible(x, 3) or divisible(x, 5)

        if check:
            total = total + x
    
    print(total)

main()