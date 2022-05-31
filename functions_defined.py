import speech_recognition as sr
import pyttsx3

# intialising speech recgonition,pyttsx3 and defining fucntion
listener = sr.Recognizer()


# Here the default  microphone is the device's microphone
# to change this uncomment the device index line and put your microphone index and comment the next line
# which is setting your device's microphone as default

# to find the your device index run code in a seprate python file
if __name__ == '__main__':
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


def take_command():
    mic = sr.Microphone(device_index=2)
    # mic = sr.Microphone()
    query = ""
    r = sr.Recognizer()
    with mic as source:
        print("listening..")
        speak('listening')
        audio = r.listen(source)
        try:
            print("recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said : {query}\n")

        except sr.UnknownValueError:
            sigt = "Sorry,I didn't get that"
            print(sigt)
            speak(sigt)

        except Exception as e:
            print(e)
            stg = "say that again please"
            print(stg)
            speak(stg)

    return query.lower()


engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def speak(audio, rate=150):
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()

