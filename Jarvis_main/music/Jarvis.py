import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')


# there is two voices in my system 1 for Zira , 0 for David in both
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Very Good Morning  Sir!!")

    elif hour>=12 and hour<18:
        speak("Good After Noon Sir")
    else:
        speak("Good Evening!!")

    speak("I am Jarvis 0.1 , How may i assist you")
  
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query       



if __name__=="__main__":
    wishMe()
    while True:
      query = takeCommand().lower()

      #logic for executing tasks based on query
      if 'wikipedia' in query:
        speak('Searching request..........')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("Sir!! According to search Results")
        print(results)
        speak(results)

         #plants according to Wikipedia
         #taj mahal as wikipedia
         #India as wikipedia
      elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")

      
      elif 'google' in query:
        webbrowser.open("https://www.google.com")

      elif 'open Hacktoberfest' in query:
        webbrowser.open("https://hacktoberfest.com/participation/")

      elif 'open linkedin' in query:
        webbrowser.open("https://www.linkedin.com/feed/")
    

      elif 'Introduce yourself' in query:
        speak('Hello!!! Everyone I will be your ,assistant able to perform  minor tasks on your voice command!!, I am designed on Python!! , I will be happy to assist you.')
        
      


      elif 'joke' in query:
        speak('Why are math books so darn depressing?')
      elif 'why' in query:
        speak(' because They’re literally filled with problems.')

      elif 'time'in query:
       strtime= datetime.datetime.now().strftime("%H:%M")
       speak(f"sir!! the time is {strtime}")

      # ADD CODE FOR MUSIC ### Issue No. 1 
  elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "D:\\LatestSong"
            music_dir = "C:\\Users\\Abhishek\\LatestSong"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
      # ADD CODE TO FIND OUT CPU CONFIGURATION ON VOICE COMMAND ### Issue No.2

      # ADD CODE TO FIND OUT CURRRENT DAY  ### Issue No.3

      # ADD CODE TO GIVE INFORMATION ABOUT HACKTOBERFEST 2022  ### Issue No.4

      # ADD CODE TO OPEN CAMERA ON VOICE COMMAND   #### Issue No.5

      # ADD CODE TO PERFORM ADDITION, SUBSTRACTION , MULTIPLICATION , DIVISION , SQUARE ROOT ON VOICE COMMAND   ISSUE NO.6

      # ADD CODE TO GET IMAGES ON GOOGLE   ### ISSUE NO.7
           ### For Example Google search for tree should open images of trees on google

      



