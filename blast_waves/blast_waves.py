#
import math
import numpy as np

import matplotlib.pyplot as plt

# Initial conditions
rho_0 = 1
lum_0 = 1
H = 1
gamma = 5/3

t_0 = 0.05
r_0 = 0.76*(math.pow(t_0, 0.6))
eth_0 = (5/11)*t_0
p_0 = 0.16/(math.pow(t_0, 0.8))
vol_0 = 4/3*(3.14*r_0**3)
y_0 = round(math.pow(((math.pow(gamma, 2) - 1)/2)*(eth_0/(rho_0*vol_0)), 0.5)*t_0, 4)

p = p_0
eth = eth_0
vol = vol_0
del_y = 0.0001
del_t =  del_y/math.pow(((gamma**2 - 1)/2)*(eth/(rho_0*vol)), 0.5)

# print("Time step", del_t)
time = del_t
plot_time = []
plot_y = []
plot_z1 = []
plot_z2 = []
plot_energy = []
plot_pressure = []

for y in np.arange(y_0, 1.9900 + del_y, del_y):
    z_2 = -2*H*np.log(1 + y/(2*H))
    z_1 = -2*H*np.log(1 - y/(2*H))
    plot_z1.append(z_1)
    plot_z2.append(-z_2)
    del_z = (z_1 - z_2)/100

    vol_i = 0
    radius = []
    height = []
    for z in np.arange(z_2, z_1 + del_z, del_z):
        if 1/2*math.pow(math.e, z/2)*(1 - y**2/4 + math.pow(math.e, -z)) <= 1:
           r = 2*H*np.arccos(1/2*math.pow(math.e, z/2)*(1 - y**2/4 + math.pow(math.e, -z)))
        else:
           r = 2*H*np.arccos(1)

        height.append(z)
        height.append(z)
        radius.append(-r)
        radius.append(r)
        vol_i = vol_i + 3.14*(r**2)*(del_z)
    
    if round(y, 4) in [1.0000, 1.4000, 1.9000, 1.9800, 1.9900]:
       plt.scatter(radius, height, label="Euler Approximation", marker='o')
       
    del_t =  del_y/math.pow(((gamma**2 - 1)/2)*(eth/(rho_0*vol_i)), 0.5)
    eth = eth + lum_0*del_t - p*(vol_i-vol)
    p = (gamma-1)*(eth/vol_i)
    vol = vol_i
    
    time += del_t
    # print("time step", time)
    plot_energy.append(eth)
    plot_pressure.append(p)
    plot_y.append(y)
    plot_time.append(time)
    

# print("Time", time)
# print(len(plot_pressure), len(plot_time))
vel_z1 = [0]
for i in range(len(plot_z1)-1):
    vel_z1.append((plot_z1[i+1] - plot_z1[i])/(plot_time[i+1] - plot_time[i]))


# plt.plot(plot_time[1000:], plot_pressure[1000:], label="Euler Approximation", marker='o')
# plt.xscale('log')
# plt.yscale('log')
# plt.plot(radius, height, label="Euler Approximation", marker='o')
plt.xlim(-10, 10)
plt.ylim(-10, 20)
plt.show()




