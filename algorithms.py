class Algorithms:
    __reiterations = 100000
    
    def bubble_sort(unsorted_data):
        sorted_data = unsorted_data
        
        for i in range(len(sorted_data)-1):
            for j in range(len(sorted_data)-1):
                if sorted_data[j] > sorted_data[j+1]:
                    temp = sorted_data[j]
                    sorted_data[j] = sorted_data[j+1]
                    sorted_data[j+1] = temp
        return sorted_data
    def selection_sort(unsorted_data):
        sorted_data = unsorted_data
        smallest_number_position = 0
        
        for i in range(len(sorted_data)-1):
            for j in range(i, len(sorted_data)-1):
                if(sorted_data[smallest_number_position] > sorted_data[j]):
                    smallest_number_position = j
            temp = sorted_data[i]
            sorted_data[i] = sorted_data[smallest_number_position]
            sorted_data[smallest_number_position] = temp 
            
        return sorted_data
    def insertion_sort(unsorted_data):
        pass

unsorted_data = [4,7,9,3,2,8,1,5,6,0]

print(Algorithms.bubble_sort(unsorted_data))
print(Algorithms.selection_sort(unsorted_data))