"""
This script is used to test the performance of the bloom filter on a dataset of passwords.
False positive rate, query time, and memory usage are tested on a held out set of passwords (the test set).

This file can be run as a standalone script to test the performance of the bloom filter, but mainly is meant to be imported as a module.

Run the __main__.py file to get comprehensive testing results and sanity checks.
"""

import sys
import tempfile
import time
from pathlib import Path

from bloom_filter import bloom_filter


class password_checker:

    def __init__(self, hash_file, acceptable_error_rate, m=None, k=None):

        # split into test and train sets
        self.split = 0.8
        self.train_set, self.test_set = self.split_data(hash_file)

        print(f"Train set size: {len(self.train_set)}")
        print(f"Test set size: {len(self.test_set)}")

        train_path = self._write_train_file(self.train_set)
        try:
            self.bloom_filter = bloom_filter(train_path, acceptable_error_rate, m, k)
        finally:
            train_path.unlink(missing_ok=True)


    def _write_train_file(self, train_lines):
        """
        Write the train set as a temporary file in order to provide the correect input for the bloom filter.
        """
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".txt", delete=False) as f:

            f.writelines(train_lines)
            path = Path(f.name)
        return path

    def split_data(self, hash_file):
        """
        Split the data into train and test sets.
        """
        path = Path(hash_file)
        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()
        split_at = int(len(lines) * self.split)
        return lines[:split_at], lines[split_at:]

    def check_password(self, password):
        """
        Check if the password is in the bloom filter.
        """
        return self.bloom_filter.check(password)

    def test_false_positive_rate(self):
        """
        Test the false positive rate of the bloom filter by checking how many
        passwords in the test set are falsely identified as being in the train set.
        """
        false_positives = 0
        for password in self.test_set:
            if self.bloom_filter.check(password.strip()):
                false_positives += 1

        rate = false_positives / len(self.test_set) * 100
        print(f"\nFalse positive rate: {rate}%")
        return rate

    def test_query_time(self):
        """
        Test the query time of the bloom filter by checking how 
        long it takes to check a sample of 1000 passwords in the test set.
        """
        # sample 1000 samples from the test set
        sample = self.test_set[:1000]

        # query time for each password in the test set
        start_time = time.perf_counter()
        for password in sample:
            self.bloom_filter.check(password.strip())
        end_time = time.perf_counter()

        elapsed = end_time - start_time
        avg_time = elapsed / len(sample)
        print(f"\nQuery time: {elapsed} seconds")
        print(f"Average query time: {avg_time} seconds")
        return elapsed, avg_time

    def test_memory_usage(self):
        """
        Test the memory usage of the bloom filter by comparing it to a traditional set.
        """
        # set up traditional set for comparison
        traditional_set = set(line.strip() for line in self.test_set)

        bloom_filter_memory = sys.getsizeof(self.bloom_filter.byte_array)
        traditional_set_memory = sys.getsizeof(traditional_set)
        print(f"\nBloom filter memory usage: {bloom_filter_memory} bytes")
        print(f"Traditional set memory usage: {traditional_set_memory} bytes")
        return bloom_filter_memory, traditional_set_memory


if __name__ == "__main__":
    hash_file = "test_cases/1MPasswords.txt"
    acceptable_error_rate = 0.01
    checker = password_checker(hash_file, acceptable_error_rate)
    checker.test_false_positive_rate()
    checker.test_query_time()
    checker.test_memory_usage()
    print("Done!")
