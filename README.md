# CS361 Sorting and Hashing

---

## Running the Merge Sort Algorithm

```
python3 part1_merge_sort/test_merge_sort.py
```

- **Test 1 – Correctness:** Validates sorting on 9 small hand-checkable arrays. Edge cases include duplicates, negatives, floats, and already-sorted/reverse-sorted inputs.
- **Test 2 – Performance Benchmark:** Times the sort on integer and float arrays from 2²⁰ to 2³⁰ elements. I/O time is excluded from all measurements.

---

## Running the Hashing Algorithm

The hashing algorithm is contained in `part2_bloom_filter.pyz` and the source code can be viewed under `part2_bloom_filter/`. Python must be installed to run the `.pyz` file *(requires Python 3.14.3)*.

**Run with either command:**

```
python part2_bloom_filter.pyz
python3 part2_bloom_filter.pyz
```

**This runs 4 testing methods:**

- Displays whether all indices are within bounds
- Verifies the hash is deterministic
- Reports the false positive rate
- Reports the average query time

Outputs `Done!` when finished.

---

