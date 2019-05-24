import matplotlib.pyplot as plt
import numpy as np
import re
import matplotlib.animation as animation

# create a figure, axis and plot element 
fig, ax = plt.subplots(figsize=(10, 6))
ax.set(xlim=(0, 5), ylim=(0, 700)) 


#main
forceRegex = r"([0-9.Ee\-+]+)\s+\(+([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\)\s\(([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\)+\s\(+([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\s([0-9.Ee\-+]+)\)+"
t =[]
fx = []; fy = []; fz = []
px = []; py = []; pz = []
vx = []; vy = []; vz = []

pipefile = open('postProcessing/forcesOnFloatingObject/0/force.dat','r')
lines = pipefile.readlines()

for line in lines:
    match = re.search(forceRegex,line)
    if match:
        t.append(float(match.group(1)))
        fx.append(float(match.group(2)))
        fy.append(float(match.group(3)))
        fz.append(float(match.group(4)))
        px.append(float(match.group(5)))
        py.append(float(match.group(6)))
        pz.append(float(match.group(7)))
        vx.append(float(match.group(8)))
        vy.append(float(match.group(9)))
        vz.append(float(match.group(9)))



force = ax.plot([], [],'b',lw = 2)[0]
def animate(i):
        force.set_data(t[:i], fz[:i])
        

plt.title('30 Wedge Force')
plt.xlabel('time(s)')
plt.ylabel('Force(N)')

anim = animation.FuncAnimation(fig, animate, frames=len(t)-1) 
anim.save('forceAnimPlot.mp4', fps=100, extra_args=['-vcodec', 'libx264'])
plt.plot(t,fz)
plt.savefig('forcePlot.png')
plt.show()
