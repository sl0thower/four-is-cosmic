names = {
    0: 'zero',
    1: 'one', 
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
    }

def number2name(number: int) -> str:
    """
    return the english name of an integer [0, 9999] as a string
    """
    n = number
    name = ""
    if n == 0:
        return names[0]
    if not isinstance(n, int) or (n < 0 or n > 9999):
        raise BaseException(f"no name for {n}")
    thousands = n // 1000
    if thousands > 0:
        name += names[thousands] + " " + names[1000]
        n = n - thousands * 1000
        if n > 0:
            name += ", "
    hundreds = n // 100
    if hundreds > 0:
        name += names[hundreds] + " " + names[100]
        n = n - hundreds * 100
        if n > 0:
            name += " "
    if n > 19:
        tens = n // 10
        name += names[tens * 10]
        n = n - tens * 10
        if n > 0:
            name += "-" + names[n]
    else:
        if n > 0:
            name += names[n]
    return name

def number2namecount(n: int) -> int:
    """
    return the number of letters in a number's name excluding spaces and
    commas
    """
    name = number2name(n)
    counter = 0
    for i in name:
        if i not in [" ","-",","]:
            counter += 1
    return counter