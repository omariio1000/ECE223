import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

# Function to create Bode plots for a given transfer function
def create_bode_plot(poles, title):
    # Create a Transfer Function (TF) model.
    tf = signal.TransferFunction([1], np.poly(poles))
    
    # Calculate bode magnitudes and phases
    frequencies, magnitudes, phases = signal.bode(tf)

    # Create magnitude plot
    plt.figure(figsize=(14, 6))
    plt.subplot(2, 1, 1)
    plt.semilogx(frequencies, magnitudes)  # Bode magnitude plot
    plt.title('Bode Magnitude Plot of ' + title)
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()

    # Create phase plot
    plt.subplot(2, 1, 2)
    plt.semilogx(frequencies, phases)  # Bode phase plot
    plt.title('Bode Phase Plot of ' + title)
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Phase [degrees]')
    plt.grid()
    plt.tight_layout()
    file_name = f'{os.path.dirname(__file__)}\\hw2\\bode_{title}.png'
    plt.savefig(file_name)
    plt.close()
    
# Poles for second-order Butterworth polynomial
poles_2nd_order = [-1/2 + 1j * np.sqrt(2)/2, -1/2 - 1j * np.sqrt(2)/2]

# Poles for third-order Butterworth polynomial
# Calculated using the angle 60 degrees which is pi/3 radians for Butterworth filter
angle = np.pi/3
poles_3rd_order = [-1, -np.cos(angle) + 1j * np.sin(angle), -np.cos(angle) - 1j * np.sin(angle)]

# Create Bode plots for each filter
create_bode_plot(poles_2nd_order, 'Second-Order Butterworth Filter')
create_bode_plot(poles_3rd_order, 'Third-Order Butterworth Filter')