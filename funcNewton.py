
#function for Newton's 1D method
def funcNewton(f, x, dx = 0.0000001, tol = 0.0000001):
    """
    f - the function f(x)
    x - initial guess
    dx - small change to find derivative
    tol - tolerance to estimate the root

    returns the root of the given function using Newton's formula.
    """
    df = (f(x+dx) - f(x)) / dx  #find the derivative of function f at x
    while True:
        x1 = x - f(x)/df        #Newton's formula to find the root
        t = abs(x1 - x)
        if t < tol:             #If t is less than the tolerance value, come out of the loop.
            break
        x = x1                  #else continue this procedure until t is less than tolerance.
    return  round(x1,6)         #return the root reduced to 6 decimal places


#1st test
fx = lambda x : 3 * x ** 2 - 3  #define the function
print(funcNewton(fx,2))         #call the function and print the root

#2nd test
fx = lambda x : 5 * x ** 2 - 9 * x - 2  #define the function
print(funcNewton(fx,4))                 #call the function and print the root

#3rd test
fx = lambda x : 3 * x ** 3 - 9 * x ** 2 - 2 * x + 6     #define the function
print(funcNewton(fx,3))                                 #call the function and print the root

#4th test
fx = lambda x : 9 * x ** 2 - 1  #define the function
print(funcNewton(fx,1))         #call the function and print the root

#5th test
fx = lambda x : 5 * x ** 4 - 2      #define the function
print(funcNewton(fx,5))             #call the function and print the root

