"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import matplotlib.pyplot as plt

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/525/David/figs/lebensdauer.pdf"

source_filename = "lebensdauer.txt"

xlabel = "Kanäle"
ylabel = "Anzahl Ereignisse"
title = "Lebensdauermessung der Barium-Probe"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[1]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', linewidths = 0.4, s = 10, label="Messwerte", zorder=10)   


plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)