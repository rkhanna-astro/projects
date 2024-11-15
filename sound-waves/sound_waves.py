import math
import numpy as np
import matplotlib.pyplot as plt


N = 1000
density = [0]*N
velocity = [0]*N
position = [0]*N
sound_speed = 1

rho0 = 1
rho1 = 0.03
vel1 = (sound_speed*rho1)/rho0
length = 2
lamda = 1

courant_number = 0.1
del_x = length/N
del_t = (del_x*courant_number)/sound_speed

pos = 0
for x in np.arange(0, 2, del_x):
    density[pos] = 1 + rho1*(math.cos((2*3.14*x)/lamda))
    velocity[pos] = vel1*(math.cos((2*3.14*x)/lamda))
    position[pos] = x
    pos += 1


print("tthis is delt", del_t)

fig_v, v_axis = plt.subplots(2,2)
fig_d, d_axis = plt.subplots(2,2)

def plot_graph(plot, time, entity):
    plot.set(xlabel='Position Axis', ylabel=f'{entity} Axis')

    if time == 0:
        plot.set_title("t = 0.0 s")
    elif time == 0.3:
        plot.set_title("t = 0.3 s")
    elif time == 0.5:
        plot.set_title("t = 0.5 s")
    elif time == 1:
        plot.set_title("t = 1.0 s")
    return plot

for t in np.arange(0, 1+del_t, del_t):
    copy_v = [0]*N
    copy_d = [0]*N
    for j in np.arange(0, N):
        if  j == N-1:
            copy_v[j] = (velocity[j-1] + velocity[0])/2 + del_t * (((velocity[j-1]**2)-(velocity[0]**2))/(4*del_x) + (sound_speed**2/density[j])*((density[j-1]-density[0])/(2*del_x)))
            copy_d[j] = (density[j-1] + density[0])/2 + del_t * ((density[j-1]*velocity[j-1] - density[0]*velocity[0])/(2*del_x))
        
        if j != N-1:
          copy_v[j] = (velocity[j-1] + velocity[j+1])/2 + del_t * (((velocity[j-1]**2)-(velocity[j+1]**2))/(4*del_x) + (sound_speed**2/density[j])*((density[j-1]-density[j+1])/(2*del_x)))
  
          copy_d[j] = (density[j-1] + density[j+1])/2 + del_t * ((density[j-1]*velocity[j-1] - density[j+1]*velocity[j+1])/(2*del_x))

    velocity = np.copy(copy_v)
    density = np.copy(copy_d)

    plot_densty = [rho - rho0 for rho in density]

    if t == 0:
        vel_t0 = plot_graph(v_axis[0,0], t, 'Velocity ($V_x$)')
        den_t0 = plot_graph(d_axis[0,0], t, 'Density ($p - p_0$)')
        vel_t0.plot(position, velocity, color="black")
        den_t0.plot(position, plot_densty, color="black")
    elif t == 0.3:
        vel_t1 = plot_graph(v_axis[0,1], t, 'Velocity ($V_x$)')
        den_t1 = plot_graph(d_axis[0,1], t, 'Density ($p - p_0$)')
        vel_t1.plot(position, velocity, color="black")
        den_t1.plot(position, plot_densty, color="black")

    elif t == 0.5:
        vel_t2 = plot_graph(v_axis[1,0], t, 'Velocity ($V_x$)')
        den_t2 = plot_graph(d_axis[1,0], t, 'Density ($p - p_0$)')
        vel_t2.plot(position, velocity, color="black")
        den_t2.plot(position, plot_densty, color="black")

    elif t == 1:
        vel_t3 = plot_graph(v_axis[1,1], t, 'Velocity ($V_x$)')
        den_t3 = plot_graph(d_axis[1,1], t, 'Density ($p - p_0$)')
        vel_t3.plot(position, velocity, color="black")
        den_t3.plot(position, plot_densty, color="black")

fig_d.subplots_adjust(bottom=0.1, right=0.9, 
                      top=0.9, wspace=0.6, hspace=0.6)
fig_v.subplots_adjust(bottom=0.1, right=0.9, 
                      top=0.9, wspace=0.6, hspace=0.6)
plt.show()
