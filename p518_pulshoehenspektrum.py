# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:04:31 2021

@author: Wörk
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file

output1_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/result_pulshoehenspektrum.pdf"
output2_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/pulshoehenspektrum.pdf"

source_filename = "alpha_214.txt"

xlabel = "Kanal"
ylabel = "Anzahl Ereignisse"
title = "Pulshöhenspektrum der Winkelverteilungsmessung"

data = open(source_filename, 'r')
lines=data.readlines()

analog = []
gate = []

for i in lines:
    analog.append(float(i.split()[0]))
    gate.append(float(i.split()[1]))

data.close()

fig_U = plt.figure(dpi=400)

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.scatter(analog, gate, color='black', marker = '+', s=20, linewidths = 0.4, label="Messwerte", zorder=10)   

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output1_filename)

def f(x, a, b, c, d):
    e1 = (x-b)/c
    e2 = (x-b)/d
    return a * np.exp(-1/2*(e1+np.exp(-1*e2)))

# def f(x, a, b, c, d):
#     return x+a+b+c+d

params = (200, 360, 70, 70)

fit_params, pcov = scipy.optimize.curve_fit(f, analog[20:800], gate[20:800], p0 = params)
perr = np.sqrt(np.diag(pcov))

print(fit_params, perr)

fitx = np.linspace(21, 800, 10000)
fity = f(fitx, *fit_params)

fig_2U = plt.figure(dpi=400)

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.scatter(analog[20:800], gate[20:800], color='black', marker = '+', s=20, linewidths = 0.4, label="Messwerte", zorder=10)   

plt.figtext(0.48,0.145,  
            "$f(x)=a\cdot \exp(-\\frac{1}{2}(\\frac{x-b}{c} + \exp(\\frac{x-b}{d})))$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $c=%g \pm %g$ \n $d=%g \pm %g$"%(round(fit_params[0],1), round(perr[0],1), round(fit_params[1],1), round(perr[1],1), round(fit_params[2],1), round(perr[2],1), round(fit_params[3],1), round(perr[3],1)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.6, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_2U.savefig(output2_filename)