import pyaudio
import wave
from pynput import keyboard
import time

end_recording = False

def keypress(key):
    global end_recording
    if key != None:
        end_recording = True
        return False
sound = pyaudio.PyAudio()

stream = sound.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,   frames_per_buffer=1024)
frames=[]
print("Recording...")
print("Press any key to stop recording...")

with keyboard.Listener(on_press=keypress) as listener:
    while end_recording == False:
        micinput = stream.read(1024)
        frames.append(micinput)

print("Stopped recording!")
stream.stop_stream()
stream.close()
sound.terminate()

audio_file = wave.open("YourRecording.wav","wb")
audio_file.setnchannels(1)
audio_file.setsampwidth(sound.get_sample_size(pyaudio.paInt16))
audio_file.setframerate(44100)
audio_file.writeframes(b''.join(frames))
audio_file.close()