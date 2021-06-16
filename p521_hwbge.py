"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file
TITLE = "hwbge"

output_filename = "%s.pdf" % TITLE

source_filename = "%s.txt" % TITLE

xlabel = "${E_{\\gamma}}$"
ylabel = "$(\Delta E)^2$"
title = "Halbwertsbreite gegen Wurzel der Photonenenergie"

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
chi2red = round(chi2(x, y, dy, f, fit_params[0], fit_params[1]),0)

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


plt.figtext(0.65,0.18,  
            "Anpassung: $f(x)=\\alpha^2\cdot x + \\beta$\n $\\alpha=%g \pm %g$ \n $\\beta=%g \pm %g$ \n $\chi^2=%g$"%(round(np.sqrt(fit_params[0]),3), round(1/2*(fit_params[0])**(-1/2)*perr[0],3),round(fit_params[1],3), round(perr[1],3) ,chi2red), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

print(fit_params)
print(perr)

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)