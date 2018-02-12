"""
Gradient Descent to find min of:
f(x1,y1) = 1.5*x1**2+x2**2-2*x1*x2+2*x1**3+0.5*x1**4
Steven Yen
2018/02/11
"""

import numpy as np

def myFunction(x1,x2):
    return 1.5*x1**2+x2**2-2*x1*x2+2*x1**3+0.5*x1**4

def dfdx1(x1,x2):
    return 3*x1-2*x2+6*x1**2+2*x1**3

def dfdx2(x1,x2):
    return 2*x2-2*x1

def combinedFun(x1,x2):
    return [x1, x2, myFunction(x1,x2),dfdx1(x1,x2),dfdx2(x1,x2)]

#print combinedFun(1,-3)
#print combinedFun(0.978,1.287)

lrate = 0.001294 #eta
theta =  0.1 #error rate

maxIterations = 1000

def findMin(x1i,x2i):
    toExit = False
    iterations = 0  # number of iterations

    np.set_printoptions(precision=3)
    while(not toExit):

        print (np.array([x1i, x2i, myFunction(x1i, x2i), dfdx1(x1i,x2i),dfdx2(x1i,x2i)]))
        x1i = x1i-lrate*dfdx1(x1i,x2i)
        x2i = x2i-lrate*dfdx2(x1i,x2i)

        #magnitute of derivative
        gradFmag = ((dfdx1(x1i,x2i)**2+ dfdx2(x1i,x2i)**2))**0.5
        if(gradFmag<theta):
            #print("exit condition 1")
            toExit = True

        iterations = iterations+1
        if(iterations>maxIterations):
            #print("exit condition 2")
            toExit = True

print("starting guess (x10,x20) = (1,-3)")
findMin(1,-3)

