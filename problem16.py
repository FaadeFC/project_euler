# What is the sum of the digits of the number 2 ** 1000?
def power(b, n):
    """ Return b raised up to the n. """
    answer = b ** n
    return answer

def summation(n):
    """ Return the sum of the digits in n. """
    n = str(n)
    total = 0

    for x in n:
        x = int(x)
        total += x
    
    return total

def main():
    """ Execute the main program. """
    n = 1000
    number = power(2, n)
    answer = summation(number)
    print(answer)

main()