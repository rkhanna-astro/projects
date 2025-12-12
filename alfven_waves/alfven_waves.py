# We need math package for using sinusoidal functions.
import math
# Numpy provides us with vide variety of mathematical and array manipulation tools.
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm

def label_graph(plot, entity):
  plot.set(xlabel='Position Axis', ylabel=f'{entity} Axis')
  plot.set_title('1-D Alfven wave propagation')
  return plot

def plot_maxima(field, pos, plot):
  for i in range(1, len(field)-1):
     if field[i] > 0 and field[i-1] < field[i] and field[i+1] < field[i]:
        print(field[i-1], field[i], field[i+1])
        x_max = pos[i]
        v_max = field[i]

        plot.axvline(x=x_max, color='red', linestyle='--', label=f'Max value at x={x_max:.2f}')
        plot.plot(x_max, v_max, 'r*')
        plot.text(x_max, v_max, f'({x_max:.2f}, {v_max:.2f})', color='black', fontsize=6, ha='left', va='bottom')

def find_closest(pos, val):
  left = 0
  right = len(pos) - 1

  while left < right:
     mid = int((left + right)/2)
     if val < pos[mid]:
       right = mid - 1
     elif val > pos[mid]:
       left = mid + 1
     else:
        return mid
    
  return left

colormap = cm.viridis
rho_0 = 10
b_0 = 1
b_1 = 0.5
vel_1 = -b_1/(math.sqrt(4*3.14*rho_0))
N = 1000
mag_field = [0]*N
vel_field = [0]*N
position = [0]*N
time_evolution = [0, 0.5, 1.0]

length = 2
lamda = 1
courant_number = 0.05
del_x = length/N
sound_speed = 1

del_t = (del_x*courant_number)/sound_speed
pos = 0

fig_v, v_plots = plt.subplots(1)
fig_d, d_plots = plt.subplots(1)

expected_speed = round(b_0/(4*3.14*rho_0)**(0.5), 2)
# print(expected_speed)

for x in np.arange(0, 2, del_x):
    mag_field[pos] = 1 + b_1*(math.cos((2*3.14*x)/lamda))
    vel_field[pos] = vel_1*(math.cos((2*3.14*x)/lamda))
    position[pos] = float(x)
    pos += 1

# plot_maxima(vel_field, position, v_plots)
# plot_maxima(mag_field, position, d_plots)

# print(mag_field)
ind = 0
#plotting velocity and magnetic field maxima
# pos_v = 0.5
# pos_b = 1

for time in np.arange(0, 1 + del_t, del_t):
    vel_prev = vel_field[-1]
    mag_prev = mag_field[-1]

    for j in np.arange(0, N):
        vel_curr = vel_field[j]
        mag_curr = mag_field[j]

        if j < N-1:
            vel_next = vel_field[j+1]
            mag_next = mag_field[j+1]
        else:
            vel_next = vel_field[0]
            mag_next = mag_field[0]

        vel_field[j] = vel_curr + ((del_t*b_0)/(4*3.14*rho_0))*((mag_next - mag_prev)/(2*del_x))
        mag_field[j] = mag_curr + (del_t*b_0)*((vel_next - vel_prev)/(2*del_x))
    
        vel_prev = vel_curr
        mag_prev = mag_curr

    if time in time_evolution:
      vel_t = label_graph(v_plots, 'Velocity Wave ($V_Z$)')
      den_t = label_graph(d_plots, 'Magnetic Wave ($B_Z$)')
      vel_t.plot(position, vel_field, label = str(time) + 's', color=colormap(time))
      den_t.plot(position, mag_field, label = str(time) + 's', color=colormap(time))

      if ind < len(time_evolution):
        pos_v = 0.5 + expected_speed*time_evolution[ind]
        pos_b = 1.0 + expected_speed*time_evolution[ind]
      
      # print(pos_v, pos_b)
      ind_v = find_closest(position, pos_v)
      ind_b = find_closest(position, pos_b)
    
      val_v = vel_field[ind_v]
      val_b = mag_field[ind_b]
    
      vel_t.text(pos_v, val_v, f'{ind+1}')
      den_t.text(pos_b, val_b, f'{ind+1}')

      ind += 1
# print(position)

vel_t.legend(loc='upper right')
den_t.legend(loc='upper right')

# print(vel_field)
# plot_maxima(vel_field, position, v_plots)
# plot_maxima(mag_field, position, d_plots)


plt.show()
