import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

# Constants - all values from Carroll and Ostlie
me = 9.10938215 * 10**(-31) # kg
k = 1.3806504 * 10**(-23) # J K^-1
h = 6.62606896 * 10**(-34) # J s
eV = 1.602176487 * 10**(-19) # J
chi = 13.6 * eV

# Taken from my student number
ne = 51 * 10**19 # m^-3

# A list of the temperatures
temp_list = np.arange(2000, 22000, 0.1)

#########
#       #
#   H   #
#       #
#########

# Assume ZII = 1 as H II is just a proton, which has no degeneracy
ZII = 1

# ZI for H as a function of temperature
def ZI_H(T):
    return 2 + 8*np.exp(-51/(5*k*T)) + 18*np.exp(-544/(45*k*T))

# The Saha equation for H
def saha_H(T):
    return 2*ZII/(ne*ZI_H(T)) * ((2*np.pi*me*k*T)/(h**2))**(3/2) * np.exp(-chi/(k*T))

# The ionisation fraction for H
def frac_H(T):
    return saha_H(T)/(1 + saha_H(T))

fraction = frac_H(temp_list)

# Find where 90% of the H atoms are ionised
intersect = np.argwhere(np.diff(np.sign(0.9-fraction))).flatten()
intersect_temp = temp_list[intersect][0]
print("The temperature at which 90% of the H atoms are ionised is "+ str(intersect_temp) + " K")

# Plot the graph
plt.plot(temp_list, fraction, label=r'$N_{II}/N_{total}$')
plt.scatter(intersect_temp, 0.9, s=200, marker='+', label='90% H II', color='red')
plt.xlabel("T (K)")
plt.ylabel(r"$N_{II}/N_{total}$")
plt.title(r"The fraction of ionised hydrogen ($N_{II}/N_{total}$) in the star against temperature (T)")
plt.annotate('90% ionisation occurrs\nat ' + str(np.rint(intersect_temp))[:-2] + ' K', xy=(intersect_temp + 200, 0.89), xytext=(15000, 0.6), arrowprops=dict(arrowstyle="->"))
plt.legend()
plt.show()

##########
#        #
#   Ca   #
#        #
##########

# Values given in the assignment
ZI = 1.32
ZII = 2.3
chi = 6.11 * eV

# The Saha equation for Ca
def saha_Ca(T):
    return 2*ZII/(ne*ZI) * ((2*np.pi*me*k*T)/(h**2))**(3/2) * np.exp(-chi/(k*T))

# The ionisation fraction for Ca
def frac_Ca(T):
    return saha_Ca(T)/(1 + saha_Ca(T))

fraction = frac_Ca(temp_list)

# Plot the graph
plt.plot(temp_list, fraction, label=r'$N_{II}/N_{total}$')
plt.xlabel("T (K)")
plt.ylabel(r"$N_{II}/N_{total}$")
plt.title(r"The fraction of singly ionised calcium ($N_{II}/N_{total}$) in the star against temperature (T)")
plt.show()