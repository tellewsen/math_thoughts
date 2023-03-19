import random
from matplotlib import pyplot as plt


def play():
    has_not_lost = True
    score = 0
    while has_not_lost:
        die = random.randint(1, 6)
        if die == 1:
            return score
        score += die


def main():
    n = 1_000_000
    score_dict = {}
    for _ in range(n):
        score_at_loss = play()
        try:
            score_dict[score_at_loss] += 1
        except KeyError:
            score_dict[score_at_loss] = 1

    # stuff it into a plotable datastructure
    score_tuples = []
    for k, v in score_dict.items():
        score_tuples.append((k, v))
    scores = sorted(score_tuples)
    score = []
    count = []
    for k, v in scores:
        score.append(k)
        count.append(v)

    # cumulative count is more interesting
    cumulative_count = []
    for i in range(len(count)):
        cumulative_count.append(sum(count[i:]) / n)

    plt.figure(1)
    plt.xlabel("Score")
    plt.ylabel("Probability of getting this score or higher")
    plt.title(f"Simulation of {n} games")
    plt.plot(score, cumulative_count, "o")
    plt.savefig(f"result_{n}_games.png")

    # Weigh score by probability to assess how high a score is worth risking
    cumulative_count_weighted = []
    for i in range(len(score)):
        cumulative_count_weighted.append(score[i] * cumulative_count[i])
    plt.figure(2)
    plt.xlabel("Score")
    plt.ylabel("Probability of getting this score or higher weighted by score")
    plt.title(f"Weighted probabilities")
    plt.plot(score, cumulative_count_weighted)
    plt.show()
    # plt.savefig(f"weighted_result_{n}_games.png")


if __name__ == "__main__":
    main()
