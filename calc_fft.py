# coding:utf-8
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

from scipy.signal import hamming

sampling_rate = 100  # [Hz]
sampling_time = sampling_rate ** -1  # [s]

t = np.linspace(0, 10, 10 * sampling_rate)
f = 10
x = np.sin(2 * np.pi * t ** 2 / 2)
i = 0

frequency_list = []
while True:
    n = 512  # データ数
    y = x[i:n + i]
    y = y * hamming(n)
    # FFT 処理と周波数スケールの作成
    yf = fftpack.fft(y)

    frequency_list.append(np.abs(yf[1:n / 2]))
    i += 1
    if n + i == len(x):
        break

frequency_list = np.array(frequency_list)
print(frequency_list.shape)
plt.plot(t, x)
plt.show()

# plt.pcolormesh(t,f,frequency_list,vmax=1e-6)
plt.pcolor(frequency_list.T)
plt.show()
"""
freq = fftpack.fftfreq(n, sampling_time)

plt.plot(freq[1:n / 2], np.abs(yf[1:n / 2]))

plt.ylabel("Amplitude")
plt.axis("tight")
plt.show()
"""
