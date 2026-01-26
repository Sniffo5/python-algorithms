import math

class Algorithms:
    """
    A collection of sorting algorithms implemented in pure Python.
    Includes classic algorithms and optimized hybrid approaches.
    """

    # ==================== CLASSIC O(N^2) ALGORITHMS ====================
    # Best for very small arrays or teaching purposes.

    @staticmethod
    def bubble_sort(unsorted_data):
        """
        Bubble Sort: O(n^2)
        Repeatedly steps through the list, compares adjacent elements and swaps them
        if they are in the wrong order. "Bubbles" largest elements to the top.
        """
        sorted_data = unsorted_data[:] # Create copy
        n = len(sorted_data)
        
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if sorted_data[j] > sorted_data[j+1]:
                    sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
                    swapped = True
            if not swapped: # Optimization: Exit if no swaps occurred
                break
        return sorted_data

    @staticmethod
    def selection_sort(unsorted_data):
        """
        Selection Sort: O(n^2)
        Divides the list into a sorted and unsorted region. Repeatedly finds the
        minimum element from the unsorted region and moves it to the sorted region.
        """
        sorted_data = unsorted_data[:]
        n = len(sorted_data)
        
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if sorted_data[j] < sorted_data[min_index]:
                    min_index = j
            if min_index != i:
                sorted_data[i], sorted_data[min_index] = sorted_data[min_index], sorted_data[i]
        return sorted_data    

    @staticmethod
    def insertion_sort(unsorted_data):
        """
        Insertion Sort: O(n^2)
        Builds the sorted array one item at a time. Much less efficient on large
        lists than more advanced algorithms. Efficient for small data sets.
        """
        sorted_data = unsorted_data[:]
        Algorithms._insertion_sort_range(sorted_data, 0, len(sorted_data) - 1)
        return sorted_data

    @staticmethod
    def _insertion_sort_range(data, low, high):
        """Helper for range-based insertion sort (used in hybrid algorithms)."""
        for i in range(low + 1, high + 1):
            key = data[i]
            j = i - 1
            while j >= low and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key

    # ==================== EFFICIENT O(N log N) ALGORITHMS ====================

    @staticmethod
    def merge_sort(unsorted_data):
        """
        Merge Sort: O(n log n)
        Divide and conquer algorithm. Divides input array in two halves, calls itself
        for the two halves and then merges the two sorted halves. Stable sort.
        """
        if len(unsorted_data) <= 1:
            return unsorted_data
        
        mid = len(unsorted_data) // 2
        left_data = unsorted_data[:mid]
        right_data = unsorted_data[mid:]

        left_sorted = Algorithms.merge_sort(left_data)
        right_sorted = Algorithms.merge_sort(right_data)
    
        return Algorithms.merge(left_sorted, right_sorted)

    @staticmethod
    def merge(left_data, right_data):
        """Standard merge operation for Merge Sort."""
        result = []
        i = j = 0
        len_l, len_r = len(left_data), len(right_data)

        # Optimization: append to list is faster than index reassignment for dynamic lists
        while i < len_l and j < len_r:
            if left_data[i] <= right_data[j]:
                result.append(left_data[i])
                i += 1
            else:
                result.append(right_data[j])
                j += 1
        
        result.extend(left_data[i:])
        result.extend(right_data[j:])
        return result

    @staticmethod
    def quicksort(unsorted_data):
        """
        Quicksort: O(n log n) average
        Divide and conquer. Picks a 'pivot' and partitions the array into elements
        less than pivot and greater than pivot. Fast in practice but unstable.
        """
        data = unsorted_data[:]
        Algorithms._quicksort_helper(data, 0, len(data) - 1)
        return data

    @staticmethod
    def _quicksort_helper(data, low, high):
        # Optimization: Use iteration stack instead of recursion to avoid depth limits
        # and reduce function call overhead.
        stack = [(low, high)]
        
        while stack:
            low, high = stack.pop()
            if low >= high:
                continue
            
            # Optimization: Use insertion sort for small subarrays
            if high - low < 16:
                Algorithms._insertion_sort_range(data, low, high)
                continue

            # Median-of-three pivot selection
            mid = (low + high) // 2
            if data[low] > data[mid]: data[low], data[mid] = data[mid], data[low]
            if data[low] > data[high]: data[low], data[high] = data[high], data[low]
            if data[mid] > data[high]: data[mid], data[high] = data[high], data[mid]
            
            # Place pivot at high-1 (since we know high is >= pivot)
            pivot = data[mid]
            data[mid], data[high - 1] = data[high - 1], data[mid]
            
            i = low
            j = high - 1
            
            while True:
                i += 1
                while data[i] < pivot: i += 1
                j -= 1
                while data[j] > pivot: j -= 1
                
                if i >= j: break
                data[i], data[j] = data[j], data[i]
            
            # Restore pivot
            data[i], data[high - 1] = data[high - 1], data[i]
            
            # Push larger partition first to minimize stack usage
            if i - 1 - low > high - (i + 1):
                stack.append((low, i - 1))
                stack.append((i + 1, high))
            else:
                stack.append((i + 1, high))
                stack.append((low, i - 1))

    @staticmethod
    def heapsort(unsorted_data):
        """
        Heapsort: O(n log n)
        Uses a binary heap data structure. Guarantess O(n log n) time unlike Quicksort.
        Great for space complexity as it sorts in-place.
        """
        data = unsorted_data[:]
        n = len(data)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            Algorithms._heapify(data, n, i)
        
        # Extract elements
        for i in range(n - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            Algorithms._heapify(data, i, 0)
        return data

    @staticmethod
    def _heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and data[left] > data[largest]: largest = left
        if right < n and data[right] > data[largest]: largest = right
        
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            Algorithms._heapify(data, n, largest)

    @staticmethod
    def introsort(unsorted_data):
        """
        Introsort: O(n log n)
        Hybrid algorithm (Quicksort + Heapsort + Insertion Sort). Starts with Quicksort,
        switches to Heapsort if recursion depth gets too deep (preventing worst case),
        and uses Insertion Sort for small partitions.
        """
        data = unsorted_data[:]
        if len(data) <= 1: return data
        
        max_depth = 2 * (len(data).bit_length()) # Approx 2 * log2(n)
        Algorithms._introsort_helper(data, 0, len(data) - 1, max_depth)
        return data

    @staticmethod
    def _introsort_helper(data, low, high, depth_limit):
        size = high - low + 1
        if size < 16:
            Algorithms._insertion_sort_range(data, low, high)
            return
        if depth_limit == 0:
            Algorithms._heapsort_range(data, low, high)
            return
            
        # Partition (Quicksort step)
        mid = (low + high) // 2
        if data[low] > data[mid]: data[low], data[mid] = data[mid], data[low]
        if data[low] > data[high]: data[low], data[high] = data[high], data[low]
        if data[mid] > data[high]: data[mid], data[high] = data[high], data[mid]
        
        pivot = data[mid]
        data[mid], data[high - 1] = data[high - 1], data[mid]
        
        i = low
        j = high - 1
        while True:
            i += 1
            while data[i] < pivot: i += 1
            j -= 1
            while data[j] > pivot: j -= 1
            if i >= j: break
            data[i], data[j] = data[j], data[i]
            
        data[i], data[high - 1] = data[high - 1], data[i]
        
        Algorithms._introsort_helper(data, low, i - 1, depth_limit - 1)
        Algorithms._introsort_helper(data, i + 1, high, depth_limit - 1)

    @staticmethod
    def _heapsort_range(data, low, high):
        n = high - low + 1
        for i in range(n // 2 - 1, -1, -1):
            Algorithms._heapify_range(data, n, i, low)
        for i in range(n - 1, 0, -1):
            data[low], data[low + i] = data[low + i], data[low]
            Algorithms._heapify_range(data, i, 0, low)

    @staticmethod
    def _heapify_range(data, n, i, offset):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and data[offset + left] > data[offset + largest]: largest = left
        if right < n and data[offset + right] > data[offset + largest]: largest = right
        
        if largest != i:
            data[offset + i], data[offset + largest] = data[offset + largest], data[offset + i]
            Algorithms._heapify_range(data, n, largest, offset)

    # ==================== LINEAR TIME (O(N) / O(NK)) ALGORITHMS ====================

    @staticmethod
    def radix_sort(unsorted_data):
        """
        Radix Sort: O(nk)
        Non-comparative sorting algorithm. Sorts integers by processing individual digits.
        OPTIMIZED: Uses bitwise operations and base 256 for speed.
        """
        if not unsorted_data: return unsorted_data
        
        # Check if we need to handle negatives
        _min = min(unsorted_data)
        if _min < 0:
            # Shift all numbers to be positive for sorting, then shift back
            # This is O(n) and simpler than separate positive/negative implementations
            data = [x - _min for x in unsorted_data]
        else:
            data = unsorted_data[:]
            
        max_val = max(data)
        # Bit shifting optimization. base 256 checks 8 bits at a time.
        # This is significantly faster than division/modulus
        block_size = 8
        mask = (1 << block_size) - 1
        
        # Calculate number of passes needed
        passes = (max_val.bit_length() + block_size - 1) // block_size
        
        shift = 0
        for _ in range(passes):
            # Counting sort for the current byte
            buckets = [[] for _ in range(256)]
            for num in data:
                buckets[(num >> shift) & mask].append(num)
            
            # Flatten buckets
            data = []
            for bucket in buckets:
                data.extend(bucket)
            
            shift += block_size
            
        if _min < 0:
            data = [x + _min for x in data]
            
        return data

    @staticmethod
    def counting_sort(unsorted_data):
        """
        Counting Sort: O(n + k)
        Counts the number of objects having distinct key values.
        Extremely fast when the range of input (k) is not significantly greater than n.
        """
        if not unsorted_data: return unsorted_data
        
        _min = min(unsorted_data)
        _max = max(unsorted_data)
        
        # Fallback if range is too huge to prevent memory error/freezing
        if (_max - _min) > 2000000:
             return sorted(unsorted_data) # Or use Radix Sort
             
        range_val = _max - _min + 1
        count = [0] * range_val
        output = [0] * len(unsorted_data)
        
        for num in unsorted_data:
            count[num - _min] += 1
            
        for i in range(1, range_val):
            count[i] += count[i - 1]
            
        for i in range(len(unsorted_data) - 1, -1, -1):
            val = unsorted_data[i]
            output[count[val - _min] - 1] = val
            count[val - _min] -= 1
            
        return output

    # ==================== ADVANCED HYBRID ALGORITHMS ====================

    @staticmethod
    def timsort(unsorted_data):
        """
        Timsort: O(n log n)
        Adaptive hybrid algorithm (Merge Sort + Insertion Sort).
        This is a simplified pure-Python implementation of what Python uses internally.
        """
        min_run = 32
        n = len(unsorted_data)
        data = unsorted_data[:]
        
        for i in range(0, n, min_run):
            Algorithms._insertion_sort_range(data, i, min((i + 31), (n - 1)))
            
        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))
                if mid < end:
                    Algorithms._tim_merge(data, start, mid, end)
            size *= 2
            
        return data

    @staticmethod
    def _tim_merge(data, left, mid, right):
        # Optimization: Slicing is fast in Python
        left_part = data[left:mid + 1]
        right_part = data[mid + 1:right + 1]
        
        i = j = 0
        k = left
        len_l, len_r = len(left_part), len(right_part)
        
        while i < len_l and j < len_r:
            if left_part[i] <= right_part[j]:
                data[k] = left_part[i]
                i += 1
            else:
                data[k] = right_part[j]
                j += 1
            k += 1
            
        # Optimization: Bulk assignment if anything is left
        if i < len_l:
            data[k: right + 1] = left_part[i:]
        elif j < len_r:
            data[k: right + 1] = right_part[j:]

    @staticmethod
    def adaptive_sort(unsorted_data):
        """
        Adaptive Sort: The "Smart" Sorter.
        Analyzes the input data to select the theoretically optimal sorting strategy.
        Attempting to approach Python's C-based performance using pure Python tricks.
        """
        if not unsorted_data: return []
        n = len(unsorted_data)
        
        # 1. Very small arrays -> Insertion Sort
        if n < 64:
            return Algorithms.insertion_sort(unsorted_data)

        # 2. Check for already sorted or reverse sorted data (Linear scan)
        # Using a generator with next() is usually slower than a loop in Python for detailed checks,
        # but for simple monotonicity we can iterate efficiently.
        data = unsorted_data # Reference, don't copy yet
        
        # Check first 10 items to guess trend
        ascending = 0
        descending = 0
        limit = min(n, 20)
        for i in range(limit - 1):
            if data[i] <= data[i+1]: ascending += 1
            if data[i] >= data[i+1]: descending += 1
            
        # If strong trend detected, verify full array
        if ascending == limit - 1:
            # Check full sorted
            is_sorted = True
            for i in range(n - 1):
                if data[i] > data[i+1]:
                    is_sorted = False
                    break
            if is_sorted: return data[:]

        if descending == limit - 1:
            # Check full reverse
            is_reverse = True
            for i in range(n - 1):
                if data[i] < data[i+1]:
                    is_reverse = False
                    break
            if is_reverse: return data[::-1] # Fast slice reverse

        # 3. Check for Integer optimizations
        # We can peek at the first element to guess type
        if isinstance(data[0], int):
            # Check range
            _min = min(data)
            _max = max(data)
            _range = _max - _min
            
            # If range is small (e.g., student grades), Counting Sort is O(N)
            # Threshold: Range < N * 2 is a good heuristic
            if _range < n * 2:
                return Algorithms.counting_sort(unsorted_data)
            
            # If range is massive but N is also large, Radix Sort is O(N * log_base(Range))
            # which is better than O(N log N) comparison sort.
            # Bitwise Radix sort is extremely fast for integers.
            return Algorithms.radix_sort(unsorted_data)

        # 4. Fallback for generic objects or floats -> Timsort
        return Algorithms.timsort(unsorted_data)
