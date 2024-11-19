# This function does the Axis labeling work for us
def label_graph(plot, ind, time, entity):
  plot.set(xlabel='Position Axis', ylabel=f'{entity} Axis')
  plot.set_title(f' {ind}     t = {time} ')
  return plot

# This function plots the velocity and density graphs for 4 different times.
# This will be called for stable Courant Number case.
def plot_graph(time, pos, vel, rho, v_plots, d_plots):
  max_vel = max(vel)
  max_den = max(rho)
  if time == 0:
    vel_t0 = label_graph(v_plots[0,0], '(a)', time, 'Velocity ($V_x$)')
    den_t0 = label_graph(d_plots[0,0], '(a)', time, 'Density ($p - p_0$)')
    vel_t0.axhline(y=max_vel, color='b', linestyle='--')
    den_t0.axhline(y=max_den, color='b', linestyle='--')
    vel_t0.text(10, max_vel, f'Maximum Velocity: {max_vel:.2f}', color='b', fontsize=10, ha='left')
    den_t0.text(10, max_den, f'Maximum Desnity: {max_den:.2f}', color='b', fontsize=10, ha='left')
    vel_t0.plot(pos, vel, color="black")
    den_t0.plot(pos, rho, color="black")

  elif time == 0.3:
    vel_t1 = label_graph(v_plots[0,1], '(b)', time, 'Velocity ($V_x$)')
    den_t1 = label_graph(d_plots[0,1], '(b)', time, 'Density ($p - p_0$)')
    vel_t1.axhline(y=max_vel, color='b', linestyle='--')
    den_t1.axhline(y=max_den, color='b', linestyle='--')
    vel_t1.plot(pos, vel, color="black")
    den_t1.plot(pos, rho, color="black")

  elif time == 0.5:
    vel_t2 = label_graph(v_plots[1,0], '(c)', time, 'Velocity ($V_x$)')
    den_t2 = label_graph(d_plots[1,0], '(c)', time, 'Density ($p - p_0$)')
    vel_t2.axhline(y=max_vel, color='b', linestyle='--')
    den_t2.axhline(y=max_den, color='b', linestyle='--')
    vel_t2.plot(pos, vel, color="black")
    den_t2.plot(pos, rho, color="black")

  elif time == 1:
    vel_t3 = label_graph(v_plots[1,1], '(d)', time, 'Velocity ($V_x$)')
    den_t3 = label_graph(d_plots[1,1], '(d)', time, 'Density ($p - p_0$)')
    vel_t3.axhline(y=max_vel, color='b', linestyle='--')
    den_t3.axhline(y=max_den, color='b', linestyle='--')
    vel_t3.plot(pos, vel, color="black")
    den_t3.plot(pos, rho, color="black")

# This function plots the velocity and density graphs for only small time evolution.
# This will be called for unstable Courant Number case.
def plot_unstable_graph(time, pos, vel, rho, v_plots, d_plots):
  if time == 0:
    vel_t0 = label_graph(v_plots[0,0], '(a)', time, 'Velocity ($V_x$)')
    den_t0 = label_graph(d_plots[0,0], '(a)', time, 'Density ($p - p_0$)')
    vel_t0.plot(pos, vel, color="red")
    den_t0.plot(pos, rho, color="red")

  elif time == 0.04:
    vel_t1 = label_graph(v_plots[0,1], '(b)', time, 'Velocity ($V_x$)')
    den_t1 = label_graph(d_plots[0,1], '(b)', time, 'Density ($p - p_0$)')
    vel_t1.plot(pos, vel, color="red")
    den_t1.plot(pos, rho, color="red")

  elif time == 0.08:
    vel_t2 = label_graph(v_plots[1,0], '(c)', time, 'Velocity ($V_x$)')
    den_t2 = label_graph(d_plots[1,0], '(c)', time, 'Density ($p - p_0$)')
    vel_t2.plot(pos, vel, color="red")
    den_t2.plot(pos, rho, color="red")

  elif time == 0.1:
    vel_t3 = label_graph(v_plots[1,1], '(d)', time, 'Velocity ($V_x$)')
    den_t3 = label_graph(d_plots[1,1], '(d)', time, 'Density ($p - p_0$)')
    vel_t3.plot(pos, vel, color="red")
    den_t3.plot(pos, rho, color="red")
