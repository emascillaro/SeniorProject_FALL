import speech_recognition as sr

# Checks and prints version of SpeechRecognition currently installed
print(sr.__version__)

# Creates a recognizer instance
r = sr.Recognizer()

"""
Transcribing speech from an audio file
"""

# Record Data from File
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

# Check the type of audio in "audio"
print(type(audio))

# Invokes Google Web Speech API & outputs text
print("audio file to text:", r.recognize_google(audio))

"""
Transcribing speech from an audio file - capturing portions of the file
"""

# Record Data from File
with harvard as source:

    # First 4 seconds of Audio recorded in Audio_0_4
    audio_0_4 = r.record(source, duration = 4)

    # Second 4 seconds of Audio recorded in Audio_4_8
    audio_4_8 = r.record(source, duration = 4)

# Invokes Google Web Speech API & outputs text
print("First 4 seconds of audio file to text:", r.recognize_google(audio_0_4))
print("Second 4 seconds of audio file to text:", r.recognize_google(audio_4_8))

### Implementing offset (start capturing x seconds into the audio file)

# Record Data from File
with harvard as source:
    # Seconds 3-7 of Audio recorded in Audio_3_7
    audio_3_7 = r.record(source, offset = 3, duration = 4)

# Invokes Google Web Speech API & outputs text
print("Seconds 3-7 of audio file to text (using offset):", r.recognize_google(audio_3_7))


### How transcription could get messed up - start/stop recording mid-word

# Record Data from File
with harvard as source:
    # Seconds 4.7-7.5 of Audio recorded in Audio_midword
    audio_midword = r.record(source, offset = 4.7, duration = 2.8)

# Invokes Google Web Speech API & outputs text
print("Seconds 4.7-7.5 of audio file to text:", r.recognize_google(audio_midword))
