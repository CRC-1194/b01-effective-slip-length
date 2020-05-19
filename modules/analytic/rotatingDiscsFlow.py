import numpy as np

# analytic reference solution for the Couette and 
# Poiseuille flow between two plates

def rotatingflow(x, r, h, omega, mu, L1 = 0, L2 =0):
    '''Analytic Poiseuille-flow velocity field between two rotating plates

    The coordinate system is located in the center of the channel
    x - coordinate in the channel (cross section)
    r - radius of the wedge
    mu - kinematic viscosity
    h - height of the channel
    omega - rotation speed
    L - slip length (default L=0)
    '''
    # f(eta) is a sixth degree polynomial 
    u = -np.sqrt(omega**5/mu**3)/24*(6/h**3*x**5 - 10/h**2*x**4 + 4/h*x**3)*r
    v = omega*r*(-x**4/h**4 + 2/h**3*x**3)
    w = omega**2/(12*mu)*(1/h**3*x**6 - 2/h**2*x**5 + 1/h*x**4)
    magU = np.sqrt(u**2 + v**2 + w**2)

    # f(eta) is a fifth degree polynomial    
    # u = -np.sqrt(omega**5/mu**3)/48*(10/h**2*x**4 - 12/h*x**3 + 2*h*x)*r
    # v = omega*r*(-x**4/h**4 + 2/h**3*x**3)
    # w = omega**2/(24*mu)*(2/h**2*x**5 - 3/h*x**4 + h*x**2)
    # magU = np.sqrt(u**2 + v**2 + w**2)
    
    
    
    return u, v, w, magU

