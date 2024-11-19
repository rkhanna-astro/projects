# We need math package for using sinusoidal functions.
import math
# Numpy provides us with vide variety of mathematical and array manipulation tools.
import numpy as np
# Using matplotlib we can plot our results.
import matplotlib.pyplot as plt
# This module has been created to make our code modular and separate out plotting functionalities
import plotting_graph


# In this function, we have added the logic to simulate 1D sound wave propogation
def model_sound_waves():
 
  # Let's take user input for dynamic terms to make our model more user-friendly.
  try: 
    # First let us define our grid size for modeling a medium
    N = input("Enter grid resolution (default is 1000): ") or "1000"
    N = int(N)
  
    # Based on the input grid resolution choosen by the user, 
    # we define the velocity, density and position matrix for each grid point 
    density = [0]*N
    velocity = [0]*N
    position = [0]*N
  
    # Now let us initialize the perturbation (disturbance) density amplitude. 
    # If the amplitude is small our solution should show linear evolution,
    # and if it large enough, we expec the wave to grow non-linearly.
    rho_1 = input("Enter perturbation density amplitude (default is 0.03): ") or "0.03"
    rho_1 = float(rho_1)
    # Courant variable defines the stability of a finite difference system.
    # If it's too large (more than 1) our system can solution can collapse giving invalid results.
    courant_number = input("Enter courant number (default is 0.1): ") or "0.1"
    courant_number = float(courant_number)
  except ValueError:
    # If any invalid number is entered the code will escape out
    print("That's not a valid number")
    return

  # Initial conditions given in the study statement   
  sound_speed = 1
  rho_0 = 1
  length = 2
  lamda = 1

  # We can derive the velocity disturbance's amplitude 
  # using it's relation with isotherm sound speed and density ratio
  vel_1 = (sound_speed*rho_1)/rho_0
  # del_x defines spacing between two consecutive points on our grid.   
  del_x = length/N
  # del_t defines the time step for our temporal evolution of flux conservative equation.   
  del_t = (del_x*courant_number)/sound_speed
  
  # Through this loop we initiate the initial density and velocity waveforms
  # at the starting of our time evolution (t = 0). 
  # We also define the position matrix to access each grid point.
  pos = 0
  for x in np.arange(0, 2, del_x):
    density[pos] = 1 + rho_1*(math.cos((2*3.14*x)/lamda))
    velocity[pos] = vel_1*(math.cos((2*3.14*x)/lamda))
    position[pos] = x
    pos += 1
  
  # We will have different plots to track velocity and density evolution of te wave.
  fig_v, v_plots = plt.subplots(2,2)
  fig_d, d_plots = plt.subplots(2,2)

  # Here we define the starting time and ending time for our disturbance evolution.
  # The end time depends on the courant number as unstable condition can break the code
  # so we need to escape early.    
  start_time = 0
  if courant_number > 1:
    # This can break the code due to overflow hence we will only evolve two time steps
    end_time = 0.1+del_t
  else:
    # For the stable case, we can evolve our system till the very end (propagate one wavelength)
    end_time = 1 + del_t

  # This is temporal evolution iteration for our wave equation discretized and approximated 
  # using Finite Difference Schemes. 
  # For various initial conditions the velocity and density waveforms might evolve differently.
  for time in np.arange(start_time, end_time, del_t):
    # prev variable (short form of previous) tracks the "j-1" grid point's velocity and density
    prev_v = velocity[-1]
    prev_d = density[-1]
  
    for j in np.arange(0, N):
      # curr variable (short form of current) tracks the "j" grid point's velocity and density
      curr_v = velocity[j]
      curr_d = density[j]
      
      if j != N-1:
        # next variable tracks the "j+1" grid point's velocity and density
        next_v = velocity[j+1]
        next_d = density[j+1]  

        # Here we update the velocity matrix for each grid point "j".
        # We have applied the Lax Finite Difference method here to approximate velocity gradient terms.
        # The density gradient term has been approximated using central difference scheme.
        velocity[j] = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))

        # Here we update the density matrix for each grid point "j".
        # The density gradient term has been approximated using central difference scheme.
        density[j] = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))

        # IMPORTANT
        # The current "j" point will become the previous point for the "j+1" point.
        # But, we have already updated the "j" point's velocity and density values, 
        # and they can't be used as these values are for (t+1) time step, 
        # and we need the values for the previous "t" time step for each time evolution to "t+1".

        # To handle this, we keep track of "j" point's density and velocities at "t" time step.
        # This is important as "j" act as previous point for "j+1" point and we need it's "t" time step values.
        prev_v = curr_v
        prev_d = curr_d

      if  j == N-1:
        # next variable tracks the "N-1" (last) grid point's velocity and density.
        # As our waveform should be continous after one complete wavelength, 
        # the last grid point (N+1) connects to the first grid point (0).
        next_v = velocity[0]
        next_d = density[0]

        velocity[j] = (prev_v + next_v)/2 + del_t * (((prev_v**2)-(next_v**2))/(4*del_x) + (sound_speed**2/curr_d)*((prev_d-next_d)/(2*del_x)))
        density[j] = (prev_d + next_d)/2 + del_t * ((prev_d*prev_v - next_d*next_v)/(2*del_x))
    
    # Time evolution is done, so it's time to observe the results.
    # We need to plot (p-p0) for our density values at each grid point
    density_diff = [rho - rho_0 for rho in density]
    if courant_number > 1:
      # We will plot differently for unstable evolution case 
      plotting_graph.plot_unstable_graph(time, position, velocity, density_diff, v_plots, d_plots)
    elif (time == 0 or time == 0.3 or time == 0.5 or time == 1):
      # This module plots the "velocity and density" vs position curves for different times.   
      plotting_graph.plot_graph(time, position, velocity, density_diff, v_plots, d_plots)

  # I needed to do some adjustments to better space each curve.  
  fig_d.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
  fig_v.subplots_adjust(bottom=0.1, right=0.9, 
                        top=0.9, wspace=0.6, hspace=0.6)
  
  # This will render both the velocity and density graphs for different times.
  # Both the plots might overlap, so you can close one to show the other,
  # or you can move one of the graph's window to see them side-by-side.   
  plt.show()

# This is the main function which is called by python's compiler as soon as we run this file
if __name__ == "__main__":
  # Our modeling sound wave function is called.  
  model_sound_waves()
