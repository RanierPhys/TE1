import numpy as np
import matplotlib.pyplot as plt

#accelerate particle from t = 0. to t= 1., and constant velocity before.



def r_0(x):
    a =5.
    beta = 0.6
    w = beta/a
    return np.array([a*np.cos(w*x),a*np.sin(w*x)] )   

def v_0(x):
    a =5.
    beta = 0.6
    w = beta/a
    return np.array([-beta*np.sin(w*x),beta*np.cos(w*x)] ) 
    

def lambdafun(t,tret,v_0, phi):
    a =5.
    beta = 0.6
    w = beta/a
    gamma= (1-beta**2)**(-0.5)
    a1 = beta-np.tan(phi/2.)
    a2 = w*gamma*(tret-t)/2. + np.arctan(gamma*a1)
    psi = 2*np.arctan(beta -np.tan(a2)/gamma) 
    return np.array([np.cos(w*tret+psi), np.sin(w*tret+psi)])

#particle's time:
t=5.
#defining retadard time:
tret = np.linspace(-100., t, 1000)
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
