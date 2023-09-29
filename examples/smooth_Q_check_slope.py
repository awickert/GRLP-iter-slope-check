# Figure UpliftSubsidence in paper

import numpy as np
from matplotlib import pyplot as plt
#plt.ion()

import grlp

S0 = 0.015
P_xB = 0.2
z1 = 0

Qamp = 0.5
dt = 3.15E7 * 1E2
nt = int(100)
Bmax = 250.

lp = grlp.LongProfile()
self = lp

self.bcr = z1

lp.basic_constants()
lp.bedload_lumped_constants()
lp.set_hydrologic_constants()

nsteps = 3

_x = np.hstack([
        np.linspace(0, 10000, 201),
        np.linspace(10010, 10050, nsteps),
        np.linspace(10100, 20000, 199) ])
_Q = np.hstack([
        50 * np.ones(201),
        np.linspace(50, 100, nsteps),
        100 * np.ones(199) ])

lp.set_x( x_ext = _x )
#lp.set_z(S0=-S0, z1=z1)
lp.set_z(S0=-0.000001, z1=z1)
lp.set_Q( Q_ext = _Q )
lp.set_B(100)
lp.set_niter(3)
lp.set_z_bl(z1)
Qs0 = lp.k_Qs * lp.Q[0] * S0**(7/6.)
lp.set_Qs_input_upstream(Qs0)

# Starting case
U = 0.
lp.set_uplift_rate(U/3.15E7)
lp.evolve_threshold_width_river(100, 1E13)

"""
fig = plt.figure(figsize=(6,3))
ax1 = fig.add_subplot(1,1,1)
plt.xlabel('Downstream distance [km]', fontsize=14, fontweight='bold')
plt.ylabel('Elevation [m]', fontsize=14, fontweight='bold')
plt.tight_layout()
ax1.plot(lp.x/1000., lp.z - lp.z[0] + 500, color='.5', linewidth=3)
plt.show()
"""

S_predicted = S0 * (_Q[0]/_Q[-1])**(6/7.)
S_obs = -(np.diff(lp.z) / np.diff(lp.x))[-1]

print( S_predicted )
print( S_obs )

print( "Obs/Pred:", S_obs/S_predicted )

