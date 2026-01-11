class Algorithms:

    def bubble_sort(unsorted_data):
        sorted_data = unsorted_data
        
        for i in range(len(sorted_data)-1):
            for j in range(len(sorted_data)-1-i):
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
    def merge_sort(unsorted_data):
        if (len(unsorted_data) <= 1):
            return unsorted_data
        
        left_data = unsorted_data[:(len(unsorted_data)//2)]
        right_data = unsorted_data[(len(unsorted_data)//2):]

        left_sorted = Algorithms.merge_sort(left_data)
        right_sorted = Algorithms.merge_sort(right_data)
    
        return Algorithms.merge(left_sorted, right_sorted)
    def merge(left_data, right_data):
        left_index = 0
        right_index = 0
        sorted_data = []

        while (left_index < len(left_data) and right_index < len(right_data)):
            if(left_data[left_index] <= right_data[right_index]):
                sorted_data.append(left_data[left_index])
                left_index+=1
            else:
                sorted_data.append(right_data[right_index])
                right_index+=1
        
        while left_index < len(left_data):
            sorted_data.append(left_data[left_index])
            left_index += 1
    
        while right_index < len(right_data):
            sorted_data.append(right_data[right_index])
            right_index += 1

        return sorted_data
