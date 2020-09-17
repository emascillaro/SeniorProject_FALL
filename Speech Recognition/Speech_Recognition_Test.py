import speech_recognition as sr

# Checks and prints version of SpeechRecognition currently installed
print(sr.__version__)

# Creates a recognizer instance
r = sr.Recognizer

# Record Data from File
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)  # Throwing error that there is a missing positional argument "source"

# Check the type of audio in "audio"
print(type(audio))