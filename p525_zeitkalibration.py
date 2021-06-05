# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:02:15 2021

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/525/David/figs/zeitkalibration.pdf"

source_filename = "zeitkalibration.txt"

xlabel = "$t/$ns"
ylabel = "Kanäle"
title = "Zeitkalibration des TAC"

def f(x, a, b):
    return a*x + b


def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i], a, b))/s[i])**2
    return chi

data = open(source_filename, 'r')
lines=data.readlines()

t = (8, 24, 40, 56, 72)
channel = []
dchannel = []

for x in lines:
    channel.append(float(x.split()[1]))
    dchannel.append(float(x.split()[4]))
data.close()

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

fit_params, pcov = scipy.optimize.curve_fit(f, t, channel)

print(fit_params)
perr = np.sqrt(np.diag(pcov))
print(perr)

fitt = np.linspace(t[0]-5, t[-1]+5,num=10000)
fitchannel = f(fitt, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.xlim(t[0]-5, t[-1]+5)

plt.errorbar(t, channel, yerr = dchannel, fmt='x', color='black',
                 markersize=5, lw = 2, ecolor='black', elinewidth=0.5, markeredgewidth=0.4,
                 capsize=2, label="Spektrallinienmaxima", zorder=10)   
    
plt.figtext(0.65,0.2,  
            "Anpassung: $f(x)=\\alpha \cdot x + \\beta$\n $\\alpha=%g \pm %g$ \n $\\beta=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params[0],2), round(perr[0],2), round(fit_params[1],2), round(perr[1],2), round(chi2(t, channel, dchannel, f, *fit_params),2)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                    'alpha':0.7, 'pad':3})   

plt.plot(fitt, fitchannel, color = 'blue', label="Anpassung", zorder=5)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)