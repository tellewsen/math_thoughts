"""
When looking at numbers, som numbers are more "pleasing" to look at 
than others. 

For instance, 112233 "looks better" than 81241. How many of the numbers
between 0 and some large number are "pleasing"?

Which patterns make numbers more "pleasing"?

TODO: Look at the list of numbers less than 10k/100k that are not
classified as pleasing and add a check for them
"""


def is_symmetric(num: int) -> bool:
    """
    1221,13431 etc.
    """
    strnum = str(num)
    length = len(strnum)
    for i in range(int(length / 2)):
        if strnum[i] != strnum[length - 1 - i]:
            return False
    return True


def is_descending(num: int) -> bool:
    """
    Each digit goes down by the same amount

    987,975,963,951,876,864,852 etc.
    """
    if num < 100:
        return False
    strnum = str(num)
    step = int(strnum[0]) - int(strnum[1])
    if step < 0:
        return False
    for i in range(1, len(strnum) - 1):
        if int(strnum[i]) - int(strnum[i + 1]) != step:
            return False
    return True


def is_ascending(num: int) -> bool:
    """
    Each digit goes up by the same amount

    123,135,147,159,234,246,258,345,357,369 etc.
    """
    if num < 100:
        return False
    strnum = str(num)
    step = int(strnum[1]) - int(strnum[0])
    if step < 0:
        return False
    for i in range(1, len(strnum) - 1):
        if int(strnum[i + 1]) - int(strnum[i]) != step:
            return False
    return True


def is_pleasing(num: int) -> bool:
    return is_symmetric(num) or is_ascending(num) or is_descending(num)


def main() -> None:
    N = 10000
    pleasing = set()
    not_pleasing = set()
    for i in range(10, N):
        pleasing.add(i) if is_pleasing(i) else not_pleasing.add(i)
    n_pleasing = len(pleasing)
    print("Pleasing: ", sorted(pleasing))
    print("Pleasing ratio: ", "{:.2%} ({} of {})".format(n_pleasing / N, n_pleasing, N))
    # print("not pleasing: ", not_pleasing)


if __name__ == "__main__":
    main()
