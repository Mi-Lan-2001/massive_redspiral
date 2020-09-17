import matplotlib.pyplot as plt
import h5py as h5
import numpy as np
import seaborn as sns

t = h5.File('E:\yanjiu\stellarmaps\\vdisp\galaxies_progmaps_hr_tng300_072.hdf5', 'r')
y = t['catsh_SubhaloSFR'][:]/t['scalar_star_mass'][:]
y[y < 1e-13] = 1e-13
x = t['scalar_star_mass'][:]
color = t['scalar_star_v_sigma'][:]

index = np.argwhere(x > 10e10)
q = np.array([])
w = np.array([])
for i in range(len(index)):
    q = np.append(q, x[index[i]])
    w = np.append(w, y[index[i]])

plt.figure(figsize=(10,10))
plt.hexbin(q, w, C=color, xscale='log', yscale='log', gridsize=50, cmap='rainbow')
sns.kdeplot(q, w, color='black', n_levels=5)

plt.axis([10e10, 10e12, 1e-13, 6e-10])
plt.colorbar()
plt.xlabel("log M★[M☉]", fontsize=16)
plt.ylabel("log SFR[M☉ yr-1]", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title('Specific star formation rate versus M* color coded by v/sigma', fontsize=16)
plt.show()