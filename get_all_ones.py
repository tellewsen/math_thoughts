import random
from time import time
import matplotlib.pyplot as plt


def throw_once(remaining):
    ones = 0
    for _ in range(remaining):
        if random.randint(1, 6) == 1:
            ones += 1
    return ones


def play_one_round(n_dice):
    n_throws = 0
    remaining = n_dice
    while remaining > 0:
        n_throws += 1
        remaining -= throw_once(remaining)
        if remaining == 0:
            break
    return n_throws


def main():
    n_rounds = 100000
    n_throws = 0
    n_dice = 6
    t1 = time()
    results = []
    for i in range(1, n_rounds + 1):
        n_throws += play_one_round(n_dice)
        results.append(n_throws / i)
    t2 = time()

    print(f"Average throws to get all ones: {n_throws/n_rounds}")
    print(f"Took {t2-t1} seconds")
    plt.figure()
    plt.plot(range(1, n_rounds + 1), results)
    plt.show()


if __name__ == "__main__":
    main()
