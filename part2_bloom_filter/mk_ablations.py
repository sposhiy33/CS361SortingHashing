"""
Optional script to run ablations on the bloom filter.
Variables:
    1. m: bit array size
    2. k: hash count

requires seaborn and matplotlib to be installed (heatmap plot)
"""

import os
import seaborn as sns
from password_checker import password_checker
import matplotlib.pyplot as plt


if __name__ == "__main__":

    hash_file = "test_cases/50kPasswords.txt"
    acceptable_error_rate = 0.01

    m = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
    k = [1,2,3,4,5,6,7,8,9,10]

    m_results = []
    # compare bloom filter performance with different m and k values
    for m_value in m:
        checker = password_checker(hash_file, acceptable_error_rate, m_value, None)
        false_positive_rate = checker.test_false_positive_rate()
        m_results.append(false_positive_rate)

    k_results = []
    for k_value in k:
        checker = password_checker(hash_file, acceptable_error_rate, None, k_value)
        false_positive_rate = checker.test_false_positive_rate()
        k_results.append(false_positive_rate)

    # plot m results
    plt.plot(m, m_results)
    plt.xlabel('m')
    plt.ylabel('false positive rate')
    plt.title('m vs false positive rate')
    plt.show()

    # plot k results
    plt.plot(k, k_results)
    plt.xlabel('k')
    plt.ylabel('false positive rate')
    plt.title('k vs false positive rate')
    plt.show()