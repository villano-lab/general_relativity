"""
script to plot sphere of masses in gravitational wave
"""

Amp = 0.4


import sys
sys.path.append('../MyPythonDir/')

import MyConstants as mc
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# array of points on sphere
N = 100 # number of points
wrapping = np.sqrt(N)

coords = np.zeros((N, 3)) # initial coords of points

for i in range(N):

    y = 1 - 2*i/N

    r = np.sqrt(1 - y**2)

    phi = i*(np.sqrt(5) - 1)*np.pi

    coords[i,:] = (r*np.sin(phi), y, r*np.cos(phi))





def wave_pos(t, coords):
    out = np.zeros(coords.shape)
    #print(coords.shape, out.shape)
    for i, xi in enumerate(coords):
        #print(coords)
        phase = Amp*np.cos(t-xi[2])
        here = np.sqrt(np.array([1 + phase, 1 - phase, 1]))*xi
        #print(here)
        out[i,:] = here
    return out

#x = wave_pos(0.1, coords)

#sys.exit()


fig = plt.figure()

ax = mplot3d.Axes3D(fig, auto_add_to_figure = 0)

fig.add_axes(ax)

ax.set_box_aspect((1,1,1))


#ax.set_title()


T = 60

points, = ax.plot(coords[:,0], coords[:,1], coords[:,2], 'o')

def init():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return [points]


def animate(j):
    t = j*4*np.pi/T
    newcoords = wave_pos(t, coords)
    #ax.remove(points)
    #points.set_data((newcoords[:,0], newcoords[:,1], newcoords[:,2]))
    points.set_data(newcoords[:,0], newcoords[:,1])
    points.set_3d_properties(newcoords[:,2])
    #points, = ax.plot(newcoords[:,0], newcoords[:,1], newcoords[:,2], 'o')
    return [points]

A = FuncAnimation(fig, animate, init_func = init, blit = True, interval = 25, repeat = True, frames = T)


plt.show()


#A.save("wave_gif.gif")






