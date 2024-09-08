# Which staring number, under one million, produces the longest chain?
def collatz(n, i=1):
    """ Return the length of sequence from the Collatz sequence. """
    if n == 1:
        return i
    elif n % 2 == 0:
        return collatz(n / 2, i + 1)
    else:
        return collatz(3 * n + 1, i + 1)

def chain(n):
    """ Return the longest chain with starting number under n. """
    number = maximum = 1

    for i in range(1, n):
        chain = collatz(i)

        if chain > maximum:
            maximum = chain
            number = i
    
    return number

def main():
    """ Execute the main program. """
    n = 1000000
    answer = chain(n)
    print(answer)

main()