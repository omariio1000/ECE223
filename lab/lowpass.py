from scipy import signal
from math import pi
import matplotlib.pyplot as plt
import os

R = 1e3
C = 318e-9

num = [1]
dem = [R*C, 1]

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

file_name = f'{os.path.dirname(__file__)}\\lowpass.png'
plt.savefig(file_name)
plt.close()