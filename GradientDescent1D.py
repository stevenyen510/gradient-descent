"""
Gradient Descent to find min of: f(x) = x**2-4
Steven Yen
2018/02/11
"""

def fsim(x):
    return x**2-4

def dfsimdx(x):
    return 2*x

lrate = 0.25 #eta
theta =  0.01 #error rate
i = 0 #number of iterations
maxIterations = 100;

def findMin(xi):
    toExit = False
    while(not toExit):
        xi = xi-lrate*dfsimdx(xi)
        print(xi)
        if(abs(dfsimdx(xi))<theta):
            toExit = True
            print("final value",xi)

print('starting guess at x0=5')
findMin(5)


