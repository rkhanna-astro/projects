import math
import numpy as np
import matplotlib.pyplot as plt


N = 1000
density = [0]*N
velocity = [0]*N
position = [0]*N
sound_speed = 1

rho0 = 1
rho1 = 0.3
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

# print("this is den", density[400])
# print("this is vel", velocity[588])\

plt.title("t = 0.0 s")
plt.xlabel("Position Axis")
plt.ylabel("Velocity Axis")
plt.plot(position, velocity, color="black")
plt.show()

print("tthis is delt", del_t)
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

    if t == 0.3:
        plt.title("t = 0.3 s")
        plt.xlabel("Position Axis")
        plt.ylabel("Velocity Axis")
        plt.plot(position, velocity, color="black")
        plt.show()
    elif t == 0.5:
        plt.title("t = 0.5 s")
        plt.xlabel("Position Axis")
        plt.ylabel("Velocity Axis")
        plt.plot(position, velocity, color="black")
        plt.show()
    elif t == 1:
        plt.title("t = 1 s")
        plt.xlabel("Position Axis")
        plt.ylabel("Velocity Axis")
        plt.plot(position, velocity, color="black")
        plt.show()

# print("this is den", density[400])
# print("this is vel", velocity[588])
