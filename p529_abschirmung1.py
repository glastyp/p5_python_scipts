"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f1(x, a):
    return x*a

def f2(x, a, b):
    return x*a + b

def chi1(x, y, s, f, a):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f1(x[i] , a))/s[i])**2
    return chi

def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f2(x[i] , a, b))/s[i])**2
    return chi

output_filename1 = "plt_3_1.pdf"

output_filename2 = "plt_3_2.pdf"

output_filename3 = "plt_3_3.pdf"

output_filename4 = "plt_3_4.pdf"

source_filename1 = "dat_3_1.txt"

source_filename2 = "dat_3_2.txt"

data1 = open(source_filename1, 'r')
lines=data1.readlines()

R1=[]
dR1=[]
d1=[]

for x in lines:
    d1.append(float(x.split()[0]))
    R1.append(float(x.split()[1]))
    dR1.append(float(x.split()[2]))
data1.close()

data2 = open(source_filename2, 'r')
lines=data2.readlines()

R2=[]
dR2=[]
d2=[]

for x in lines:
    d2.append(float(x.split()[0]))
    R2.append(float(x.split()[1]))
    dR2.append(float(x.split()[2]))
data1.close()

fit_params11, pcov11 = scipy.optimize.curve_fit(f1, d1, R1, sigma=dR1)
chi2red11 = chi1(d1, R1, dR1, f1, fit_params11[0])

fit_params21, pcov21 = scipy.optimize.curve_fit(f2, d1, R1, sigma=dR1)
chi2red21 = chi2(d1, R1, dR1, f2, fit_params21[0], fit_params21[1])

perr11 = np.sqrt(np.diag(pcov11))
perr21 = np.sqrt(np.diag(pcov21))

fitx1 = np.linspace(d1[-1]-0.1*d1[0], 1.1*d1[0],num=10)
fity11 = f1(fitx1, *fit_params11)
fity21 = f2(fitx1, *fit_params21)


fit_params12, pcov12 = scipy.optimize.curve_fit(f1, d2, R2, sigma=dR2)
chi2red12 = chi1(d2, R2, dR2, f1, fit_params12[0])

fit_params22, pcov22 = scipy.optimize.curve_fit(f2, d2, R2, sigma=dR2)
chi2red22 = chi2(d2, R2, dR2, f2, fit_params22[0], fit_params22[1])

perr12 = np.sqrt(np.diag(pcov12))
perr22 = np.sqrt(np.diag(pcov22))

fitx2 = np.linspace(d2[-1]-0.1*d2[0], 1.1*d2[0],num=10)
fity12 = f1(fitx2, *fit_params12)
fity22 = f2(fitx2, *fit_params22)

fig_U1 = plt.figure(dpi=400)

plt.title("Abschirmung von Aluminium",y=1.08)
plt.xlabel("Dicke $d/\,\mathrm{mm}$")
plt.ylabel("$-\ln(R'/R_0')$")

plt.plot(fitx1, fity11, color = 'r', label="Anpassung", zorder=2)

plt.errorbar(d1, R1, yerr = dR1, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   


plt.figtext(0.68,0.22,  
            "Anpassung: $f(x)=a\cdot x$\n $a=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params11[0],3), round(perr11[0],3) ,chi2red11), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U1.savefig(output_filename1)


fig_U3 = plt.figure(dpi=400)

plt.title("Abschirmung von Aluminium",y=1.08)
plt.xlabel("Dicke $d/\,\mathrm{mm}$")
plt.ylabel("$-\ln(R'/R_0')$")

plt.plot(fitx2, fity12, color = 'r', label="Anpassung mit Zr-Filter", zorder=2) 


plt.errorbar(d2, R2, yerr = dR2, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte mit Zr-Filter", zorder=10) 

plt.figtext(0.68,0.22,  
            "Anpassung mit Zr-Filter: $f(x)=a\cdot x$\n $a=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params12[0],3), round(perr12[0],3) ,chi2red12), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U3.savefig(output_filename3)

fig_U2 = plt.figure(dpi=400)

plt.title("Abschirmung von Aluminium",y=1.08)
plt.xlabel("Dicke $d/\,\mathrm{mm}$")
plt.ylabel("$-\ln(R'/R_0')$")

plt.plot(fitx1, fity21, color = 'r', label="Anpassung", zorder=2)


plt.errorbar(d1, R1, yerr = dR1, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   

plt.figtext(0.68,0.22,  
            "Anpassung: $f(x)=a\cdot x + b$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params21[0],3), round(perr21[0],3), round(fit_params21[1],3), round(perr21[1],3) ,chi2red21), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U2.savefig(output_filename2)

fig_U4 = plt.figure(dpi=400)

plt.title("Abschirmung von Aluminium",y=1.08)
plt.xlabel("Dicke $d/\,\mathrm{mm}$")
plt.ylabel("$-\ln(R'/R_0')$")

plt.plot(fitx2, fity22, color = 'r', label="Anpassung mit Zr-Filter", zorder=2)
   

plt.errorbar(d2, R2, yerr = dR2, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte mit Zr-Filter", zorder=10)


plt.figtext(0.65,0.22,  
            "Anpassung mit Zr-Filter: $f(x)=a\cdot x + b$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params22[0],3), round(perr22[0],3), round(fit_params22[1],3), round(perr22[1],3) ,chi2red22), 
            horizontalalignment ="center", 
            wrap = True, fontsize = 10,  
            bbox ={'facecolor':'white',  
                   'alpha':0.7, 'pad':3})

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U4.savefig(output_filename4)