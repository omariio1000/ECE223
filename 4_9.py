from scipy import signal
from math import pi
import matplotlib.pyplot as plt

#Ex 1
'''
R = 6.28
L = 0.1

num = [R/L]
dem = [1, R/L]
'''

#Ex 2
R = 75
L = 0.01

num = [L, 0]
dem = [L, R]

tfun = signal.TransferFunction(num, dem)
w, mag, phase = signal.bode(tfun)
f = w / (2 * pi)

fig, ax = plt.subplots(nrows=2)
ax[0].semilogx(f, mag)
ax[0].set_ylabel('Magnitude (dB)')
ax[0].set_title('Bode Plot\n')
ax[0].grid()
ax[1].semilogx(f, phase)
ax[1].set_ylabel('Phase (degrees)')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].grid()

plt.show()