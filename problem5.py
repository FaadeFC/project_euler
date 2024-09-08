def divisible(x, n):
    """ Return True if x is divisible by 1 to n. """
    for i in range(1, n + 1):
        if x % i != 0:
            return False
    
    return True

def main():
    """ Execute the main program. """
    x = 1

    while True:
        if divisible(x, 20):
            break

        x += 1
    
    print(x)

main()