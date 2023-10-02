# -*- coding: utf-8 -*-
import pyne2001 as ne
import numpy as np
import matplotlib.pyplot as plt

##################
#                #
#   Question 3   #
#                #
##################

# DM at the angles and up to 33 kpc away
max_dm1 = ne.get_dm(45.1, 15, 33)
max_dm2 = ne.get_dm(45.1, 25, 33)

print("The max DM due to the Galaxy along the line (45.1\u00b0, 15\u00b0) is " + str(max_dm1) + " pc cm\u207b\u00b3")
print("The max DM due to the Galaxy along the line (45.1\u00b0, 25\u00b0) is " + str(max_dm2) + " pc cm\u207b\u00b3")

##################
#                #
#   Question 4   #
#                #
##################

# Distance array - up to 50 kpc away
dist = np.arange(0.1, 50.01, 0.01)

# Arrays for results
dm1 = np.array([])
dm2 = np.array([])

for i in dist:
    dm1 = np.append(dm1, ne.get_dm(45.1, 15, i))
    dm2 = np.append(dm2, ne.get_dm(45.1, 25, i))

plt.plot(dist, dm1, label="(45.1$^{\circ}$, 15$^{\circ}$)")
plt.plot(dist, dm2, label="(45.1$^{\circ}$, 25$^{\circ}$)")

plt.legend()
plt.xlabel("Distance (kpc)")
plt.ylabel("DM (pc cm$^{-3}$)")
plt.title("Graph of the Dispersion Measure (DM) against distance from Earth")
plt.annotate('(A)', xy=(11,113.0185), xytext=(11,80), arrowprops=dict(arrowstyle="->"))
plt.annotate('(B)', xy=(7,63.6131), xytext=(7,40), arrowprops=dict(arrowstyle="->"))
plt.annotate('(C)', xy=(20.95,113.7071), xytext=(21,80), arrowprops=dict(arrowstyle="->"))
plt.annotate('(D)', xy=(14.56,64.0221), xytext=(14.5,40), arrowprops=dict(arrowstyle="->"))

# Save linear scaled graph
plt.savefig("dispersion_graphs.png")

# Make a log graph also
plt.xscale('log')
plt.savefig("dispersion_graphs_log.png")

# Close figures
plt.close()

# Output a CSV of the DMs and distances
output_Q4 = np.array([dist, dm1, dm2])
output_Q4 = np.transpose(output_Q4)
np.savetxt("output_Q4.csv", output_Q4, delimiter=",")

##################
#                #
#   Question 5   #
#                #
##################

# Convert from pc cm^-3 to cm^-2

max_density_H_1 = max_dm1 * 3.086 * 10**20
max_density_H_2 = max_dm2 * 3.086 * 10**20

# Also limit to approx 30 kpc
density_H_1 = dm1[0:int(np.floor(len(dm1)*3/5))] * 3.086 * 10**20
density_H_2 = dm2[0:int(np.floor(len(dm2)*3/5))] * 3.086 * 10**20

print("The H I density to the edge of the galaxy along the line (45.1\u00b0, 15\u00b0) is " + str(max_density_H_1) + " cm\u207b\u00b2")
print("The H I density to the edge of the galaxy along the line (45.1\u00b0, 25\u00b0) is " + str(max_density_H_2) + " cm\u207b\u00b2")

plt.plot(dist[0:len(density_H_1)], density_H_1, label="(45.1$^{\circ}$, 15$^{\circ}$)")
plt.plot(dist[0:len(density_H_2)], density_H_2, label="(45.1$^{\circ}$, 25$^{\circ}$)")

plt.legend()
plt.xlabel("Distance (kpc)")
plt.ylabel("N$_H$ (cm$^{-2}$)")
plt.title("Graph of the neutral hydrogen column density ($N_H$) \n against distance from Earth")

# Save linear scaled graph
plt.savefig("density_graphs.png")

# Make a log graph also
plt.xscale('log')
plt.savefig("density_graphs_log.png")

# Close figures
plt.close()

##################
#                #
#   Question 6   #
#                #
##################

# Distance array - 0.9 to 1.1 kpc away
dist_derivative = np.arange(0.9, 1.1, 0.001)

# Arrays for DMs
dm1 = np.array([])
dm2 = np.array([])

for i in dist_derivative:
    dm1 = np.append(dm1, ne.get_dm(45.1, 15, i))
    dm2 = np.append(dm2, ne.get_dm(45.1, 25, i))

plt.plot(dist_derivative, dm1, label="(45.1$^{\circ}$, 15$^{\circ}$)")
plt.plot(dist_derivative, dm2, label="(45.1$^{\circ}$, 25$^{\circ}$)")

# Arrays for derivatives
ddm1 = np.array([])
ddm2 = np.array([])

i = 0
while i < len(dist_derivative) - 1:
    ddm1 = np.append(ddm1, (dm1[i+1] - dm1[i])/(0.001))
    ddm2 = np.append(ddm2, (dm2[i+1] - dm2[i])/(0.001))
    i += 1

plt.plot(dist_derivative[:-1], ddm1, label="d/dx (45.1$^{\circ}$, 15$^{\circ}$)")
plt.plot(dist_derivative[:-1], ddm2, label="d/dx (45.1$^{\circ}$, 25$^{\circ}$)")

plt.legend()
plt.xlabel("Distance (kpc)")
plt.ylabel("DM (pc cm$^{-3}$)")
plt.title("Graph of the Dispersion Measure (DM) against distance from Earth")

# Save graph
plt.savefig("derivative_graphs.png")
plt.close()

# Output a CSV of the derivatives and distances
# Append a 0 to give it the same size as dist
ddm1 = np.append(ddm1, 0)
ddm2 = np.append(ddm2, 0)

output_Q6 = np.array([dist_derivative, ddm1, ddm2])
output_Q6 = np.transpose(output_Q6)
np.savetxt("output_Q6.csv", output_Q6, delimiter=",")

##################
#                #
#   Question 7   #
#                #
##################

# Convert from pc cm^-3 to cm^-2

max_extinction_1 = max_density_H_1 / (2.21 * 10**21)
max_extinction_2 = max_density_H_2 / (2.21 * 10**21)

# Also limit to approx 30 kpc
extinction_1 = density_H_1 / (2.21 * 10**21)
extinction_2 = density_H_2 / (2.21 * 10**21)

print("The optical extinction to the edge of the galaxy along the line (45.1\u00b0, 15\u00b0) is " + str(max_extinction_1) + " magnitudes")
print("The optical extinction to the edge of the galaxy along the line (45.1\u00b0, 25\u00b0) is " + str(max_extinction_2) + " magnitudes")

plt.plot(dist[0:len(extinction_1)], extinction_1, label="(45.1$^{\circ}$, 15$^{\circ}$)")
plt.plot(dist[0:len(extinction_2)], extinction_2, label="(45.1$^{\circ}$, 25$^{\circ}$)")

plt.legend()
plt.xlabel("Distance (kpc)")
plt.ylabel("$A_V$ (mag)")
plt.title("Graph of the optical extinction ($A_V$) \n against distance from Earth")

# Save linear scaled graph
plt.savefig("extinction_graphs.png")

# Make a log graph also
plt.xscale('log')
plt.savefig("extinction_graphs_log.png")

# Close figures
plt.close()
