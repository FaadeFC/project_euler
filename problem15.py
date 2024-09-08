# How many such routes are there through a 20 x 20 grid?
def grid(n):
    """ Return the number of routes in a n x n grid. """
    for i in range(n):
        for j in range(n):
            print(i, j)


def main():
    """ Execute the main program. """
    n = 2
    answer = grid(n)
    print(answer)

main()