"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b):
    return x*a + b

def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i] , a, b))/s[i])**2
    return chi

output_filename = "plt_1_3z.pdf"

source_filename = "dat_1_3.txt"

data1 = open(source_filename, 'r')
lines=data1.readlines()

D=[]
dD=[]
h=[]
dh=[]

for x in lines:
    D.append(float(x.split()[0]))
    dD.append(float(x.split()[1]))
    h.append(float(x.split()[2]))
    dh.append(float(x.split()[3]))
data1.close()

fig_U = plt.figure(dpi=400)

plt.title("Äquivalentdosis in Abhängigkeit zum Abstand",y=1.08)
# plt.ylim(-5,70)
# plt.xlim(-2,37)

fit_params, pcov = scipy.optimize.curve_fit(f, D, h, sigma=dh)
chi2red = chi2(D, h, dh, f, fit_params[0], fit_params[1])

plt.xlabel("Abstand zur Anode $1/D^2/\,\mathrm{mm}^{-2}$")
    

plt.ylabel("Mittlere Äquivalentdosis $\\langle h \\rangle  /\,\\mu \mathrm{Sv/s}$")


perr = np.sqrt(np.diag(pcov))

fitx = np.linspace(D[-1]-0.1*D[0], 1.1*D[0],num=10)
fity = f(fitx, *fit_params)

plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(D, h, xerr = dD, yerr = dh, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   

plt.figtext(0.68,0.22,  
            "Anpassung: $f(x)=a\cdot x + b$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params[0],3), round(perr[0],3), round(fit_params[1],3), round(perr[1],3) ,chi2red), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)