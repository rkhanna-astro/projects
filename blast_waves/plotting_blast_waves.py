def plot_bubble_evolution(time, radius, height, bubble_plot, ind):
    plot= None
    if time == 0.5000:
      plot = bubble_plot[0,0]
    if time == 0.8000:
      plot = bubble_plot[0,1]
    if time == 1.0000:
      plot = bubble_plot[1,0]
    if time == 1.4000:
      plot = bubble_plot[1,1]
    if time == 1.7000:
      plot = bubble_plot[0,0]
    if time == 1.9000:
      plot = bubble_plot[0,1]
    if time == 1.9800:
      plot = bubble_plot[1,0]
    if time == 1.9900:
      plot = bubble_plot[1,1]
    
    plot.scatter(radius, height, label="Euler Approximation", marker='o')
    plot.set(xlabel=f'r/H', ylabel=f'z/H')
    plot.set_title(f'{ind}    t = {time} ')
    plot.set_xlim(-20, 20)
    plot.set_ylim(-10, 20)