def main():
    """ Execute the main program. """
    n = 100
    a = n * (n + 1) / 2
    b = n * (n + 1) * (2 * n + 1) / 6
    answer = a ** 2 - b
    answer = int(answer)
    print(answer)

main()