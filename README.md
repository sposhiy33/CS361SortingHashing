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

Outputs `Done!` when finished.---

# For Team Members


---

## Report

https://www.overleaf.com/project/69cc4768c4219a8aef8b6f63

---


## Team Sign-Up

| Name | Code | Report Section |
|------|------|----------------|
| Rick | 3-way Merge Sort + benchmarking script (int & float timing) |  |
| Ethan | Hash functions (Phase 2) + Bloom Filter core (bit array, insert/query) |  |
| Shrey | Password checker (dataset loading, train/test splits) + Phase 5 analysis (false positive rate, memory, query timing) |  | 

---

## Contributing

All changes go through pull requests. Do **not** push directly to `main`.

### Workflow

1. **Clone the repo**
   ```bash
   git clone https://github.com/rickwgarcia/CS361SortingHashing.git
   cd CS361SortingHashing
   ```

2. **Create a branch** for your work
   ```bash
   git checkout -b your-name/feature-description
   # e.g. git checkout -b alex/merge-sort
   ```

3. **Make your changes**, then commit
   ```bash
   git add .
   git commit -m "Short description of what you did"
   ```

4. **Push your branch**
   ```bash
   git push origin your-name/feature-description
   ```

5. **Open a Pull Request** on GitHub into `main` and wait for review.




