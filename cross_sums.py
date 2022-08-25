"""
Is there some pattern to the cross sums of numbers?

Looks like a distribution I've seen before. Not exciting enough to
warrant any more checking 
"""
import argparse
from collections import defaultdict

from matplotlib import pyplot as plt


def cross_sum_regular(num: int) -> int:
    return sum(int(i) for i in str(num))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--numbers",
        help="Check every integer from 0 to n",
        type=int,
        default=1000,
    )
    args = parser.parse_args()
    N = args.numbers

    # calculate
    counts = defaultdict(int)
    for i in range(N):
        counts[cross_sum_regular(i)] += 1

    # plot
    sums, occurences = zip(*[(k, v / N) for k, v in counts.items()])
    plt.figure()
    plt.title(f"Cross sums of integers 0 to {N}")
    plt.ylabel("Occurences divied by N")
    plt.xlabel("Cross sum")
    plt.plot(sums, occurences, "o")
    plt.show()


if __name__ == "__main__":
    main()
