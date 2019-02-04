#Get the input as string from the user
input_string = input('Enter the list of 1s and 0s separated by space: ')
#convert it into a list
input_list = input_string.split()
#Get the number of positions to shift the contents of the list
num = int(input("Enter the number of positions to shift the contents of the list: "))
#number should be a positive integer
assert (num > 0)

def rightShift(lst,n):
    
    """ (list,int) -> None
    modifies the list by performing right shift by n bits
    >>>rightShift([1,0,1,0],2)
    1110
    >>>>rightShift([0,1,1,0],2)
    0001
    """
    
    #If the shift amount is greater than or equal to the length of the list of bits, the function returns without doing anything. 
    if n >= len(lst):
        return
    else:
        #save the left most bit
        temp = lst[0] 
        #remove n bits
        for i in range(n):
            lst.pop()
        #insert n copies of the first bit at position 0
        for i in range(n):
            lst.insert(i,temp)
        #print the list
        for i in range(len(lst)):
            print (lst[i],end = " ")
        

#call the function
rightShift(input_list,num)


        
