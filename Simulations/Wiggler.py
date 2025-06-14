import numpy as np
import matplotlib.pyplot as plt

#accelerate particle from t = 0. to t= 1., and constant velocity before.



def r_0(x):
    beta_0 = (2)**(-1/2)
    beta_perp = 0.1
    w = np.pi
    return np.array([beta_0*x,(beta_perp/w)*np.sin(w*x)] )   

def v_0(x):
    beta_0 = (2)**(-1/2)
    beta_perp = 0.1 
    w = np.pi
    return [beta_0,beta_perp*np.cos(w*x)]
    

def lambdafun(t,tret,v_0, phi):
    beta_0 = (2)**(-1/2) 
    gamma_0 = (1-beta_0**2)**(1/2)
    xi = np.sqrt((1+beta_0)/(1-beta_0))
    a1 = v_0(tret)[1]/gamma_0
    a2 = v_0(t)[1]/gamma_0
    x12 = np.arctanh(a1)/2. -np.arctanh(a2)/2.
    a3 = xi*np.tan(phi/2.) 
    if abs(a3) < np.inf:
        arg1 = (np.tanh(x12) + a3)/(1-a3*np.tanh(x12))
    else:
        arg1 = -1./np.tanh(x12)
    arg2 = arg1/xi
    psi = 2*np.arctan(arg2) 
    return np.array([np.cos(psi), np.sin(psi)])

#particle's time:
t=0.
#defining retadard time:
tret = np.linspace(-30., t, 1000)
r0 = np.zeros([len(tret),2])
Lambda = np.zeros([len(tret),2])
angles = []

#defining the directions of kvector (15,30, 45, 60, ..., 360)

for i in range(0,72):
    angles.append(5*i*np.pi/180.)
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca()

for phi in angles:
    #print('PHI \n\n', phi*180/np.pi)
    for i in range(0,len(tret)):
        
        r0[i][1] = r_0(tret[i])[1]
        r0[i][0] = r_0(tret[i])[0]
        #print(i)
        Lambda[i][0] = (t-tret[i])*lambdafun(t,tret[i],v_0, phi)[0]
        Lambda[i][1] = (t-tret[i])*lambdafun(t,tret[i],v_0, phi)[1]
        
        #beta_0 = (2)**(-1/2)
        #gamma_0 = (1-beta_0**2)**(1/2)        
        #xi = np.sqrt((1+beta_0)/(1-beta_0))
        #a1 = gamma_0*v_0(tret[i])[1]
        #a2 = gamma_0*v_0(t)[1]
        #a3 = xi*np.tan(phi/2.) 
        #numi = (np.arctanh(a1)/2. -np.arctanh(a2)/2. + np.arctanh(a3))/xi
        #print('PHI: \n\n', phi*180/np.pi, 'tempo i:   ', i, '\n' )
        #print('\n ESSE AQUI TEM DE SER ESCALAR  \n', numi, '\n\n\n')
    px = r0[:,0]+ Lambda[:,0]
    py = r0[:,1]+ Lambda[:,1]
    if phi*180/np.pi <= 360.:    
        ax.plot(px, py, color = 'b')
    else: 
        ax.plot(px, py, color = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linhas de Campo Elétrico')
leg = ax.legend()   
plt.show()
