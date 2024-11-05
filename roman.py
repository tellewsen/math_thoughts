def to_roman(num: int):
    """
    Convert integers to their roman numeral equivalent

    Only works for numbers up to 3999 due to the rule of only three of the same symbol.
    """
    if num > 3999:
        raise ValueError(
            f"Can't calculate value for {num}. Rules for roman numerals exclude values above 3999."
        )
    letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    lookupValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for i in range(len(letters)):
        while num >= lookupValues[i]:
            num -= lookupValues[i]
            result += letters[i]
    return result
