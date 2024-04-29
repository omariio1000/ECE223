from scipy import signal
from math import pi
import matplotlib.pyplot as plt
import os


R = 600
L = 400e-3
C = 2.5e-6

nums = [[0, R/C, 0], [1, 0, 0], [0, 0, 1/(L * C)]]
dem = [1, R/L, 1/(L * C)]

for i in range(len(nums)):
    tfun = signal.TransferFunction(nums[i], dem)
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

    file_name = f"{os.path.dirname(__file__)}\\hw3\\hw3_1_{i+1}.png"
    plt.savefig(file_name)
    plt.close()
