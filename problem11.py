def number_input():
    """ Return a list of lists containing all of the numbers. """
    matrix = []
    f = open("problem11.txt")

    # Collect the numbers as rows.
    for line in f:
        numbers = line.split()
        numbers = list(map(lambda x: int(x), numbers))
        matrix.append(numbers)

    f.close()
    return matrix

def rows(matrix, n):
    """ Return the maximum product of n digits for rows. """
    maximum = 1
    length = len(matrix)

    for i in range(length):
        for j in range(length - n + 1):
            product = 1

            # Checks the product for each row.
            for k in range(n):
                product *= matrix[i][j + k]

                if product > maximum:
                    maximum = product
    
    return maximum

def columns(matrix, n):
    """ Return the maximum product of n digits for columns. """
    maximum = 1
    length = len(matrix)

    for i in range(length - n + 1):
        for j in range(length):
            product = 1

            # Checks the product for each column.
            for k in range(n):
                product *= matrix[i + k][j]

                if product > maximum:
                    maximum = product
    
    return maximum

def diagonal_down(matrix, n):
    """ Return the maximum product of n digits for diagonals going down. """
    maximum = 1
    length = len(matrix)

    for i in range(length - n + 1):
        for j in range(length - n + 1):
            product = 1

            # Checks the product for each diagonal down.
            for k in range(n):
                product *= matrix[i + k][j + k]

                if product > maximum:
                    maximum = product
    
    return maximum

def diagonal_up(matrix, n):
    """ Return the maximum product of n digits for diagonals going up. """
    maximum = 1
    length = len(matrix)

    for i in range(length - n + 1):
        for j in range(length - n + 1):
            product = 1

            # Checks the product for each diagonal up.
            for k in range(n):
                product *= matrix[i + n - k - 1][j + k]

                if product > maximum:
                    maximum = product
    
    return maximum

def main():
    """ Execute the main program. """
    n = 4
    matrix = number_input()
    product1 = rows(matrix, n)
    product2 = columns(matrix, n)
    product3 = diagonal_down(matrix, n)
    product4 = diagonal_up(matrix, n)
    answer = max(product1, product2, product3, product4)
    print(answer)

main()