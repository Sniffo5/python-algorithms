from algorithms import Algorithms
from list_generation import Gen
from time import time
import math
length = 10000
unique_elements = 100
random_elements = 100

generation_methods = [Gen.random(length),Gen.random_narrow(length,unique_elements),Gen.random_semi(length, random_elements ),Gen.sorted_reverse(length)]
sorting_methods = [Algorithms.bubble_sort,Algorithms.selection_sort,Algorithms.insertion_sort,Algorithms.merge_sort, sorted]

sorting_overview = []

for i in range(len(generation_methods)):
    sorting_times = [[],[],[],[],[]]
    unsorted_data = generation_methods[i]
    for j in range(len(sorting_methods)):
        for k in range(3):
            start_time = time()
            sorting_methods[j](unsorted_data[:])
            end_time = time()
            sorting_times[j].append((end_time-start_time)*1000)
        sorting_times[j] = sum(sorting_times[j])/len(sorting_times[j])
    sorting_overview.append(sorting_times)
    
sorting_titles = ["Bubble Sort", "Selection Sort", "Insertion Sort","Merge Sort", "Python Sort"]
generation_titles = ["Random", "Few Unique", "Semi Sorted", "Sorted Reverse"]

table = "\t\t\t"

for i in range(len(generation_titles)):
    table += generation_titles[i]
    if (i < 1):
        table += "\t\t\t\t"
    else:
        table += "\t\t\t"

for i in range(len(sorting_titles)):
    table += "\n"
    table += sorting_titles[i]
    for j in range(len(sorting_overview)):
        table += "\t\t"
        table += str(sorting_overview[j][i])
        

print(table)
