import random

class Gen:
    def random(len, min = 1, max= 20000000):
        return(random.sample(range(min,max),len))
        
    def random_semi(len, randomness):
        lista = list(range(1,len))
        for i in range(randomness+1):
            lista[random.randrange(len-1)] = lista[random.randrange(len-1)]
        return lista
    
    def random_narrow(len,unique):
        unique_list = list(range(0,unique))
        return(random.choices(unique_list,k=len))
        
    def sorted_reverse(len):
        return(list(range(len, 0, -1)))