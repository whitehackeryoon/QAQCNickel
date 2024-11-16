import numpy as np
import matplotlib.pyplot as plt

#construct a time signal

Fs = 8 #sampling freq
tstep = 1 / Fs #sample time interval
f0 = 1 #signal freq

N = int(Fs / f0) #number of samples

t = np.linspace(0, (N-1)*tstep, N) #time steps
fstep = Fs / N #freq interval
f = np.linspace(0, (N-1)*fstep, N) #freq steps

y = 1 * np.sin(2 * np.pi * f0 * t) 

#perform fft
X =  np.fft.fft(y)
X_mag = np.abs(X) / N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot [0] = X_mag_plot[0] / 2 #DC component doesnt need to multiply by 2

#plot
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(f_plot, X_mag_plot, '.-')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude')
ax1.grid()
ax2.grid()
plt.tight_layout()
plt.show()





