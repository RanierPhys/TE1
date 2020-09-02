import numpy as np
import matplotlib.pyplot as plt

#accelerate particle from t = 0. to t= 1., and constant velocity before.



def r_0(t):
    w = np.pi
    a = 0.8/w
    return np.array([0.,a*np.sin(w*t)] )   

def v_0(x):
    w = np.pi
    a = 0.8/w
    return [0.,a*w*np.cos(w*x)]

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
t=0
#defining retadard time:
tret = np.linspace(-10000., t, 50000)
r0 = np.zeros([len(tret),2])
beta = np.zeros([len(tret),2])
Lambda = np.zeros([len(tret),2])
angles = []

#defining the directions of kvector (15,30, 45, 60, ..., 360)
for i in range(0,24):
    angles.append(15*i*np.pi/180)

plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca()

for phi in angles:


    for i in range(0,len(tret)):
        
        r0[i][1] = r_0(tret[i])[1]
        r0[i][0] = r_0(tret[i])[0]
        vi = v_0(tret[i])
        vi = np.array(vi)
        dt = t-tret[i]
        beta[i][0] = dt*(vi[0])
        beta[i][1] = dt*(vi[1])
        betai = np.array([vi[0], vi[1]])
        Lambdai = lambdafun(t,tret[i], gamma, betai, kvetor(phi))
        Lambda[i][0] =  Lambdai[0]
        Lambda[i][1] = Lambdai[1]
    px = r0[:,0] + beta[:,0] + Lambda[:,0]
    py = r0[:,1] + beta[:,1] + Lambda[:,1]
    ax.plot(px, py, color = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linhas de Campo Elétrico')
leg = ax.legend()   
plt.show()
