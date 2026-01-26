from algorithms import Algorithms
from list_generation import Gen
from time import time

# Configuration
length = 10000
unique_elements = 100
random_elements = 100

# Generate test data
generation_methods = [
    Gen.random(length),
    Gen.random_narrow(length, unique_elements),
    Gen.random_semi(length, random_elements),
    Gen.sorted_reverse(length)
]

# All sorting algorithms to test (bubble_sort removed as requested)
sorting_methods = [
    Algorithms.selection_sort,
    Algorithms.insertion_sort,
    Algorithms.merge_sort,
    Algorithms.quicksort,
    Algorithms.heapsort,
    Algorithms.introsort,
    Algorithms.radix_sort,
    Algorithms.counting_sort,
    Algorithms.timsort,
    Algorithms.adaptive_sort,
    sorted  # Python's built-in for comparison
]

sorting_titles = [
    "Selection Sort",
    "Insertion Sort", 
    "Merge Sort",
    "Quicksort",
    "Heapsort",
    "Introsort",
    "Radix Sort",
    "Counting Sort",
    "Timsort",
    "Adaptive Sort",
    "Python sorted()"
]

generation_titles = ["Random", "Few Unique", "Semi Sorted", "Sorted Reverse"]

# Run benchmarks
print("=" * 70)
print("SORTING ALGORITHM BENCHMARKS")
print("=" * 70)
print("Array size:", length, "elements | Iterations per test: 3")
print()

sorting_overview = []

for i in range(len(generation_methods)):
    sorting_times = [[] for _ in range(len(sorting_methods))]
    unsorted_data = generation_methods[i]
    print("Testing:", generation_titles[i], "data...")
    
    for j in range(len(sorting_methods)):
        for k in range(3):
            start_time = time()
            result = sorting_methods[j](unsorted_data[:])
            end_time = time()
            sorting_times[j].append((end_time - start_time) * 1000)
        
        avg_time = sum(sorting_times[j]) / len(sorting_times[j])
        sorting_times[j] = avg_time
        
    sorting_overview.append(sorting_times)

# Print detailed results
print()
print("=" * 70)
print("RESULTS (milliseconds, lower = better)")
print("=" * 70)

for j in range(len(generation_titles)):
    print()
    print(generation_titles[j], "Data:")
    print("-" * 40)
    
    # Sort by time for this data type
    results = [(sorting_overview[j][i], sorting_titles[i]) for i in range(len(sorting_titles))]
    results.sort()
    
    for time_val, name in results:
        marker = " <-- BEST" if time_val == results[0][0] else ""
        print("  {:.<25} {:>10.3f}ms{}".format(name, time_val, marker))

# Summary: Best algorithm per data type
print()
print("=" * 70)
print("BEST PURE-PYTHON ALGORITHM FOR EACH DATA TYPE")
print("=" * 70)

for j in range(len(generation_titles)):
    # Exclude Python's sorted() from our algorithms
    our_times = [(sorting_overview[j][i], sorting_titles[i]) for i in range(len(sorting_titles) - 1)]
    best_time, best_algo = min(our_times)
    python_time = sorting_overview[j][-1]
    
    if best_time <= python_time:
        status = "MATCHES/BEATS Python!"
    else:
        ratio = best_time / python_time
        status = str(round(ratio, 1)) + "x slower than C-Python"
    
    print(generation_titles[j] + ": " + best_algo)
    print("  -> " + str(round(best_time, 2)) + "ms vs Python's " + str(round(python_time, 2)) + "ms (" + status + ")")

print()
print("=" * 70)
print("NOTES")
print("=" * 70)
print("- Python's sorted() uses Timsort implemented in C (10-100x faster)")
print("- Radix Sort: Best for random integers with large range")
print("- Counting Sort: Best for data with few unique values")  
print("- Adaptive Sort: Auto-selects algorithm based on data characteristics")
print("- For sorted/reverse sorted data, Adaptive Sort uses O(n) detection")
