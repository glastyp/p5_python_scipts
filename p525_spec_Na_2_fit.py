"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/525/David/figs/spec_Na_4_fit.pdf"

source_filename = "spec_Na_2.txt"

xlabel = "Kanäle"
ylabel = "Anzahl Ereignisse"
title = "Barium-Spektrum mit Anpassungsfunktionen"

def f(x, a, b, c, d):
    return a*np.exp(-(x-b)**2/(2*c**2)) + d

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

a = 140

b = 7307

c = 200

d = 10

params = (a, b, c, d)

fit_params, pcov = scipy.optimize.curve_fit(f, analog, gate,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitanalog = np.linspace(analog[0], analog[-1],num=10000)
fitgate = f(fitanalog, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s = 10,linewidths = 0.4, label="Messwerte", zorder=1)   

plt.plot(fitanalog, fitgate, color = 'blue', label="Anpassung", zorder=2)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)