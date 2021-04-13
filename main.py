import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri','')
                print(command)
    except:
        print('No working!')
    return command

def run_siri():
    ok=1
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('how is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'are you ok' in command:
        talk('sorry, I have a headache')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'send' in command:
        #pywhatkit.sendwhatmsg('+40758670653','Buna gorge!',21,56)
        pywhatkit.sendwhatmsg('+40733571633','Buna cyuc! trimit asta cu siri facuta de mine in python',22,10)
        #pywhatkit.sendwhatmsg('+40748050600','Buna iubire', 22, 0o6)
    elif 'bye' in command:
        talk('Bye Alexandra!See you soon..')
        ok=0
    else:
        talk('PLease say the command again.')
    return ok

while True:
    ok = run_siri()
    if ok==0:
        break