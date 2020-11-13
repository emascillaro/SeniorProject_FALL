import speech_recognition as sr
import pyaudio
import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Creates a recognizer instance
r = sr.Recognizer()

"""
Transcribing speech from microphone input
"""

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
    print("Entire Phrase: ")
    text_output = r.recognize_google(audio)
    print(text_output)

    #Part of Speech Stuff
    sentences = nltk.sent_tokenize(text_output)

    data = []
    noun_list = []
    for sent in sentences:
        data = data + nltk.pos_tag(nltk.word_tokenize(sent))

    for word in data:
        if 'NN' in word[1]:
            #print(word)
            noun_list.append(word[0])

    print("nouns:", noun_list)
    understood_speech = 1

except:
    print("Could not Recognize speech")
    understood_speech = 0