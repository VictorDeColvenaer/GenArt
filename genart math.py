
import numpy as np
import matplotlib.pyplot as plt
import random

#figure, axes = plt.subplots()

fig = plt.figure(frameon=False)
#fig.set_size_inches(w,h)
axes = plt.Axes(fig, [0., 0., 1., 1.])
axes.set_axis_off()
fig.add_axes(axes)

#plt.axis('off')

z = 14000
a = float(input('geef een getal tussen 0 en 20:'))
b = float(input('geef een getal tussen 0 en 20:'))
c = float(input('geef een getal tussen 0 en 1: '))
axes.set_xlim(-1.2,1.2)
axes.set_ylim(-1.2,1.2)
#axes.set_facecolor('black')

colors = ['darkcyan','royalblue','blue','navy','cornflowerblue']
colors = colors * 14
random.shuffle(colors)

for j in range(35):
    for i in range(400):
        x = np.cos(a*np.pi*(i+400*(j-1))/z)*(1-c*(np.cos(b*np.pi*(i+400*(j-1))/z)) ** 2)
        y = np.sin(a*np.pi*(i+400*(j-1))/z)*(1-c*(np.cos(b*np.pi*(i+400*(j-1))/z)) ** 2)
        radius = 1/200 + 0.1*(np.sin(52*np.pi*(i+400*(j-1))/z)) ** 4
        cc = plt.Circle(( x , y ), radius, fill = False, color = colors[j], alpha = 0.08)
        axes.set_aspect(1)
        axes.add_artist(cc)

plt.savefig('genart.svg', format = 'svg',dpi = 1200)
plt.savefig('genart.pdf', format = None, dpi = 1200)
plt.show()
