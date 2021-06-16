"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# Title for input- and output-file
TITLE = "gauss_fit_Co_szint"
FILE = "Cobalt1"
PARAMS = "%s_params.txt" % TITLE

output_filename = "D:/Uni/Physik/physik562/P5-Protokolle/P5-Protokolle/521/Rohdaten/plotting/%ss.pdf" % TITLE

source_filename = "%s.txt" % FILE

xlabel = "Kanal"
ylabel = "Anzahl Ereignisse"
title = "Spektrum der Cobalt-Quelle mit Anpassung (Szi)"
peaks = 4
width = 500

def gaus(x, a, b, c):
    return a*np.exp(-(x-b)**2/(2*c**2))

def f(x, a, b, c, d, e):
    return gaus(x, a, b, c) + x*d + e

data = open(source_filename, 'r')
lines=data.readlines()

x=[]
y=[]

sigma=0
for i in lines:
    x.append(float(i.split()[0]))
    y.append(float(i.split()[2]))
    sigma = sigma + float(i.split()[2])
data.close()
print(sigma)

paramdata = open(PARAMS, 'r')
lines = paramdata.readlines()


params = []

for j in range(3):
    for i in lines:
        params.append(float(i.split()[j]))
paramdata.close()

d = -0.01
e = 100

for i in range(2):
    for j in range(peaks):
        params.append(d)
    for j in range(peaks):
        params.append(e)

fity = []
fitx = []

for i in range(peaks):
    
    if(i==4):
        width=350
    
    cp = int(params[i+peaks]) # cp: current peak
    print(cp)
    cpar = [params[i], params[i+peaks], params[i + 2*peaks], params[i + 3*peaks], params[i + 4*peaks]]
    
    fit_params, pcov = scipy.optimize.curve_fit(f, x[cp -width:cp + width], y[cp-width:cp+width], p0=cpar)
    perr = np.sqrt(np.diag(pcov))
    
    print(fit_params)
    print(perr)
    print("---------------------------------------")
    
    for j in range(2*width):
        fity.append(f(x[cp+j-width],*fit_params))
        fitx.append(x[cp+j-width])

fig_U = plt.figure(dpi=400)

plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.scatter(x, y, color='black', marker = '+', s=10, linewidths = 0.4, label="Messwerte", zorder=1)  

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)