"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/525/David/figs/prompt_Na_12.pdf"

source_filename = "prompt_Na_12.txt"

xlabel = "Kanäle"
ylabel = "Anzahl Ereignisse"
title = "Prompt-Kurven des TAC"

def f(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))

def gaus5(x, *params):
    res = 0
    for i in range(5):
        res += f(x, params[i], params[i+5], params[i+10])
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

a1 = 43
a2 = 37
a3 = 35
a4 = 33
a5 = 32

b1 = 932
b2 = 1508
b3 = 2044
b4 = 2596
b5 = 3188

c1 = 100
c2 = 100
c3 = 100
c4 = 100
c5 = 100

a = (a1, a2, a3, a4, a5)
b = (b1, b2, b3, b4, b5)
c = (c1, c2, c3, c4, c5)

params = (a, b, c)

fit_params, pcov = scipy.optimize.curve_fit(gaus5, analog, gate,p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitanalog = np.linspace(analog[0], analog[-1],num=10000)
fitgate = gaus5(fitanalog, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s = 10,linewidths = 0.4, label="Messwerte", zorder=1)   

plt.plot(fitanalog, fitgate, color = 'blue', label="Anpassung", zorder=2)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)