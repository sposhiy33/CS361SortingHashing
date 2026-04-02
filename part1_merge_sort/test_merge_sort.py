# ----------------------------------------------------------
# File:          test_merge_sort.py
# Description:   Three way merge sort benchmark, sizes 2²⁰–2³⁰, integers vs floats, exclude I/O time
# Author:        Rick Garcia
# Email:         rickwgarcia@unm.edu
# Date:          2026-04-02
# ----------------------------------------------------------

import time
import random
from three_way_merge import merge_sort

random.seed(42)

# Test 1: Correctness
print("TEST 1: Correctness")
print("-" * 38)

small_tests = [
    ([3, 1, 2],           [1, 2, 3]),
    ([9, 7, 5, 3, 1],     [1, 3, 5, 7, 9]),
    ([1],                 [1]),
    ([4, 4, 4, 4],        [4, 4, 4, 4]),
    ([2, 1],              [1, 2]),
    ([1.5, 0.5, 2.5],     [0.5, 1.5, 2.5]),
    ([-3, -1, -2],        [-3, -2, -1]),
    ([1, 2, 3, 4, 5],     [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1],     [1, 2, 3, 4, 5]),
]

for inp, expected in small_tests:
    arr = inp[:]
    if len(arr) > 1:
        merge_sort(arr, 0, len(arr) - 1)
    print(f"  {'PASS' if arr == expected else 'FAIL'}  {inp} -> {arr}")

# Test 2: Performance Benchmark
print()
print("TEST 2: Performance Benchmark (2^20 to 2^30)")
print("-" * 38)
print(f"{'Size':>12}  {'Int (s)':>10}  {'Float (s)':>10}")
print("-" * 38)

for exp in range(20, 31):
    n = 2 ** exp

    # Generate, sort, then delete before generating the next type
    # to avoid holding more than one large array in memory at a time
    random.seed(exp)
    arr = [random.randint(0, n) for _ in range(n)]
    t0 = time.perf_counter()
    merge_sort(arr, 0, n - 1)
    int_time = time.perf_counter() - t0
    del arr

    random.seed(exp)
    arr = [random.uniform(0.0, float(n)) for _ in range(n)]
    t0 = time.perf_counter()
    merge_sort(arr, 0, n - 1)
    float_time = time.perf_counter() - t0
    del arr

    print(f"{n:>12,}  {int_time:>10.4f}  {float_time:>10.4f}")
