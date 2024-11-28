import numpy as np
import keyboard
from time import sleep
import pyaudio
import random

# パラメーター
VOLUME = 0.5 # 音量
SOUND_TIME = 0.5 # sec
SHIFT_MAX_SEMITONE = 0.2
SHIFT_MIN_SEMITONE = 0.5 # 何半音ずらすかの範囲

ENABLE_CHANGE_KEY = True # キー変更
MIN_KEY = -6
MAX_KEY = 6


### func ###
fs = 44100  # サンプリング周波数
def gen_audio(freq, sec):
    t = np.arange(0, sec, 1/fs)
    note = VOLUME * np.sin(freq* t * 2 * np.pi)
    return (note / np.max(np.abs(note)))

def sound(freq_array):
  for freq in freq_array:
    # print('' + str(deg) + ' : ' + str(major_scale[deg-1]) + '[Hz]')
    stream = p.open(format=pyaudio.paFloat32,
                  channels=1,
                  rate=fs,
                  output=True)
    stream.write(gen_audio(freq, SOUND_TIME).astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    
def gen_major_scale(key = 0,deg_shifted = 0, shift_semitone = 0): # 度数，何半音ずらすか
    arry = []
    major_scale_diff_a = [-9,-7,-5,-4,-2,0,2,3] # A4(440Hz)から何半音離れているか
    for i in range(len(major_scale_diff_a)):# C,D,E,F,G,A,B
      if i == deg_shifted-1:
        arry.append(440 * ( 2 ** ( (major_scale_diff_a[i] + shift_semitone + key) /12) )) # 1オクターブ(12半音)で倍になる
      else:
        arry.append(440 * ( 2 ** ( (major_scale_diff_a[i] + key) /12) )) # 1オクターブ(12半音)で倍になる
    return arry
  
def get_key():
  if keyboard.is_pressed('q'):
    return -1
  if keyboard.is_pressed('r'):
    return -2

  if keyboard.is_pressed('1'): 
    return 1
  if keyboard.is_pressed('2'):
    return 2
  if keyboard.is_pressed('3'):
    return 3
  if keyboard.is_pressed('4'):
    return 4
  if keyboard.is_pressed('5'):
    return 5
  if keyboard.is_pressed('6'):
    return 6
  if keyboard.is_pressed('7'):
    return 7
  if keyboard.is_pressed('8'):
    return 8
  return 0



### start ###
p = pyaudio.PyAudio()

while True:

  ans = random.randint(1,8)
  shift_semitone_size = random.uniform(SHIFT_MAX_SEMITONE, SHIFT_MIN_SEMITONE)
  key = 0
  if ENABLE_CHANGE_KEY:
    key = random.randint(MIN_KEY,MAX_KEY)
  shift_sig = random.randint(0,1)

  if shift_sig==0:
    shift_sig = -1

  # print(shift_sig)
  major_scale = gen_major_scale(key = key,deg_shifted = ans,shift_semitone = shift_sig*shift_semitone_size)


  # print(major_scale)
  sound(major_scale)
  print('for exit prees \'q\', for mouitido press \'r\'')
    
  while True:
    key = get_key()
    if key==0:
      sleep(0.05)
      continue
    if key == -2:
      sound(major_scale)
    if key == -1:
      print('ans : ' + str(ans) + ', key : ' + str(key) + ', zure : ' + str(shift_sig*shift_semitone_size))
      p.terminate()
      print('end')
      exit()
    if key > 0:
      if key == ans:
        print('seika-i')
        print('ans : ' + str(ans) + ', key : ' + str(key) + ', zure : ' + str(shift_sig*shift_semitone_size))
        break
      else:
        print('aho')
        while key == get_key():
          sleep(0.05)
