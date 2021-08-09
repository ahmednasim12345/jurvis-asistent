import pyttsx3 
import speech_recognition as sr
import datetime
import audioop
import wikipedia
import googlesearch
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
#engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good evening")
    else:speak("Good night")    
            
    

    speak(" WELCOME NASIM ! I AM YOUR ASSISTANT ! HOW CAN I HELP YOU SIR?")


def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)  
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None" 
    return query           

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

    
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open stackoverloading' in query:
            webbrowser.open("stackoverloading.com")  
                
                           


    

    



