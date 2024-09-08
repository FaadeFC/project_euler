from math import sqrt, floor

def prime(n):
    """ Return true if n is prime. """
    if n == 1:
        return False
    elif n < 4:
        return True
    else:
        b = floor(sqrt(n))

        for i in range(2, b + 1):
            if n % i == 0:
                return False
    
    return True

def summation(n):
    """ Return the sum of all of the primes below n. """
    total = 0

    for i in range(1, n):
        check = prime(i)

        if check:
            total += i
    
    return total

def main():
    """ Execute the main program. """
    n = 2000000
    answer = summation(n)
    print(answer)

main()