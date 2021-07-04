"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import matplotlib.pyplot as plt

# Title for input- and output-file
TITLE = "schwellenkurve_winkelverteilung_D12"

output_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5/518/David/figs/%s.pdf" % TITLE

source_filename = "schwellenkurve_winkelverteilung.txt"

xlabel = "Disikriminatorschwelle"
ylabel = "Anzahl Ereignisse D12"
title = "Diskriminatorschwelle und D12"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []
norm = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[1]))
    norm.append(float(x.split()[4]))
data.close()

# for i in range(len(gate)):
#     gate[i] = gate[i]/norm[i]

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s=30, linewidths = 0.5, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)

#-----------------------------------------------------------------------

TITLE = "schwellenkurve_winkelverteilung_KOINZ"

output_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/%s.pdf" % TITLE

source_filename = "schwellenkurve_winkelverteilung.txt"

xlabel = "Disikriminatorschwelle"
ylabel = "Anzahl Ereignisse Koinzidenz"
title = "Diskriminatorschwelle und Koinzidenz"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[3]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s=30, linewidths = 0.5, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)

#-----------------------------------------------------------------------

TITLE = "schwellenkurve_winkelverteilung_ODER"

output_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/%s.pdf" % TITLE

source_filename = "schwellenkurve_winkelverteilung.txt"

xlabel = "Disikriminatorschwelle"
ylabel = "Anzahl Ereignisse ODER"
title = "Diskriminatorschwelle und ODER"

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

#-----------------------------------------------------------------------

TITLE = "schwellenkurve_winkelverteilung_D25"

output_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/%s.pdf" % TITLE

source_filename = "schwellenkurve_winkelverteilung.txt"

xlabel = "Disikriminatorschwelle"
ylabel = "Anzahl Ereignisse D25"
title = "Diskriminatorschwelle und D25"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[4]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s=30, linewidths = 0.5, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)