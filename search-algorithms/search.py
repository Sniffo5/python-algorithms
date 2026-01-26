def linear_search(data, search):
    for i in range(len(data)):
        if search == data[i]:
            return i


def binary_search2(data ,search):
    low = 0
    high = len(data) -1
    index = (high-low)//2
    
    while low <= high and high -1 != low:
        if data[index] == search:
            return index
        if data[index] < search:
            low = index
            index = (high+low)//2
        if data[index] > search:
            high = index
            index = (high-low)//2
    return -1
    

        
lista = [1,2,3,4,5,6,7,8,9,10]

print(linear_search(lista[:],5))
print(binary_search2(lista[:],0))
