"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

m = 0.150*32.4

for i in range(2):

    output_filename = "plt_1_2_%s.pdf"%str(i+5)
    
    source_filename1 = "dat_1_2_%s.txt"%str(1+i*1)
    source_filename2 = "dat_1_2_%s.txt"%str(3+i*1)
    
    data1 = open(source_filename1, 'r')
    lines=data1.readlines()
    U1=[]
    dU1=[]
    I_C1=[]
    dI_C1=[]

    for x in lines:
        U1.append(float(x.split()[0]))
        dU1.append(float(x.split()[1]))
        I_C1.append(float(x.split()[2]))
        dI_C1.append(float(x.split()[3]))
    data1.close()

    for j in range(len(I_C1)):
        I_C1[j]=I_C1[j]*1/m
        dI_C1[j]=dI_C1[j]*1/m

    
    data1 = open(source_filename2, 'r')
    lines=data1.readlines()
    U2=[]
    dU2=[]
    I_C2=[]
    dI_C2=[]

    for x in lines:
        U2.append(float(x.split()[0]))
        dU2.append(float(x.split()[1]))
        I_C2.append(float(x.split()[2]))
        dI_C2.append(float(x.split()[3]))
    data1.close()
    
    for j in range(len(I_C2)):
        I_C2[j]=I_C2[j]*1/m
        dI_C2[j]=dI_C2[j]*1/m
    
    fig_U = plt.figure(dpi=400)
    
    if(i==0):
        plt.title("Äquivalentdosis in Abhängigkeit vom Emissionsstrom",y=1.08)
        # plt.ylim(-5,70)
        # plt.xlim(-2,37)
        plt.xlabel("Emissionsstrom $I/\,\mathrm{mA}$")
    else:
        plt.title("Äquivalentdosis in Abhängigkeit der Röhrenspannung",y=1.08)
        # plt.ylim(-5,70)
        # plt.xlim(-2,37)
        plt.xlabel("Röhrenspannung $U/\,\mathrm{V}$")
        
    
    plt.ylabel("Mittlere Äquivalentdosis $\\langle h \\rangle  /\,\mathrm{mSv/s}$")
    
    
    plt.errorbar(U2, I_C2, xerr = dU2, yerr = dI_C2, fmt='.', color='red',
                 markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="Molybdän-Röhre", zorder=10)
    
    plt.errorbar(U1, I_C1, xerr = dU1, yerr = dI_C1, fmt='.', color='black',
                 markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="Kupfer-Röhre", zorder=10)   
    
    
    plt.legend(loc='best')
    
    plt.grid(True, zorder=0)
    
    fig_U.savefig(output_filename)