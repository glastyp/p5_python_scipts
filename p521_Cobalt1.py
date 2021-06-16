"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import matplotlib.pyplot as plt

# Title for input- and output-file
TITLE = "Cobalt1"

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/521/David/figs/%s.pdf" % TITLE

source_filename = "%s.txt" % TITLE

xlabel = "Kanal"
ylabel = "Anzahl Ereignisse"
title = "$^{60}$Co-Spektrum mit Szintillations-Detektor"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[2]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s=10, linewidths = 0.4, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)