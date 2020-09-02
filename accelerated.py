import numpy as np
import matplotlib.pyplot as plt

#accelerate particle from t = 0. to t= 1., and constant velocity before.

def x_0(t):
    if t < 0:
        return 0.
    if 0< t <1:
        return np.sqrt(1+t**2) -1.
    if 1 < t:
        return np.sqrt(2) -1. + (t-1.)/np.sqrt(2) 
    
def v_0(x):
    if x <= 0:
        return [0.,0.]
    if 0< x <1:
        div = (1+x**2)**(1/2)
        return [x/(div),0.]
    if 1 <= x:
        return [1./np.sqrt(2),0.]

def kvetor(phi):
    kpar,kperp = np.cos(phi), np.sin(phi)
    return np.array([kpar,kperp])

def gamma(b):
    return (1-b**2)**(-1/2)
    

def lambdafun(t,tret,gamma,beta, kvetor):
    if beta[0] == 0. and beta[1] == 0.:
        betanormal = np.array([0.,0.])
        betamodulo = 0.
        kbeta = 0.
    else:        
        betamodulo = np.sqrt(beta[0]**2+beta[1]**2)
        betanormal = beta/betamodulo
        kbeta = np.dot(kvetor,beta)/betamodulo
    gammabeta = gamma(betamodulo) 
    e1 = gammabeta**(-1) -1
    
    prod1 = np.dot(kvetor,betanormal)
    prod2 = np.dot(kvetor,beta)
    
    return (t-tret)*(e1*prod1*betanormal + kvetor )/(gammabeta*(1.+prod2))

#particle's time:
t=2.
#defining retadard time:
tret = np.linspace(-4., t, 5000)
x0 = np.zeros([len(tret),2])
beta = np.zeros([len(tret),2])
Lambda = np.zeros([len(tret),2])
angles = []

#defining the directions of kvector (15,30, 45, 60, ..., 360)
for i in range(0,72):
    angles.append(5*i*np.pi/180)

plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca()

for phi in angles:


    for i in range(0,len(tret)):
        
        x0[i][0] = x_0(tret[i])
        x0[i][1] = 0.
        vi = v_0(tret[i])
        vi = np.array(vi)
        dt = t-tret[i]
        beta[i][0] = dt*(vi[0])
        beta[i][1] = dt*(vi[1])
        betai = np.array([vi[0], vi[1]])
        Lambdai = lambdafun(t,tret[i], gamma, betai, kvetor(phi))
        Lambda[i][0] =  Lambdai[0]
        Lambda[i][1] = Lambdai[1]
    px = x0[:,0] + beta[:,0] + Lambda[:,0]
    py = x0[:,1] + beta[:,1] + Lambda[:,1]
    ax.plot(px, py, color = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linhas de Campo Elétrico')
leg = ax.legend()   
plt.show()
