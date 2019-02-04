import matplotlib.pyplot as plt
import math

def robotarm(theta1,theta2,l1,l2):
    """
    returns the position of the end point of the second link of robot arm.
    (float, float, int, int) -> list
    
    >>>robotarm(math.pi/8,math.pi/4,4,2)
    [4.46, 3.38]
    
    """

    #start point of the first link is the origin.
    [x1, y1] = [0, 0]
    #end point of the first link is [x2, y2].
    x2 = l1 * math.cos(theta1)
    y2 = l1 * math.sin(theta1)

    #end point of first link is start point of second link.
    #end point of second link is [x3, y3]
    x3 = x2 + (l2 * math.cos(theta1+theta2))
    y3 = y2 + (l2 * math.sin(theta1+theta2))
    #plot the robot arm.
    plt.plot([x1,x2,x3],[y1,y2,y3])
    plt.show()
    #return the position(rounded to 2 decimals) of the end point second link.
    return [round(x3,2), round(y3,2)]

#call the function and print the return value.
print(robotarm(math.pi/8,math.pi/4,4,2))
