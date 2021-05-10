"""
Created on Tue Nov 24 14:19:15 2020

@author: david
"""


import matplotlib.pyplot as plt


for i in range(2):
    
    output_filename = "plt_1_1_%s.pdf"%str(i+1)
    
    source_filename1 = "dat_1_1_%s.txt"%str(1+i*3)
    
    source_filename2 = "dat_1_1_%s.txt"%str(2+i*3)

    source_filename3 = "dat_1_1_%s.txt"%str(3+i*3)
    
    data1 = open(source_filename1, 'r')
    lines=data1.readlines()
    U_C1=[]
    dU_C1=[]
    I_C1=[]
    dI_C1=[]

    for x in lines:
        U_C1.append(float(x.split()[0]))
        dU_C1.append(float(x.split()[1]))
        I_C1.append(float(x.split()[2]))
        dI_C1.append(float(x.split()[3]))
    data1.close()
    
    data2 = open(source_filename2, 'r')
    lines=data2.readlines()
    U_C2=[]
    dU_C2=[]
    I_C2=[]
    dI_C2=[]
    
    for x in lines:
        U_C2.append(float(x.split()[0]))
        dU_C2.append(float(x.split()[1]))
        I_C2.append(float(x.split()[2]))
        dI_C2.append(float(x.split()[3]))
    data2.close()
    
    data3 = open(source_filename3, 'r')
    lines=data3.readlines()
    U_C3=[]
    dU_C3=[]
    I_C3=[]
    dI_C3=[]
    
    for x in lines:
        U_C3.append(float(x.split()[0]))
        dU_C3.append(float(x.split()[1]))
        I_C3.append(float(x.split()[2]))
        dI_C3.append(float(x.split()[3]))
    data3.close()
    
    fig_U = plt.figure(dpi=400)
    
    if(i==0):
        plt.title("Ionisation mit Molybdän-Röhre",y=1.08)
    else:
        plt.title("Ionisation mit Kupfer-Röhre",y=1.08)
        
    plt.xlabel("Kondensatorspannung $U_\mathrm{C}/\,\mathrm{V}$")
    plt.ylabel("Ionisationsstrom $I_\mathrm{C}/\,\mathrm{nA}$")
    
    plt.errorbar(U_C1, I_C1, xerr = dU_C1, yerr = dI_C1, fmt='.', color='b',
                 markersize=2, ecolor='b', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="$U=15\,$kV", zorder=10)

    plt.errorbar(U_C2, I_C2, xerr = dU_C2, yerr = dI_C2, fmt='.', color='r',
                 markersize=2, ecolor='r', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="$U=25\,$kV", zorder=10)
    
    plt.errorbar(U_C3, I_C3, xerr = dU_C3, yerr = dI_C3, fmt='.', color='black',
                 markersize=2, ecolor='black', elinewidth=0.5, markeredgewidth=1,
                 capsize=2, label="$U=35\,$kV", zorder=10)    
    
    plt.legend(loc='best')
    
    plt.grid(True, zorder=0)
    
    fig_U.savefig(output_filename)