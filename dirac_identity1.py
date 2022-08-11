

#Dirac identity

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.exp(b**2/(4*a)+c)
def d(x):
    return np.exp((-a)*(x-(b/2*2))**2)*f(x)

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
X=np.pi-50
Y=np.pi+50

x=np.arange(X,Y,0.1)
RHS=np.sqrt(np.pi/a)*np.exp(b**2/(4*a)+c)
LHS=(quad(lambda x:d(x),X,Y)[0])

print("RHS: ",RHS)
print("LHS: ",LHS)
plt.plot(x,d(x))
plt.grid(True)
plt.show()
