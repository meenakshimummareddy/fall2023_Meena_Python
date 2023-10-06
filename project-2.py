import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error with the Google API: {0}".format(e))
        return ""


# Main program loop
while True:
    command = listen().lower()

    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is your name" in command:
        speak("I am your personal assistant.")
    elif "exit" in command:
        speak("Goodbye!")
        break
    else:
        speak("I'm sorry, I don't understand that command.")
