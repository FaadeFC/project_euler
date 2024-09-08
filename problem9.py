def triplet(a, b, c):
    """ Return True if the three numbers is a Pythagorean triplet. """
    answer1 = a ** 2 + b ** 2
    answer2 = c ** 2
    return answer1 == answer2

def summation(n):
    """ Return the value of a, b, and c that sum up to 1000. """
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a + b + c == n and triplet(a, b, c):
                    return (a, b, c)

def main():
    """ Execute the main program. """
    n = 1000
    (a, b, c) = summation(n)
    product = a * b * c
    print(f"The answer is ({a}, {b}, {c}) with a product of {product}")

main()