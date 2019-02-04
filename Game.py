

class ConwayGame:

        
    
    def emptyplane(self,x,y):
        
        """(int, int) -> (list)
        returns a 2-D list of x(horizontal) by y(vertical)
        initialized to value False in every cell.
        """
        
        #create 2D list of size x by y with False in every cell.
        plane = [[False] * x]*y
        #return the list
        return plane

    
    def printplane(self,plane):
        
        """(plane) -> None
        print the plane followed by a new line.
        True values are displayed by 'o' and
        False values are displayed by blank space.
        """
        #loop through the list to assign True value the char 'o' and False value the char ''.
        for i in range(len(plane)):
            for j in range(len(plane[0])):
                if plane [i] [j] == False:
                    print("x",end = "")
                elif plane [i] [j] == True:
                    print("o", end = "")
                else:
                    print("error")
            print()
        #print a new line.
        print("\n")

                
                                    
game = ConwayGame()
plane = game.emptyplane(5,6)
game.printplane(plane)


