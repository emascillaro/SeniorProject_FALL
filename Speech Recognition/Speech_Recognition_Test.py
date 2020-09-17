import speech_recognition as sr

# Checks and prints version of SpeechRecognition currently installed
print(sr.__version__)

# Creates a recognizer instance
r = sr.Recognizer()

# Record Data from File
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

# Check the type of audio in "audio"
print(type(audio))

# Invokes Google Web Speech API 
print(r.recognize_google(audio))