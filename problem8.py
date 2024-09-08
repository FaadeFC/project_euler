def multiply(n):
    """ Multiply the digits in the string n. """
    product = 1

    for digit in n:
        digit = int(digit)
        product *= digit
    
    return product

def iterate(number, n):
    """ Return the digits and product of the greatest product. """
    maximum = 1
    maximum_digits = ""
    length = len(number)

    # Loop through all of the digits with a length of n.
    for i in range(length - n + 1):
        digits = number[i : i + n]
        product = multiply(digits)

        # Update the maximum number.
        if product > maximum:
            maximum_digits = digits
            maximum = product
    
    return maximum_digits, maximum


def main():
    """ Execute the main program. """
    f = open("problem8.txt")
    number = ""
    
    for line in f:
        number += line.strip()
    
    f.close()
    (digits, maximum) = iterate(number, 13)
    print(f"{digits} with product of {maximum}")

main()