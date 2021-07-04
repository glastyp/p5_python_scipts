"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file
TITLE = "winkelverteilung"

source_filename = "%s.txt" % TITLE

output_filename = "D:/arbeitsplatz/Documents/Sciebo/Physik/FS 6 P5/P5-Protokolle/518/David/figs/%s.pdf" % TITLE

xlabel = "Winkel $\\theta$ in Grad"
ylabel = "Anzahl Ereignisse"
title = "Winkelverteilung der Höhenstrahlung"

def f(x, a):
    return a*(np.cos(x/180*np.pi)**2)

data = open(source_filename, 'r')
lines=data.readlines()

x=[]
y=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
data.close()

params = (np.max(x))

fit_params, pcov = scipy.optimize.curve_fit(f, x, y, p0 = params)
perr = np.sqrt(np.diag(pcov))

print(fit_params, perr)

fitx = np.linspace(np.min(x), np.max(x), 10000)
fity = f(fitx, fit_params[0])

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.scatter(x, y, color='black', marker = '+', s=30, linewidths = 0.7, label="Messwerte", zorder=2)  

plt.figtext(0.5,0.22,  
            "Anpassung: $f(\\theta)=\\alpha \cdot \cos^2(\\theta)$ \n $a=%g \pm %g$"%(round(fit_params[0],0), round(perr[0],0)), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)