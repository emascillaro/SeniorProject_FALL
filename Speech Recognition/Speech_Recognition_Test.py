import speech_recognition as sr

# Checks and prints version of SpeechRecognition currently installed
print(sr.__version__)

# Creates a recognizer instance
r = sr.Recognizer