"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b):
    return a*x + b


def chi2(x, y, s, f, a, b):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i],a, b))/s[i])**2
    return chi

for i in range(2):
    
    x1 = 10
    
    x2 = 7
    
    
    output_filename = "plt_1_2_%s.pdf"%str(i+3)
    
    source_filename = "dat_1_2_%s.txt"%str(2+i*2)
    
    data1 = open(source_filename, 'r')
    lines=data1.readlines()
    U=[]
    dU=[]
    I_C=[]
    dI_C=[]

    for x in lines:
        U.append(float(x.split()[0]))
        dU.append(float(x.split()[1]))
        I_C.append(float(x.split()[2]))
        dI_C.append(float(x.split()[3]))
    data1.close()
    
    fig_U = plt.figure(dpi=400)
    
    if(i==0):
        plt.title("Ionisation mit Molybdän-Röhre",y=1.08)
        fit_params, pcov = scipy.optimize.curve_fit(f, U[x1:], I_C[x1:], sigma=dI_C[x1:])
        chi2red = chi2(U[x1:], I_C[x1:], dI_C[x1:], f, fit_params[0], fit_params[1])
        plt.ylim(-0.5,4.5)
    else:
        plt.title("Ionisation mit Kupfer-Röhre",y=1.08)
        fit_params, pcov = scipy.optimize.curve_fit(f, U[x2:], I_C[x2:], sigma=dI_C[x2:])
        chi2red = chi2(U[x2:], I_C[x2:], dI_C[x2:], f, fit_params[0], fit_params[1])
        plt.ylim(-5,70)
        
    plt.xlabel("Röhrenspannung $U/\,\mathrm{V}$")
    plt.ylabel("Ionisationsstrom $I_\mathrm{C}/\,\mathrm{nA}$")

    perr = np.sqrt(np.diag(pcov))
    
    fitx = np.linspace(U[0]-0.1*U[-1], 1.1*U[-1],num=10)
    fity = f(fitx, *fit_params)
    
    plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)
    
    plt.errorbar(U, I_C, xerr = dU, yerr = dI_C, fmt='.', color='black',
                 markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="Messwerte", zorder=10)   
    
    plt.figtext(0.3,0.5,  
                "Anpassung: $f(x)=a\cdot x +b$\n $a=%g \pm %g$ \n $b=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params[0],3), round(perr[0],3), round(fit_params[1],3),round(perr[1],3), chi2red), 
                horizontalalignment ="center", 
                wrap = True, fontsize = 10,  
                bbox ={'facecolor':'white',  
                       'alpha':0.7, 'pad':3})
    
    plt.xlim(-2,37)
    
    
    plt.legend(loc='best')
    
    plt.grid(True, zorder=0)
    
    fig_U.savefig(output_filename)