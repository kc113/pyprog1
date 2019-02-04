class conncomp:
    #constructor
    def __init__(self,file):
        

        self.filename = open(file,'r') #open the file

        self.nv = self.filename.readline() #read the number of vertices
        self.ne = self.filename.readline() #read the number of edges
        self.edgelist = self.filename.readlines() #read the edges
        print(self.edgelist)

        self.filename.close() #close the file

#create object
findcc = conncomp('text3.txt')

        
        
