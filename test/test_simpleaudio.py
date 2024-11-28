import numpy as np
import simpleaudio as sa


fs = 44100  # サンプリング周波数
def gen_audio(freq, sec):
    t = np.linspace(0, sec, sec* fs, False)
    note = np.sin(freq* t * 2 * np.pi)
    return (note * (2**15 - 1) / np.max(np.abs(note))).astype(np.int16)  # 16ビットオーディオに変換

play_obj = sa.play_buffer(gen_audio(440, 1), 1, 2, fs)
play_obj.wait_done()