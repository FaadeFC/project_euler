from math import sqrt

def triangular(n):
    """ Return the nth triangular number. """
    answer = n * (n + 1) / 2
    answer = int(answer)
    return answer

def divisors(n):
    """ Return the number of factors that n has. """
    total = 0

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if sqrt(n) == i:
                total += 1
            else:
                total += 2
    
    return total

def main():
    """ Execute the main program. """
    i = 1
    total = 0

    while total <= 500:
        number = triangular(i)
        total = divisors(number)
        i += 1
    
    print(number)

main()