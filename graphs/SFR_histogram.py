import matplotlib.pyplot as plt
import h5py as h5
import numpy as np

t = h5.File('E:\yanjiu\stellarmaps\\vdisp\galaxies_progmaps_hr_tng300_072.hdf5', 'r')
y = t['catsh_SubhaloSFR'][:]
x = t['scalar_star_mass'][:]

index = np.argwhere(x > 10e10)
q = np.array([])
for i in range(len(index)):
    q = np.append(q, y[index[i]])

plt.figure(figsize=(10,20))
plt.hist(q, bins=100, log=True)
plt.xlabel("SFR", fontsize=16)
plt.ylabel("amount", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim(0, 80)
plt.title('histogram of SRF', fontsize=16)
plt.show()
