import numpy as np
import matplotlib.pyplot as plotter
 
samplingFrequency   = 100;  # How many time points are needed i,e., Sampling Frequency
samplingInterval    = 1/samplingFrequency;   # At what intervals time points are sampled (sampling period)
beginTime           = 0;    # Begin time period of the signals (second)
endTime             = 10;    # End time period of the signals (second)
signalFrequency     = 1;    # Frequency of the signals

# Time points
time        = np.arange(beginTime, endTime, samplingInterval);

# Create  sine waves
amplitude = np.sin(2*np.pi*signalFrequency*time)

# Create subplot
figure, axis = plotter.subplots(2, 1)
plotter.subplots_adjust(hspace=2)
# Time domain representation for sine wave 1
axis[0].set_title('Sine wave in time domain')
axis[0].plot(time, amplitude)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

# Add the sine waves
amplitude = amplitude

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')

plotter.show()