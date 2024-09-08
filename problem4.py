def palindrome(n):
    """ Return True if n is a palindrome. """
    number = str(n)
    number_reverse = number[::-1]

    if number == number_reverse:
        return True
    else:
        return False

def main():
    """ Execute the main program. """
    number = 0

    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            check = palindrome(product)

            if check and product > number:
                number = product
    
    print(number)

main()