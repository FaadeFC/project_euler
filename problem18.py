# Find the maximum total from top to bottom of the triangle below.
def number_input():
    """ Return a list of lists containing the pyramid. """
    matrix = []
    f = open("problem18test.txt")

    # Collect the numbers as rows.
    for line in f:
        numbers = line.split()
        numbers = list(map(lambda x: int(x), numbers))
        matrix.append(numbers)
    
    f.close()
    return matrix

def trace(matrix):
    """ Returns the maximum total from top to bottom of the triangle. """
    length = len(matrix)
    total = matrix[0][0]
    j = 0

    # Checks which number is bigger for each row.
    for i in range(1, length):
        number1 = matrix[i][j]
        number2 = matrix[i][j + 1]

        if number1 > number2:
            total += number1
        else:
            total += number2
            j += 1
    
    return total

def main():
    """ Executes the main program. """
    matrix = number_input()
    answer = trace(matrix)
    print(answer)

main()