import matplotlib.pyplot as plt
import numpy as np
import os

# Correcting the calculation for poles visualization
# Poles for second-order Butterworth polynomial
poles_2nd_order = [-1/2 + 1j * np.sqrt(2)/2, -1/2 - 1j * np.sqrt(2)/2]

# Poles for third-order Butterworth polynomial
# For the third order, the real pole is at -1, and the complex ones need to be recalculated
# using the angle 60 degrees which is pi/3 radians for Butterworth filter
angle = np.pi/3
poles_3rd_order = [-1, -np.cos(angle) + 1j * np.sin(angle), -np.cos(angle) - 1j * np.sin(angle)]

# Plot the poles on the complex plane
plt.figure()
plt.plot(np.real(poles_2nd_order), np.imag(poles_2nd_order), 'ro', label='2nd-order poles')
plt.plot(np.real(poles_3rd_order), np.imag(poles_3rd_order), 'bo', label='3rd-order poles')
plt.title('Poles of 2nd and 3rd Order Butterworth Filters on the Complex Plane')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.xlim([-1, 1])
plt.ylim([-1, 1])
file_name = f'{os.path.dirname(__file__)}\\hw2\\complex.png'
plt.savefig(file_name)
plt.close()
