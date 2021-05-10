"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize



output_filename = "plt_2.pdf"

source_filename = "dat_2.txt"

data1 = open(source_filename, 'r')
lines=data1.readlines()
I=[]
dI=[]
N=[]

for x in lines:
    I.append(float(x.split()[0]))
    dI.append(float(x.split()[1]))
    N.append(float(x.split()[2]))
data1.close()

fig_U = plt.figure(dpi=400)

plt.title("Zählrate in Abhängigkeit des Emissionsstroms",y=1.08)
plt.xlabel("Emissionsstrom $I/\,\mathrm{mA}$")
    

plt.ylabel("Mittlere Zählrate $\\langle N/\mathrm{s} \\rangle$")


plt.errorbar(I, N, xerr = dI, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)

plt.legend(loc='best')

a = np.arange(0,1.1,0.1)

print(a)

plt.xticks(a)

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)