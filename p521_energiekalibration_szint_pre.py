"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file
TITLE = "energiekalibration_szint_pre"

output_filename = "D:/david/Documents/Physik/FS 6 P5/P5/521/David/figs/%s.pdf" % TITLE

source_filename = "%s.txt" % TITLE

xlabel = "Energie"
ylabel = "Kanal"
title = "Emissions-Linien und jeweilige Kanäle des MCA; Vorauswahl"

def f(x, a, b):
    return a*x + b

def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i] , a, b))/s[i])**2
    return chi

data = open(source_filename, 'r')
lines=data.readlines()

x=[]
y=[]
dy=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    dy.append(float(i.split()[2]))
data.close()

fit_params, pcov = scipy.optimize.curve_fit(f, x, y, sigma=dy)
chi2red = chi2(x, y, dy, f, fit_params[0], fit_params[1])

perr = np.sqrt(np.diag(pcov))

fitx = np.linspace(0, 1500,num=10)
fity = f(fitx, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.xlim(0, 1500)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(x, y, yerr = dy, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   


plt.figtext(0.68,0.22,  
            "Anpassung: $f(x)=a\cdot x + b$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params[0],3), round(perr[0],3),round(fit_params[1],1), round(perr[1],1) ,chi2red), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)