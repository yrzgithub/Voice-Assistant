from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from pywhatkit import playonyt, search
from pyjokes import get_joke
from keyboard import wait

recog = Recognizer()
convertor = init()
voices = convertor.getProperty("voices")
convertor.setProperty("voice", voices[1].id)  # female voice


def SayAndPrint(text):
    print(text)
    convertor.say(text)
    convertor.runAndWait()


def action(command):
    print(command)
    if "play" in command:
        command = command.replace("play ", "")
        print(command)
        SayAndPrint("Playing...")
        playonyt(command)

    elif "are you single" in command:
        SayAndPrint("Sorry dear,I already have a boyfriend...It's you..")

    elif "search" in command:
        SayAndPrint("Searching...")
        command = command.replace("search ", "")
        print(command)
        search(command)

    elif "joke" in command:
        SayAndPrint("ok..")
        SayAndPrint(get_joke())

    else:
        SayAndPrint("Sorry! Come again...")


def assistant():
    with Microphone() as s:
        try:
            recog.adjust_for_ambient_noise(source=s, duration=3)
            SayAndPrint("Listening...")
            voice = recog.listen(s, timeout=5)
            command = recog.recognize_google(voice)
            command = command.lower()
            print(command)
            if "ok dear" in command:
                command = command.replace("ok dear ", "")
                action(command)

        except:
            SayAndPrint("Sorry dear, Couldn't catch you at the moment...")


while True:
    assistant()
    SayAndPrint("press ctrl+a to listen again...")
    wait("ctrl+a")

# optimized

from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from pywhatkit import playonyt, search
from pyjokes import get_joke
from keyboard import wait

speech_recognizer = Recognizer()
convertor = init()
voices = convertor.getProperty("voices")
convertor.setProperty("voice", voices[1].id)  # female voice


def SayAndPrint(text):
    print(text)
    convertor.say(text)
    convertor.runAndWait()


def action(command):
    print(command)
    if "play" in command:
        command = command.replace("play ", "")
        print(command)
        SayAndPrint("Playing...")
        playonyt(command)

    elif "are you single" in command:
        SayAndPrint("Sorry dear,I already have a boyfriend...It's you..")

    elif "search" in command:
        SayAndPrint("Searching...")
        command = command.replace("search ", "")
        print(command)
        search(command)

    elif "joke" in command:
        SayAndPrint("ok..")
        SayAndPrint(get_joke())

    else:
        SayAndPrint("Sorry! Come again...")


def assistant():
    with Microphone() as s:
        try:
            recog.adjust_for_ambient_noise(source=s, duration=3)
            SayAndPrint("Listening...")
            voice = recog.listen(s, timeout=5)
            command = recog.recognize_google(voice)
            command = command.lower()
            print(command)
            if "boss" in command:
                command = command.replace("ok dear ", "")
                action(command)

        except:
            SayAndPrint("Sorry dear, Couldn't catch you at the moment...")


while True:
    assistant()
    SayAndPrint("press ctrl+a to listen again...")
    wait("ctrl+a")


