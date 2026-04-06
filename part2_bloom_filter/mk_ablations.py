"""
Optional script to run ablations on the bloom filter.
Grid search over:
    1. m: bit array size
    2. k: hash count

Plots false positive rate (%) as a heatmap.

Requires matplotlib and seaborn.
"""

import math

import matplotlib.pyplot as plt
import seaborn as sns
from password_checker import password_checker


if __name__ == "__main__":

    hash_file = "test_cases/50kPasswords.txt"
    acceptable_error_rate = 0.01

    m = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # rows = m, columns = k
    rates = []
    for m_value in m:
        row = []
        for k_value in k:
            checker = password_checker(hash_file, acceptable_error_rate, m_value, k_value)
            row.append(checker.test_false_positive_rate())
        rates.append(row)

    m_labels = [f"$10^{{{int(round(math.log10(v)))}}}$" for v in m]

    fig, ax = plt.subplots(figsize=(max(8, len(k) * 0.35), max(4, len(m) * 0.55)))
    sns.heatmap(
        rates,
        xticklabels=k,
        yticklabels=m_labels,
        ax=ax,
        cmap="viridis",
        annot=True,
        fmt=".3g",
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "false positive rate (%)"},
    )
    ax.set_xlabel("k (hash count)")
    ax.set_ylabel("m (bit array size)")
    ax.set_title("False positive rate: grid search over m and k")
    plt.tight_layout()
    plt.show()
