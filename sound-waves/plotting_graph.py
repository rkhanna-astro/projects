def label_graph(plot, time, entity):
  plot.set(xlabel='Position Axis', ylabel=f'{entity} Axis')
  plot.set_title(f't = {time} ')
  return plot

def plot_graph(time, pos, vel, rho, v_plots, d_plots):
  if time == 0:
    vel_t0 = label_graph(v_plots[0,0], time, 'Velocity ($V_x$)')
    den_t0 = label_graph(d_plots[0,0], time, 'Density ($p - p_0$)')
    vel_t0.plot(pos, vel, color="black")
    den_t0.plot(pos, rho, color="black")

  elif time == 0.3:
    vel_t1 = label_graph(v_plots[0,1], time, 'Velocity ($V_x$)')
    den_t1 = label_graph(d_plots[0,1], time, 'Density ($p - p_0$)')
    vel_t1.plot(pos, vel, color="black")
    den_t1.plot(pos, rho, color="black")

  elif time == 0.5:
    vel_t2 = label_graph(v_plots[1,0], time, 'Velocity ($V_x$)')
    den_t2 = label_graph(d_plots[1,0], time, 'Density ($p - p_0$)')
    vel_t2.plot(pos, vel, color="black")
    den_t2.plot(pos, rho, color="black")

  elif time == 1:
    vel_t3 = label_graph(v_plots[1,1], time, 'Velocity ($V_x$)')
    den_t3 = label_graph(d_plots[1,1], time, 'Density ($p - p_0$)')
    vel_t3.plot(pos, vel, color="black")
    den_t3.plot(pos, rho, color="black")

def plot_unstable_graph(time, pos, vel, rho, v_plots, d_plots):
  vel_t0 = label_graph(v_plots[0,0], time, 'Velocity ($V_x$)')
  den_t0 = label_graph(d_plots[0,0], time, 'Density ($p - p_0$)')
  vel_t0.plot(pos, vel, color="black")
  den_t0.plot(pos, rho, color="black")
