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

    # First 4 seconds of audio recorded in audio_0_4
    audio_0_4 = r.record(source, duration = 4)

    # Second 4 seconds of audio recorded in audio_4_8
    audio_4_8 = r.record(source, duration = 4)

# Invokes Google Web Speech API & outputs text
print("First 4 seconds of audio file to text:", r.recognize_google(audio_0_4))
print("Second 4 seconds of audio file to text:", r.recognize_google(audio_4_8))

### Implementing offset (start capturing x seconds into the audio file)

# Record Data from File
with harvard as source:
    # Seconds 3-7 of audio recorded in audio_3_7
    audio_3_7 = r.record(source, offset = 3, duration = 4)

# Invokes Google Web Speech API & outputs text
print("Seconds 3-7 of audio file to text (using offset):", r.recognize_google(audio_3_7))


### How transcription could get messed up - start/stop recording mid-word

# Record Data from File
with harvard as source:
    # Seconds 4.7-7.5 of audio recorded in audio_midword
    audio_midword = r.record(source, offset = 4.7, duration = 2.8)

# Invokes Google Web Speech API & outputs text
print("Seconds 4.7-7.5 of audio file to text:", r.recognize_google(audio_midword))


"""
Transcribing speech from an audio file with background noise
"""

jackhammer = sr.AudioFile('jackhammer.wav')

# Record Data from File
with jackhammer as source:
    # Audio w/ background noise recorded in audio_BN
    audio_BN = r.record(source)

# Invokes Google Web Speech API & outputs text
print("Audio file to text (Has Background Noise):", r.recognize_google(audio_BN))

### Adjusting for Background Noise (not perfect)

# Record Data from File
with jackhammer as source:
    # Adjusts for background noise
    r.adjust_for_ambient_noise(source)
    # Adjusted audio w/ background noise recorded in audio_Adjust_BN
    audio_Adjust_BN = r.record(source)
# Invokes Google Web Speech API & outputs text
print("Audio file to text (Adjusted Background Noise):", r.recognize_google(audio_Adjust_BN))


### Adjusting for Background Noise (improved)

# Record Data from File
with jackhammer as source:
    # Adjusts for background noise - only reads first 0.5 seconds to calibrate
    #(won't consume as much audio from the beginning of the file)
    r.adjust_for_ambient_noise(source, duration = 0.5)
    # Adjusted audio w/ background noise recorded in audio_Adjust2_BN
    audio_Adjust2_BN = r.record(source)

# Invokes Google Web Speech API & outputs text - shows all alternative tramscriptions
print("Audio file to text (Adjusted Background Noise - improved):", r.recognize_google(audio_Adjust2_BN, show_all = True))