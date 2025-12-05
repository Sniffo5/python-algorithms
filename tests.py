from algorithms import Algorithms
from list_generation import Gen

unsorted_data = Gen.random(100,1,500)

print(Algorithms.insertion_sort(unsorted_data[:]))