import speech_recognition as sr
import os
from shutil import copyfile

in_folder = ""
out_folder = "


for i in os.listdir(in_folder):
    if '.wav' in i:
        print(i)
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(in_folder + i) as source:
            audio = r.record(source)  # read the entire audio file

        try:
            text = r.recognize_google(audio)
            text = text.replace('"', '')
            text = text.replace('.', '')
            text = text.replace('?', '')
            text = text.replace('-', '')
            text = text.replace('!', '')
            copyfile(in_folder + i, out_folder + text + '.wav')

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio for: " + i)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))





