
# Initial Conditions

import math
import numpy as np

rho_0 = 1
lum_0 = 1
H = 1
gamma = 5/3

t_0 = 0.01
r_0 = 1
eth_0 = (5/11)*t_0
p_0 = (0.5*(eth_0))/(math.pow(r_0, 3))
vol_0 = 4/3*(3.14*r_0**3)
y_0 = math.pow(((math.pow(gamma, 2) - 1)/2)*(eth_0/(rho_0*vol_0)), 0.5)*t_0

print("Initia", eth_0, p_0, vol_0, y_0)

del_t = 0.01

p = p_0
eth = eth_0
vol = vol_0
y = y_0

while y < 1.99*H:
    z_2 = -2*H*np.log(1 + y/(2*H))
    z_1 = -2*H*np.log(1 - y/(2*H))
    del_z = (z_1 - z_2)/100

    vol_i = 0
    for z in np.arange(z_2, z_1, del_z):
        r = 2*H*np.arccos(1/2*math.pow(math.e, z/(2*H))*(1 - y**2/(4*H**2) + math.pow(math.e, (-z/H))))
        vol_i = vol_i + 3.14*(r**2)*(del_z)
    
    eth = eth + lum_0*del_t - p*(vol_i-vol)
    
    y = y + (((gamma**2 - 1)/2)*(eth/(rho_0*vol_i))**0.5)*del_t
    p = (gamma-1)*(eth/vol_i)
    vol = vol_i
    print("Final", eth, p, vol, y)






