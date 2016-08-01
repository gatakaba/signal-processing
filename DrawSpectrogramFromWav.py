import wave
import sys
import scipy as sp
import matplotlib.pyplot as plt

if __name__ == "__main__":
    wo = wave.open("out.wav", "rb")
    chunk = 65536
    data = sp.fromstring(wo.readframes(chunk), sp.int16)
    srate = wo.getframerate()
    nFFT = 1024
    window = sp.hamming(nFFT)
    
    Pxx, freq, bins, im = plt.specgram(
            data,
            NFFT=nFFT,
            Fs=srate,
            noverlap=512,
            window=window)

    plt.show()
