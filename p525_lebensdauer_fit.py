"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""
import math as m
from scipy.special import erf
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b, k, s):
    return a*np.exp(1/b*(-x+1/b*s*s/2+k))*(erf((x-1/b*s**2-k)/(m.sqrt(2)*s))+1)


output_filename = "D:/Uni/Physik/physik562/P5-Protokolle/P5-Protokolle/525/Rohdaten/plotting/lebensdauer_fit.pdf"

source_filename = "lebensdauer.txt"

xlabel = "Kanäle"
ylabel = "Anzahl Ereignisse"
title = "Zerfall des angeregten $^{133}$Cs"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for x in lines:
    analog.append(float(x.split()[0]))
    gate.append(float(x.split()[1]))
data.close()

fig_U = plt.figure(dpi=400)

a = 200
b = 300
s = 50
k = 1400

params = (a, b, k, s)

fit_params, pcov = scipy.optimize.curve_fit(f, analog, gate, p0=params)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitanalog = np.linspace(analog[0]-100, analog[-1]+100,num=10000)
fitgate = f(fitanalog, *fit_params)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.ylim(-5,180)

plt.scatter(analog, gate, color='black', marker = '+', linewidths = 0., s = 10, label="Messwerte", zorder=2)   

plt.plot(fitanalog, fitgate, color = 'blue', label="Anpassung", zorder=4)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)