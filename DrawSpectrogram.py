# coding:utf-8
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd


def drawSpectrogram(data):
    fs = 10000
    nFFT = 1024
    window = sp.hamming(nFFT)
    # NFFT:Number of data points used in each block for the FFT
    # Fs:Sampling frequency
    Pxx, freq, bins, im = plt.specgram(
        data,
        NFFT=nFFT,
        Fs=fs,
        noverlap=512,
        window=window)
    plt.show()


if __name__ == "__main__":
    dt = pd.read_csv("vibrate2_10000Hz.CSV")
    # data = dt["CH01"]
    drawSpectrogram(np.sin(np.linspace(0, 10, 1000)))
