"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/525/David/figs/spec_Ba_3_fit.pdf"

source_filename = "spec_Ba_3.txt"

xlabel = "Kanäle"
ylabel = "Anzahl Ereignisse"
title = "Barium-Spektrum mit Anpassungsfunktionen"

def f(x, a, b, c, d):
    return a*np.exp(-(x-b)**2/(2*c**2)) + d

def gaus4(x, *params):
    res = 0
    for i in range(4):
        res += f(x, params[i], params[i+4], params[i+8], params[12])
    return res

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

a1 = 1862
a2 = 706
a3 = 94
a4 = 209

b1 = 386
b2 = 1194
b3 = 4309
b4 = 5121

c1 = 50
c2 = 50
c3 = 100
c4 = 100

d = 10

a = (a1, a2, a3, a4)
b = (b1, b2, b3, b4)
c = (c1, c2, c3, c4)

params = (a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d)

fit_params, pcov = scipy.optimize.curve_fit(gaus4, analog, gate,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitanalog = np.linspace(analog[0], analog[-1],num=10000)
fitgate = gaus4(fitanalog, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s = 10,linewidths = 0.4, label="Messwerte", zorder=1)   

plt.plot(fitanalog, fitgate, color = 'blue', label="Anpassung", zorder=2)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)