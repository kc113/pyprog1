import copy

import time

start=time.clock()

"""start_state=[[1,2,3],[4,5,6],[7,8,0]]

goal_state=[[1,2,3],[0,4,5],[7,8,6]]"""

start_state=[[1,2,5],[3,4,0],[6,7,8]]

goal_state=[[0,1,2],[3,4,5],[6,7,8]]

def left_shift(pres_state):

    global count

    temp_state=copy.deepcopy(pres_state)

    for i in range(3):

        for j in range(3):

            if temp_state[i][j]==0 and j>0:

                    count=count+1

                    (temp_state[i][j-1],temp_state[i][j])=(temp_state[i][j],temp_state[i][j-1])

                    return temp_state

    return pres_state

def right_shift(pres_state):

    global count


    temp_state=copy.deepcopy(pres_state)

    for i in range(3):

        for j in range(3):

            if temp_state[i][j]==0 and j<2:

                    count+=1

                    (temp_state[i][j+1],temp_state[i][j])=(temp_state[i][j],temp_state[i][j+1])

                    return temp_state

    return pres_state

  

def upper_shift(pres_state):

    global count

    temp_state=copy.deepcopy(pres_state)

    for i in range(3):

        for j in range(3):

            if temp_state[i][j]==0 and i>0:

                count+=1

                (temp_state[i-1][j],temp_state[i][j])=(temp_state[i][j],temp_state[i-1][j])

            return temp_state

    return pres_state

def lower_shift(pres_state):

    global count

  

    temp_state=copy.deepcopy(pres_state)
    
    for i in range(3):

        for j in range(3):

            if temp_state[i][j]==0 and i<2:

                count+=1

                (temp_state[i+1][j],temp_state[i][j])=(temp_state[i][j],temp_state[i+1][j])

                return temp_state   

    return pres_state

class Node:

    def __init__(self,pres_state,parent,visited):

        self.pres_state=pres_state

        self.parent=parent

        self.visited=False

    def print_path(pres_node):

        l=[]

        while pres_node.parent != None:
            
            l.append(pres_node.pres_state)
            
            pres_node=pres_node.parent
            
            l.reverse()

        for i in range(len(l)):


                print(l[i])

                nodes=[]

                nodes.append(Node(start_state,None,False))

                big_list=[]

                big_list.append(start_state)

    def bfs(pres_state,goal_state):

        global count

        count=0

        finish=False

        nodes[0].visited=True

        while finish==False:

            pres_node=nodes[0]

            nodes.remove(nodes[0])

            print (pres_node.pres_state)

    #print nodes

        for i in range(len(nodes)):

            if nodes[i].pres_state==any(big_list):

                nodes.remove(nodes[i])

            if pres_node.pres_state==goal_state:

                print (start_state)

            print_path(pres_node)

        finish=True

        left_node=Node(left_shift(pres_node.pres_state),pres_node,False)

        right_node=Node(right_shift(pres_node.pres_state),pres_node,False)

        upper_node=Node(upper_shift(pres_node.pres_state),pres_node,False)

        lower_node=Node(lower_shift(pres_node.pres_state),pres_node,False)

        neighbours=[left_node,right_node,upper_node,lower_node]

        for i in range(len(neighbours)):

            big_list.append(neighbours[i].pres_state)  

            for j in range(len(nodes)):

                for k in range(len(neighbours)):

                    if neighbours[k].pres_state==nodes[j].pres_state or neighbours[k].pres_state==pres_node.pres_state:

    #nodes.append(neighbours[k])

                        neighbours[k].visited=True

      

        for i in range(len(neighbours)):

            if neighbours[i].visited==False:

                neighbours[i].visited=True

                nodes.append(neighbours[i])

      
obj = Node

obj.bfs(start_state,goal_state)   

print ("time_taken=",time.clock()-start)

print ("no of nodes:",count)
