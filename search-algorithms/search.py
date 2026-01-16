def linear_search(data, search):
    for i in range(len(data)):
        if search == data[i]:
            return i
def binary_search(data,search):
    data = sorted(data)
    index = len(data)/2
    index_2 = len(data)
    while True:
        
        if data[index] == search:
            return index
        
        if(data[index] < search):
            pass
        