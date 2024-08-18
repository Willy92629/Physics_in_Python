import matplotlib.pyplot as plt
import numpy as np

c = 1
I = 1

L = 0.0405
dL = 0.005
n = int(L*2/dL)+1
x = np.array([-L + dL*i for i in range(n) ])
y = np.array([-L + dL*i for i in range(n) ])
u = np.array([[0.0 for i in range(n)]for j in range(n)])
v = np.array([[0.0 for i in range(n)]for j in range(n)])

D = 1
dD = 0.01
d = [-0.5 + i*dD for i in range(101) ]
ds1 = [0,0,0.01]
ds2 = [0,0,-0.01]
B = [0,0,0]

for i in range(n):
    for j in range(n):
        for k in range(101):
            vr1 = [x[j]+0.02,y[i],-d[k]]
            r1 = ((x[j]+0.02)**2 + y[i]**2 + (-d[k])**2)**0.5
            dB1 = c * I *np.cross(ds1,vr1)/r1**3
            vr2 = [x[j]-0.02,y[i],-d[k]]
            r2 = ((x[j]-0.02)**2 + y[i]**2 + (-d[k])**2)**0.5
            dB2 = c * I *np.cross(ds2,vr2)/r2**3
            B[0] += (dB1[0]+dB2[0]) 
            B[1] += (dB1[1]+dB2[1])
        u[i][j] = B[0]
        v[i][j] = B[1]
        B = [0,0,0]
k = (u**2 + v**2)**0.5
plt.axis('scaled')
plt.streamplot(x,y,u,v,color = np.log(k))
plt.streamplot(x,y,u,v)
plt.axis([-L,L,-L,L])
plt.show()
