# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
numbers = {1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
           15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
           20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
           70: "seventy", 80: "eighty", 90: "ninety"}

def count(text):
    """ Return the number of characters in text excluding spaces. """
    text = text.replace(" ", "")
    length = len(text)
    return length

def expand(number):
    """ Return a list with number in expanded form. """
    number = str(number)
    length = len(number)
    expanded = []

    # Multiply the place value by a power of 10.
    for i in range(length):
        digit = number[i]
        digit = int(digit)
        digit *= 10 **(length - i - 1)
        expanded.append(digit)
    
    return expanded

def convert(n):
    """ Convert number into its word form. """
    number = expand(n)

    # Get all numbers less than 20.
    if n < 20:
        return numbers[n]
    
    # Get all numbers 20 through 99.
    elif n < 100:
        a = number[0]

        if n % 10 == 0:
            return numbers[a]
        else:
            b = number[1]
            return f"{numbers[a]} {numbers[b]}"
        
    # Get all numbers 100 through 999.
    elif n < 1000:
        a = number[0]
        b = number[1]
        c = number[2]

        if n % 100 == 0:
            return f"{numbers[a / 100]} hundred"
        elif b == 0:
            return f"{numbers[a / 100]} hundred and {numbers[c]}"
        elif b == 10:
            return f"{numbers[a / 100]} hundred and {numbers[b + c]}"
        elif c == 0:
            return f"{numbers[a / 100]} hundred and {numbers[b]}"
        else:
            return f"{numbers[a / 100]} hundred and {numbers[b]} {numbers[c]}"
    
    # Get one thousand.
    else:
        return "one thousand"

def main():
    """ Execute the main program. """
    n = 1000
    total = 0

    for x in range(1, n + 1):
        word = convert(x)
        total += count(word)
    
    print(total)

main()