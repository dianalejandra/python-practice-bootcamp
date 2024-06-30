# Create a funtion that receives a list and returns a tuple with the even elements in that list
def list_converter():
    my_list = [1,2,3,4,5,6,7,8,9]
    for number in my_list:
        even_tuple = ()
        if(number % 2 == 0):
            even_tuple = number
            print(number)
            return number
        
    
    
