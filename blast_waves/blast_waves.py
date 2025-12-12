#
import math
import numpy as np

import matplotlib.pyplot as plt

import plotting_blast_waves as pbw

# Initial conditions
rho_0 = 1
lum_0 = 1
H = 1
gamma = 5/3

time_evolution = {
    0.5000: "A",
    0.8000: "B",
    1.0000: "C",
    1.4000: "D",
    1.7000: "E",
    1.9000: "F",
    1.9800: "G",
    1.9900: "H"
}

# Normalized parameters initialized
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

time = del_t
plot_time = []
plot_y = []
plot_z1 = []
plot_z2 = []
plot_velocity_z1 = [0]
plot_energy = []
plot_pressure = []
plot_r0 = []

radius = []
height = []

figure_1, plot_1 = plt.subplots(2, 2)
figure_2, plot_2 = plt.subplots(2, 2)
figure_3, plot_3 = plt.subplots(3, 2)

for y in np.arange(y_0, 1.9900 + del_y, del_y):
    rounded_y = round(y, 4)
    z_2 = -2*np.log(1 + y/(2*H))
    z_1 = -2*np.log(1 - y/(2*H))
    plot_z1.append(z_1)
    plot_z2.append(-z_2)
    del_z = (z_1 - z_2)/100

    vol_i = 0
    for z in np.arange(z_2, z_1 + del_z, del_z):
        if 1/2*math.pow(math.e, z/2)*(1 - y**2/4 + math.pow(math.e, -z)) <= 1:
           r = 2*np.arccos(1/2*math.pow(math.e, z/2)*(1 - y**2/4 + math.pow(math.e, -z)))
        else:
           r = 2*np.arccos(1)

        if rounded_y in time_evolution:
            height.append(z)
            height.append(z)
            radius.append(-r)
            radius.append(r)
        vol_i = vol_i + 3.14*(r**2)*(del_z)
    
    if rounded_y in time_evolution:
        if rounded_y < 1.5:
          pbw.plot_bubble_evolution(rounded_y, radius, height, plot_1, time_evolution[rounded_y])
        else:
          pbw.plot_bubble_evolution(rounded_y, radius, height, plot_2, time_evolution[rounded_y])

        height = []
        radius = []

    del_t =  del_y/math.pow(((gamma**2 - 1)/2)*(eth/vol_i), 0.5)
    eth = eth + del_t - p*(vol_i-vol)
    p = (gamma-1)*(eth/vol_i)
    vol = vol_i
    
    time += del_t
    plot_energy.append(eth)
    plot_pressure.append(p)
    plot_y.append(y)
    plot_time.append(time)
    
for i in range(len(plot_z1)-1):
    plot_velocity_z1.append((plot_z1[i+1] - plot_z1[i])/(plot_time[i+1] - plot_time[i]))

plot_3[0,0].plot(plot_time[1000:], plot_y[1000:])
plot_3[0,0].set(xlabel='t', ylabel='y')

plot_3[0,1].plot(plot_time[1000:], plot_z1[1000:])
plot_3[0,1].plot(plot_time[1000:], plot_z2[1000:])
# plot_3[0,1].plot(plot_time[1000:], plot_r0[1000:])
plot_3[0,1].set(xlabel='t', ylabel='distance')

plot_3[1,0].plot(plot_time[1000:], plot_energy[1000:])
plot_3[1,0].set(xlabel='t', ylabel='E_th')

plot_3[1,1].plot(plot_time[1000:], plot_pressure[1000:])
plot_3[1,1].set(xlabel='t', ylabel='P')

plot_3[2,0].plot(plot_time[1000:], plot_velocity_z1[1000:])
plot_3[2,0].set(xlabel='t', ylabel='dz_1/dt')

plot_3[2,1].plot(plot_z1[1000:], plot_velocity_z1[1000:])
plot_3[2,1].set(xlabel='z1', ylabel='dz_1/dt')

for plot in plot_3.flatten():
    plot.set_xscale('log')  # Set x-axis to log scale
    plot.set_yscale('log')

figure_1.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
figure_2.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
figure_3.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
plt.show()




