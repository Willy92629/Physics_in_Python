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
N =100
z = 1
R = 0.02
dl = R*2*np.pi/N
posx = [R*np.cos(2*np.pi*i/N) for i in range(N)]
posy = [R*np.sin(2*np.pi*i/N) for i in range(N)]
dsx = [-dl*np.sin(2*np.pi*i/N) for i in range(N)]
dsy = [dl*np.cos(2*np.pi*i/N) for i in range(N)]
ds = [0,0,0]
B = [0,0,0]

for i in range(n):
    for j in range(n):
        for k in range(N):
            vr = [x[j]-posx[k],y[i]-posy[k],z]
            r = ((x[j]-posx[k])**2 +(y[i]-posy[k])**2 + z**2)**0.5
            ds[0] = dsx[k]
            ds[1] = dsy[k]
            dB = c * I *np.cross(ds,vr)/r**3
            B[0] += dB[0]
            B[1] += dB[1]
        u[i][j] = B[0]
        v[i][j] = B[1]
        B = [0,0,0]
        ds = [0,0,0]
k = (u**2 + v**2)**0.5
plt.axis('scaled')
plt.streamplot(x,y,u,v,color = np.log(k))
plt.streamplot(x,y,u,v)
plt.axis([-L,L,-L,L])
plt.show()