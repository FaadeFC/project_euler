def main():
    """ Execute the main program. """
    a = 1
    b = 2
    total = 0

    while b <= 4000000:
        if b % 2 == 0:
            total = total + b
        (a, b) = (b, a + b)
    
    print(total)

main()