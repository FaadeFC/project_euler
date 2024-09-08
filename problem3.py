def main():
    """ Execute the main program. """
    primes = []
    i = 1
    x = 600851475143

    while x != 1:
        if x % i == 0:
            primes.append(i)
            x = x / i
        i += 1
    
    answer = max(primes)
    print(answer)

main()