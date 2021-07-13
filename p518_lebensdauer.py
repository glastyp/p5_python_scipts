"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file
TITLE = "lebensdauer"

source_filename = "%s.txt" % TITLE

output_filename = "%s.pdf" % TITLE

xlabel = "$1 \mu$s - Bins"
ylabel = "Anzahl Ereignisse"
title = "Ereignisse gegen Zeit"

def f(x, a, b,c):
    return a*np.exp(x/b)+c

data = open(source_filename, 'r')
lines=data.readlines()

x=[]
y=[]

for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
data.close()
for i in range(len(x)):
    x[i]=x[i]-1
params = (np.max(x),-0.55,0)

fit_params, pcov = scipy.optimize.curve_fit(f, x, y, p0 = params)
perr = np.sqrt(np.diag(pcov))

print(fit_params, perr)

fitx = np.linspace(np.min(x), np.max(x), 10000)
fity = f(fitx, *fit_params)

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.scatter(x, y, color='black', marker = '+', s=30, linewidths = 0.7, label="Messwerte", zorder=2)  

plt.figtext(0.5,0.7,  
            "$f(t)=N_0\cdot \exp(-t/\\tau) + k$ \n $N_0=%g \pm %g$ \n $f=%g \pm %g$ \n $k=%g \pm %g$ "%(round(fit_params[0],0), round(perr[0],0),-round(fit_params[1],3), round(perr[1],3), round(fit_params[2],0), round(perr[2],0)),
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)