"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


output_filename1 = "plt_3_5.pdf"

output_filename2 = "plt_3_6.pdf"


source_filename1 = "dat_3_5.txt"

source_filename2 = "dat_3_4.txt"

source_filename3 = "dat_3_5.txt"

source_filename4 = "dat_3_6.txt"

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
data2.close()

data3 = open(source_filename3, 'r')
lines=data3.readlines()

R3=[]
dR3=[]
d3=[]

for x in lines:
    d3.append(float(x.split()[0]))
    R3.append(float(x.split()[1]))
    dR3.append(float(x.split()[2]))
data3.close()

data4 = open(source_filename4, 'r')
lines=data4.readlines()

R4=[]
dR4=[]
d4=[]

for x in lines:
    d4.append(float(x.split()[0]))
    R4.append(float(x.split()[1]))
    dR4.append(float(x.split()[2]))
data4.close()

fig_U1 = plt.figure(dpi=400)


plt.title("Abschirmung verschiedener Materialien für $\\mu'$",y=1.08)
plt.xlabel("Kernladungszahl $Z$")
plt.ylabel("$\\mu/\mathrm{mm}^{-1}$")

plt.errorbar(d1, R1, yerr = dR1, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)

plt.errorbar(d2, R2, yerr = dR2, fmt='.', color='red',
             markersize=2, ecolor='red', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte mit Zr-Filter", zorder=10) 

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U1.savefig(output_filename2)


fig_U2 = plt.figure(dpi=400)


plt.title("Abschirmung verschiedener Materialien für $\\mu$",y=1.08)
plt.xlabel("Kernladungszahl $Z$")
plt.ylabel("$\\mu/\mathrm{mm}^{-1}$")

plt.errorbar(d3, R3, yerr = dR3, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)

plt.errorbar(d4, R4, yerr = dR4, fmt='.', color='red',
             markersize=2, ecolor='red', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte mit Zr-Filter", zorder=10) 

plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U2.savefig(output_filename1)