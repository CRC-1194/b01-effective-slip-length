import numpy as np
import scipy.special as spe


def rotatingflow(r, z, R, H, omega):
    '''Analytic Poiseuille-flow velocity field between two rotating plates

    The coordinate system is located in the center of the channel
    r, z - coordinate in the wedge
    r - radius of the wedge
    H - height of the wedge
    omega - angular velocity

    '''
    # f(eta) is a sixth degree polynomial 
    #u = -np.sqrt(omega**5/nu**3)/24*(6/h**3*z**5 - 10/h**2*z**4 + 4/h*z**3)*r
    #v = omega*r*((0.77139*h*np.sqrt(omega/nu)-1)/h**4*z**4+(2-1.54278*h*np.sqrt(omega/nu))/h**3*z**3+0.77139*z*np.sqrt(omega/nu))
    #w = omega**2/(12*nu)*(1/h**3*z**6 - 2/h**2*z**5 + 1/h*z**4)
    #magU = np.sqrt(u**2 + v**2 + w**2)

    zero_J1 = spe.jn_zeros(1,220)
    beta = H/R

    v_phi_r = 0
    v_phi_z = 0
    
    for j in range(zero_J1.size - 1):
        v_phi_r = v_phi_r + 2*spe.jv(1,zero_J1[j]*r)*np.sinh(zero_J1[j]*(-z))/(zero_J1[j]*np.sinh(zero_J1[j]*beta)*spe.jv(0,zero_J1[j]))
        #v_phi_z = v_phi_z + 2*spe.jv(1,zero_J1[j]*0.5*R/R)*np.sinh(zero_J1[j]*(-z))/(zero_J1[j]*np.sinh(zero_J1[j]*beta)*spe.jv(0,zero_J1[j]))
    
    return omega*R*v_phi_r

