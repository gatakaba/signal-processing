import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def drawSpectrograms(data):
    def drawSpectrogram(data):
        fs = 1000
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
        return Pxx
    data1 = data[:, 0]
    data2 = data[:, 2]
    plt.subplot(121)
    plt.title("MMG")
    sp1 = drawSpectrogram(data1)
    plt.colorbar()
    plt.subplot(122)

    plt.title("EMG")
    sp2 = drawSpectrogram(data2)
    plt.colorbar()
    max = np.max([np.max(sp1), np.max(sp2)])
    min = np.min([np.min(sp1), np.min(sp2)])

    plt.subplot(121)
    plt.xlabel("time[s]")
    plt.ylabel("frequency[Hz]")
    plt.xticks(range(10))
    plt.yticks(np.arange(0, 500, 50))
    plt.clim(np.log10(min) * 10, np.log10(max) * 10)
    plt.subplot(122)
    plt.xlabel("time[s]")
    plt.ylabel("frequency[Hz]")
    plt.xticks(range(10))
    plt.yticks(np.arange(0, 500, 50))
    plt.clim(np.log10(min) * 10, np.log10(max) * 10)
    plt.show()


def draw(data):
    t = np.arange(0, 10 ** -3 * len(data), 10 ** -3)
    rawMMG = data[:, 0]
    IMMG = data[:, 1]
    rawEMG = data[:, 2]
    IEMG = data[:, 3]
    plt.subplot(411)
    plt.ylabel("Voltage[V]")
    plt.title("Raw MMG")
    plt.plot(t, rawMMG)
    plt.subplot(412)
    plt.ylabel("Voltage[V]")
    plt.title("Raw EMG")
    plt.plot(t, rawEMG)
    plt.subplot(413)
    plt.ylabel("Voltage[V]")
    plt.title("IMMG")
    plt.plot(t, IMMG)
    plt.subplot(414)
    plt.ylabel("Voltage[V]")
    plt.title("IEMG")
    plt.plot(t, IEMG)
    plt.xlabel("time[s]")
    plt.show()


def IMMG_and_IEMG(data):
    t = np.arange(0, 10 ** -3 * len(data), 10 ** -3)
    IMMG = data[:, 1]
    IEMG = data[:, 3]
    plt.xlabel("time[s]")
    plt.ylabel("Voltage")
    plt.title("IMMG & IEMG")
    plt.xticks(range(10))
    plt.plot(t, IMMG, linewidth=2, label="IMMG")
    plt.plot(t, IEMG, linewidth=2, label="IEMG")
    plt.legend()
    plt.show()


def MMG_and_EMG(data):
    t = np.linspace(0, 1, 10 ** 3)
    rawMMG = data[000:1000, 0]
    IMMG = data[000:1000, 1]
    rawEMG = data[000:1000, 2]
    IEMG = data[000:1000, 3]
    plt.subplot(211)
    plt.xlabel("time[s]")
    plt.ylabel("Voltage")
    plt.title("MMG & EMG")
    plt.xticks(np.linspace(0, 1, 5))

    plt.plot(t, rawEMG, label="EMG")
    plt.plot(t, rawMMG, label="MMG")
    plt.legend()
    plt.subplot(212)
    plt.xlabel("time[s]")
    plt.ylabel("Voltage")
    plt.title("IMMG & IEMG")
    plt.xticks(np.linspace(0, 1, 5))

    plt.plot(t, IEMG, label="IEMG")
    plt.plot(t, IMMG, label="IMMG")

    plt.legend()
    plt.show()


def drawFirstOneSec(data):
    draw(data[:1000])


def normalize(data):
    plt.suptitle("Normalized")
    return (data - np.mean(data, axis=0)) / np.std(data, axis=0)
if __name__ == "__main__":
    data = np.loadtxt("gupa.CSV", delimiter=",")

    print np.cov(normalize(data[:, 0]), normalize(data[:, 2]))
    # plt.plot(data[:, 0], data[:, 1])
    plt.plot(normalize(data[:, 1]))
    plt.plot(normalize(data[:, 3]))
    plt.show()
    # drawFirstOneSec(data)
    # draw(data)

    IMMG_and_IEMG(data)
    # draw(normalize(data))
    # MMG_and_EMG(normalize(data))
