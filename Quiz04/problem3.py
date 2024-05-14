import random
from itertools import permutations

def naive_shuffle(cards):
    shuffled_cards = cards[:]
    for i in range(len(shuffled_cards)-1):
        j = random.randint(0, len(shuffled_cards)-1)
        shuffled_cards[i], shuffled_cards[j] = shuffled_cards[j], shuffled_cards[i]
    return tuple(shuffled_cards)

def fisher_yates_shuffle(cards):
    shuffled_cards = cards[:]
    for i in range(len(shuffled_cards)-1, 0, -1):
        j = random.randint(0, i)
        shuffled_cards[i], shuffled_cards[j] = shuffled_cards[j], shuffled_cards[i]
    return tuple(shuffled_cards)

def count_combinations(shuffle_function, iterations):
    counts = {}
    for _ in range(iterations):
        shuffled_cards = shuffle_function([1, 2, 3, 4])
        counts[shuffled_cards] = counts.get(shuffled_cards, 0) + 1
    return counts

def print_counts(counts):
    for combination, count in counts.items():
        print(f"{combination}: {count}")

if __name__ == "__main__":
    iterations = 1000000
    print("Naive algorithm:")
    naive_counts = count_combinations(naive_shuffle, iterations)
    print_counts(naive_counts)

    print("Fisher–Yates shuffle:")
    fisher_yates_counts = count_combinations(fisher_yates_shuffle, iterations)
    print_counts(fisher_yates_counts)
