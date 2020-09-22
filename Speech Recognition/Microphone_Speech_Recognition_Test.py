import speech_recognition as sr
import pyaudio

# Creates a recognizer instance
r = sr.Recognizer()

"""
Transcribing speech from microphone input
"""

# Lists all the available microphones
print("Available Microphones:", sr.Microphone.list_microphone_names())

# Gives default Microphone information
print("DEFAULT MIC INFO")
pa = pyaudio.PyAudio()
pa.get_default_input_device_info()

# Use default system microphone as source,
mic = sr.Microphone()

# Use specified microphone as source
#mic = sr.Microphone(device_index = 2)

# Record Data from Microphone input
with mic as source:
    audio = r.listen(source)

# Invokes Google Web Speech API & outputs text
r.recognize_google(audio)