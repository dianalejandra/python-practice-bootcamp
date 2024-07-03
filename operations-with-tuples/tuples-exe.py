# Create a funtion that receives a list and returns a tuple with the even elements in that list

def get_even_numbers_from_list(numList):
    new_list = []    
    for pair in numList:
        if (pair % 2 == 0):
            new_list.append(pair)
    return tuple(new_list)
            
numList = [1,2,3,4,5,6,7,8,9]
num_tuple = get_even_numbers_from_list(numList)
print(num_tuple)