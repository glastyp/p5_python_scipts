# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""

import matplotlib.pyplot as plt

# Title for input- and output-file
TITLE = "Bodenprobe"

output_filename = "D:/Uni/Physik/physik562/P5-Protokolle/P5-Protokolle/521/Rohdaten/plotting/%s.pdf" % TITLE

source_filename = "%s.txt" % TITLE

xlabel = "Kanal"
ylabel = "# Ereignisse"
title = "Langzeitmessung von 1 kg Blumenerde"


data = open(source_filename, 'r')
lines=data.readlines()[1:]

x1=[]
y1=[]
dy1=[]
hilf=0
for i in lines:
    x1.append(float(i.split()[0]))
    dy1.append(float(i.split()[1]))
    y1.append(float(i.split()[2]))
    hilf=hilf+float(i.split()[2])
print(hilf)
data.close()


fig_U = plt.figure(dpi=400)
plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.xlim(0, 8000)


plt.errorbar(x1, y1, yerr = dy1, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   


plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)

TITLE = "Bodenprobe_untergrund"

output_filename = "D:/Uni/Physik/physik562/P5-Protokolle/P5-Protokolle/521/Rohdaten/plotting/%s.pdf" % TITLE

source_filename = "%s.txt" % TITLE

xlabel = "Kanal"
ylabel = "# Ereignisse"
title = "Langzeitmessung des Untergrundes"


data = open(source_filename, 'r')
lines=data.readlines()[1:]

x2=[]
y2=[]
dy2=[]
hilf=0
for i in lines:
    x2.append(float(i.split()[0]))
    dy2.append(float(i.split()[1]))
    y2.append(float(i.split()[2]))
    hilf=hilf+float(i.split()[2])
print(hilf)
data.close()


fig_U = plt.figure(dpi=400)
plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.xlim(0, 8000)


plt.errorbar(x2, y2, yerr = dy2, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   


plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)

TITLE = "Diff"

output_filename = "D:/Uni/Physik/physik562/P5-Protokolle/P5-Protokolle/521/Rohdaten/plotting/%s.pdf" % TITLE

xlabel = "Kanal"
ylabel = "# Ereignisse"
title = "Bereinigte Langzeitmessung von 1 kg Blumenerde"

fig_U = plt.figure(dpi=400)
plt.title(title,y=1.08)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.xlim(0, 8000)

x=[0]*len(x1)
y=[0]*len(x1)
dy=[0]*len(x1)

hilf=0

for i in range(len(x1)-10):
    x[i]=x1[i]
    y[i]=y1[i]-y2[i+4]
    hilf=hilf+y[i]
    dy[i]=(y1[i]**2+y2[i]**2)**0.5

print(hilf)
plt.errorbar(x, y, yerr = 0, fmt='.', color='black',
             markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
             capsize=2, label="Messwerte", zorder=10)   


plt.legend(loc='best')

plt.grid(True, zorder=0)

fig_U.savefig(output_filename)