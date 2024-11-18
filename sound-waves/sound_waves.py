import math
import numpy as np
import matplotlib.pyplot as plt
import plotting_graph

def model_sound_waves():

  N = 1000
  density = [0]*N
  velocity = [0]*N
  position = [0]*N
  sound_speed = 1
  rho_0 = 1
  rho_1 = 0.3
  vel_1 = (sound_speed*rho_1)/rho_0
  length = 2
  lamda = 1
  courant_number = 0.1
  del_x = length/N
  del_t = (del_x*courant_number)/sound_speed
  
  pos = 0
  for x in np.arange(0, 2, del_x):
    density[pos] = 1 + rho_1*(math.cos((2*3.14*x)/lamda))
    velocity[pos] = vel_1*(math.cos((2*3.14*x)/lamda))
    position[pos] = x
    pos += 1
  
  fig_v, v_plots = plt.subplots(2,2)
  fig_d, d_plots = plt.subplots(2,2)
  
  temp_v, temp_d = 0, 0

  if courant_number > 1:
    for time in np.arange(0, 3*del_t, del_t):
      prev_v = velocity[-1]
      prev_d = density[-1]
  
      for j in np.arange(0, N):
        curr_v = velocity[j]
        curr_d = density[j]
        
        if  j == N-1:
          next_v = velocity[0]
          next_d = density[0]
  
          temp_v = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))
          temp_d = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))
        if j != N-1:
          next_v = velocity[j+1]
          next_d = density[j+1]  
  
          temp_v = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))
          temp_d = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))
            
          prev_v = curr_v
          curr_v = next_v
  
          prev_d = curr_d
          curr_d = next_d 
   
        velocity[j] = temp_v
        density[j] = temp_d
  
      density_diff = [rho - rho_0 for rho in density]
      plotting_graph.plot_unstable_graph(time, position, velocity, density_diff, v_plots, d_plots)

  for time in np.arange(0, 1+del_t, del_t):
    prev_v = velocity[-1]
    prev_d = density[-1]

    for j in np.arange(0, N):
      curr_v = velocity[j]
      curr_d = density[j]
      
      if  j == N-1:
        next_v = velocity[0]
        next_d = density[0]

        temp_v = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))
        temp_d = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))
      if j != N-1:
        next_v = velocity[j+1]
        next_d = density[j+1]  

        temp_v = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))
        temp_d = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))
          
        prev_v = curr_v
        curr_v = next_v

        prev_d = curr_d
        curr_d = next_d 
 
      velocity[j] = temp_v
      density[j] = temp_d

    density_diff = [rho - rho_0 for rho in density]
    if time == 0 or time == 0.3 or time == 0.5 or time == 1:
      plotting_graph.plot_graph(time, position, velocity, density_diff, v_plots, d_plots)

#   fig.suptitle("Common Title for All Subplots")
  fig_d.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
  fig_v.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
  plt.show()

if __name__ == "__main__":
  model_sound_waves()
