import streamlit as st
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish user
def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    assname = "Jarvis 1 point 0"
    speak("I am your Assistant")
    speak(assname)

# Function to take command
def take_command():
    command = st.text_input("You: ")
    return command

# Streamlit app
def main():
    st.title("Jarvis Voice Assistant")
    st.write("Welcome to Jarvis Voice Assistant!")
    wish_me()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            st.write(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Here you go to Google")
            webbrowser.open("https://www.google.com")
        elif 'play music' in query or "play song" in query:
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("I am not able to send this email")

# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == "__main__":
    main()
