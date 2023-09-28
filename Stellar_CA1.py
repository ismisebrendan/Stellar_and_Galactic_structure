# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

##################
#                #
#   Question 3   #
#                #
##################

# Physical constants
c = 29979245800 # cm/s
h = 6.62607015e-27 # erg s
kb = 1.380649e-16 # erg/K 

# Flux given wavelength (l) and temperature (T) in cgs units.
def flux(l, T):
    return (2*np.pi*h*c**2)/(l**5) * 1/(np.exp( (h*c)/(l*kb*T) ) - 1) # erg s^-1 cm^-3


wavelengths = np.arange(200e-8, 20000e-8, 1e-8) # in cm
fluxes = flux(wavelengths, 6451)

plt.plot(wavelengths, fluxes, label="'My star', T = 6451 K")
plt.xticks(np.linspace(0,0.0002,5), np.linspace(0,20000,5)) # Label like it's angstroms
plt.xlabel("$\lambda$ ($\AA$)")
plt.ylabel("F$_{\lambda}$ (erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)")
plt.title("The flux (F$_{\lambda}$) per unit wavelength ($\lambda$) of a star \n with a stellar temperature of 6451 K")
plt.legend()
plt.savefig("/home/vboxuser/Documents/Stellar/blackbody.png")
plt.close()

##################
#                #
#   Question 4   #
#                #
##################

# Find index of maximum flux
max_flux_loc = np.where(fluxes == max(fluxes))[0]

# Wavelength at this index
peak_wavelength = wavelengths[max_flux_loc-1].item() * 10**8 # convert to angstrom

print("The peak wavelength of the star's emission is " + str(peak_wavelength) + " \u00C5")

##################
#                #
#   Question 5   #
#                #
##################

pc_fluxes = flux(wavelengths, 3100)

# Find index of maximum flux for PC
pc_max_flux_loc = np.where(pc_fluxes == max(pc_fluxes))[0]

# Wavelength at this index for PC
pc_peak_wavelength = wavelengths[pc_max_flux_loc-1].item() * 10**8 # convert to angstrom
plt.plot(wavelengths, fluxes, label="'My star', T = 6451 K")
plt.plot(wavelengths, pc_fluxes, label="Proxima Centauri, T = 3100 K")
plt.xticks(np.linspace(0,0.0002,5), np.linspace(0,20000,5)) # Label like it's angstroms
plt.xlabel("$\lambda$ ($\AA$)")
plt.ylabel("F$_{\lambda}$ (erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)")
plt.title("The flux (F$_{\lambda}$) per unit wavelength ($\lambda$) of a star \n with a stellar temperature of 6451 K")
plt.legend()


plt.annotate("Peak of my\nstar's spectrum,\n$\lambda$ = " + str(np.round(peak_wavelength)) + " $\AA$", xy=(peak_wavelength*1e-8, max(fluxes)), xytext=(0.00004,0.4e15), arrowprops=dict(arrowstyle="->"))
plt.annotate("Peak of Proxima\nCentauri's spectrum,\n$\lambda$ = " + str(np.round(pc_peak_wavelength)) + " $\AA$", xy=(pc_peak_wavelength*1e-8, max(pc_fluxes)), xytext=(0.0001,0.6e15), arrowprops=dict(arrowstyle="->"))


plt.savefig("/home/vboxuser/Documents/Stellar/blackbody_PC.png")
plt.close()