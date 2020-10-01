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
#print("DEFAULT MIC INFO")
#pa = pyaudio.PyAudio()
#pa.get_default_input_device_info()

# Use default system microphone as source,
print("use default microphone as source:")
mic = sr.Microphone()

# Use specified microphone as source
#mic = sr.Microphone(device_index = 2)

try:
    # Record Data from Microphone input
    print("record data from microphone input:")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Invokes Google Web Speech API & outputs text
    print("Invoke Google Web Speech API:")
    print(r.recognize_google(audio))

except:
    print("Could not Recognize speech")