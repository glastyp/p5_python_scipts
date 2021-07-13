"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import matplotlib.pyplot as plt


TITLE = "schwellenkurve_lebensdauer_1"

output_filename = "%s.pdf" % TITLE

source_filename = "schwell.txt"

xlabel = "D1 in mV"
ylabel = "$I_n$ in ‰"
title = "Variation der ersten Diskriminatorschwelle"

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

plt.scatter(analog, gate, color='black', marker = '+', s=30, linewidths = 0.5, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)

TITLE = "schwellenkurve_lebensdauer_2"

output_filename = "%s.pdf" % TITLE

source_filename = "schwell.txt"

xlabel = "D2 in mV"
ylabel = "$I_n$ in ‰"
title = "Variation der zweiten Diskriminatorschwelle"

data = open(source_filename, 'r')
lines=data.readlines()

Dis = []
koin = []

for x in lines:
    Dis.append(float(x.split()[1]))
    koin.append(float(x.split()[3]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(Dis, koin, color='black', marker = '+', s=30, linewidths = 0.5, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)
