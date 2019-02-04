#function to get a character from the user
def getChar():
    
    """ () -> str
    returns the first character of the input string entered by the user.

    >>>getChar()
    Enter a character: a
    'a'
    >>>getChar()
    Enter a character: 100
    '1'
    
    """
    #get the input
    var = input("Enter a character: ")
    #return the first character of the input
    return var[0]


#function to convert character to its 8-bit binary equivalent
def char2bin(data):
    
    """ (str) -> list
    returns a list of 8 bits binary equivalent of the character data

    >>>char2bin('a')
    ['0', '1', '1', '0', '0', '0', '0', '1']

    """
    #save the binary equivalent of ASCII value of data in variable data_bin.
    data_bin = bin(ord(data))
    #add leading 0s' to make the length of the string 8, split data_bin string to list and return it.
    return list(ord(data_bin[2:].zfill(8)))


    
    
    
