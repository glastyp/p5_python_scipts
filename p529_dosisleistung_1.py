"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a):
    return a*x


def chi2(x, y, s, f, a):
    chi = 0
    for i in range(len(x)):
        chi += ((y[i] - f(x[i],a))/s[i])**2
    return chi

for i in range(2):
    
    output_filename = "plt_1_2_%s.pdf"%str(i+1)
    
    source_filename = "dat_1_2_%s.txt"%str(1+i*2)
    
    data1 = open(source_filename, 'r')
    lines=data1.readlines()
    I=[]
    dI=[]
    I_C=[]
    dI_C=[]

    for x in lines:
        I.append(float(x.split()[0]))
        dI.append(float(x.split()[1]))
        I_C.append(float(x.split()[2]))
        dI_C.append(float(x.split()[3]))
    data1.close()
    
    fig_U = plt.figure(dpi=400)
    
    if(i==0):
        plt.title("Ionisation mit Molybdän-Röhre",y=1.08)
    else:
        plt.title("Ionisation mit Kupfer-Röhre",y=1.08)
        
    plt.xlabel("Emissionsstrom $I/\,\mathrm{mA}$")
    plt.ylabel("Ionisationsstrom $I_\mathrm{C}/\,\mathrm{nA}$")
    
    fit_params, pcov = scipy.optimize.curve_fit(f, I, I_C, sigma=dI_C)
    
#    print(fit_params)
    perr = np.sqrt(np.diag(pcov))
#    print(perr)
#    print(chi2(I, I_C, dI_C, f, fit_params[0], fit_params[1]))
    
    fitx = np.linspace(I[0]-0.1*I[-1], 1.1*I[-1],num=10)
    fity = f(fitx, *fit_params)
    
    plt.plot(fitx, fity, color = 'r', label="Anpassung", zorder=2)
    
    plt.errorbar(I, I_C, xerr = dI, yerr = dI_C, fmt='.', color='black',
                 markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="Messwerte", zorder=10)   
    
    plt.figtext(0.68,0.3,  
                "Anpassung: $f(x)=a\cdot x$\n $a=%g \pm %g$ \n $\chi^2=%g$"%(round(fit_params[0],3), round(perr[0],3), chi2(I, I_C, dI_C, f, fit_params[0])), 
                horizontalalignment ="center", 
                wrap = True, fontsize = 10,  
                bbox ={'facecolor':'white',  
                        'alpha':0.7, 'pad':3})
    
    plt.xlim(-0.1,1.1)
    
    plt.legend(loc='best')
    
    plt.grid(True, zorder=0)
    
    fig_U.savefig(output_filename)