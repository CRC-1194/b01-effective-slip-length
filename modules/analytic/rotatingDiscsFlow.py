import numpy as np
import scipy.special as spe


def rotatingflow(r, z, R, H, omega):
    '''Analytic flow velocity field between two rotating plates

    r, z - coordinate in the wedge
    R - radius of the wedge
    H - height of the wedge
    omega - angular velocity

    '''


    zero_J1 = spe.jn_zeros(1,8000)    #the positive zeros of the bessel function 1st degree
    beta = H/R

    v_phi_r = 0
    v_phi_z = 0
    
    for j in range(zero_J1.size - 1):
        v_phi_r = v_phi_r + 2*spe.jv(1,zero_J1[j]*r)*np.sinh(zero_J1[j]*(-z))/(zero_J1[j]*np.sinh(zero_J1[j]*beta)*spe.jv(0,zero_J1[j]))
        #v_phi_z = v_phi_z + 2*spe.jv(1,zero_J1[j]*0.5*R/R)*np.sinh(zero_J1[j]*(-z))/(zero_J1[j]*np.sinh(zero_J1[j]*beta)*spe.jv(0,zero_J1[j]))
    
    return omega*R*v_phi_r

