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

def main():
    """ Execute the main program. """
    limit = 10001
    count = 1
    n = 1
    
    while count <= limit: 
        if prime(n) == True:
            count += 1
        
        n += 1

    answer = n - 1 
    print(answer)

main()