class Algorithms:

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
        
        for i in range(len(sorted_data)-1):
            min_index = i
            for j in range(i, len(sorted_data)):
                if(sorted_data[i]> sorted_data[j]):
                    min_index = j
            temp = sorted_data[i]
            sorted_data[i] = sorted_data[j]
            sorted_data[j] = temp
        return sorted_data    
    def insertion_sort(unsorted_data):
        sorted_data = unsorted_data
        
        for i in range(1, len(sorted_data)):
            element = sorted_data[i]
            key = i
          
            for j in range(i-1, -1, -1):
                if(sorted_data[j] > element):
                    sorted_data[j+1] = sorted_data[j] 
                    key-=1
                else:
                    break
            sorted_data[key] = element
        return sorted_data