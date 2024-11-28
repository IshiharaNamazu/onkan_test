import numpy as np
import pyaudio

def sound_sin(A, f, t):
    return A * np.sin(2 * np.pi * f * t)

A = 0.5
f = 440
play_length = 5
fs = 44100

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

samples = np.arange(fs * play_length) / fs
y = sound_sin(A, f, samples)

print(type(y))

stream.write(y.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()
