# AI Desktop Assistant using Speech Recognition and Text-to-Speech

import speech_recognition as sr
import pyttsx3
import pyautogui
import wikipedia
import google.generativeai as genAi
import requests
import pywhatkit
import random
# Initialize the text-to-speech engine
engine = pyttsx3.init()
import atexit       
atexit.register(engine.stop)
import os



# Set up the Google Generative AI API key
client=genAi.configure(api_key="AIzaSyCv3_Qm9m0pDXMR6aTlkrMsJZ3ZzT68Emk")
model=genAi.GenerativeModel("gemini-1.5-flash")  # Using the Gemini model

urlWeather = "http://api.weatherapi.com/v1/current.json"
# Set up the Weather API key
weather_api_key = "7912f8b08d5d429ebbd113601251507"



def gemini_response(prompt):
    # Use the Google Generative AI API to generate a response
    try:
        response = model.generate_content(prompt)
        print(f"Gemini : {response.text.replace('**','')}") 

    except :
        print("Sorry, I could not generate a response at this time.")
    
def fetch_weather(Location):
    """Function to fetch weather information for a given location."""
    params = {
        "key": weather_api_key,
        "q": Location,
    }
    response=requests.get(urlWeather, params=params)  # Make a GET request to the Weather API
    if response.status_code == 200:
        data=response.json()  # Parse the JSON response
        temperature = data['current']['temp_c']  # Get the current temperature in Celsius
        condition = data['current']['condition']['text']  # Get the current weather condition
        wind= data['current']['wind_kph']  # Get the current wind speed in kph
        humidity = data['current']['humidity']  # Get the current humidity percentage
        return f"Temperature: {temperature} degrees Celsius\nCondition: {condition}\nWind: {wind} kph\nHumidity: {humidity}%"
    else:
        return "Sorry, I could not fetch the weather information at this time."


def search_wikipedia(query):
    """Function to search Wikipedia for a given query."""
    try :
        result = wikipedia.summary(query, sentences=3)  # Get a summary of the query
    except :
        result = "Sorry, I could not find any information on that topic."

    return result
def genPass():
    import string
    lowercase= string.ascii_lowercase
    uppercase= string.ascii_uppercase
    digits= string.digits
    special_characters= "@#$%!*.-"
    all_characters=lowercase+uppercase+digits+special_characters
    password=""
    import random
    pass_len= random.randint(8,12)
    for i in range(pass_len+1):
        password+= random.choice(all_characters)
    print(password)  # Print the generated password
        
    

def on_youtube(title):
    pywhatkit.playonyt(title)  # Play the given title on YouTube

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait() #it blocks while the speech is being spoken

def take_command():
    inp = sr.Recognizer() # initializing the recognizer
    with sr.Microphone() as source: # using microphone as the audio source
        print("Listening...")
        input_aud = inp.listen(source=source) # listening for the input audio
    try:
        print("Recognizing...")
        # using Google Web Speech API to recognize the speech
        user_text= inp.recognize_google(input_aud,language="en-in") # recognizing the speech using Google Web Speech API\
        return user_text # returning the recognized text
    except :
        print("Sorry, I did not understand that.")
        return ""

# user_input = take_command() # taking user input
# speak(user_input) # speaking out the recognized text


while True:
    user_input = take_command() # taking user input

    if "hello" in user_input.lower():
        print("Hello! How can I assist you today?")
        speak("Hello! How can I assist you today?")

    if "launch" in user_input.lower():
        app=user_input.lower().replace("launch", "")
        pyautogui.press('win')  # Press the Windows key to open the Start menu
        pyautogui.sleep(0.3)  # Wait for the Start menu to open
        pyautogui.typewrite(app.strip())  # Type the application name
        pyautogui.press('enter')  # Press Enter to launch the application
        print(f"Launching {app.strip()}...")

    if "close the window" in user_input.lower():
        pyautogui.hotkey('alt', 'f4')  # Close the current window
        speak("Closing the current window.")

    if "change the tab" in user_input.lower():
        pyautogui.hotkey('alt', 'tab')  # Change to the next tab
        speak("Changing to the next tab.")

    if "search" in user_input.lower():
        result=search_wikipedia(user_input.lower().replace("search", "").strip())
        print(result)

    if "act as chatbot" in user_input.lower():
        while True:
            user_prompt = input("Enter your prompt (type 'exit' to stop): ")
            if user_prompt.lower() == "exit":
                break
            gemini_response(user_prompt)
    if "weather at" in user_input.lower():
        location=user_input.lower().replace("weather at", "").replace("current","").strip()
        weather_info = fetch_weather(location)
        print(weather_info)

    if "on youtube" in user_input.lower():
        title=user_input.lower().replace("on youtube", "").replace("play","").strip()
        on_youtube(title)
        print(f"Playing '{title}' on YouTube.")
    
    if "password" in user_input.lower():
        print("Here is your password")
        speak("Here is your password")
        genPass()

    if "increase brightness" in user_input.lower():
        
        os.system(f'WMIC /NAMESPACE:\\\\root\\wmi PATH WmiMonitorBrightnessMethods WHERE "Active=TRUE" CALL WmiSetBrightness Brightness=70 Timeout=0')
        print("brightness increased to 70%")


    if "screenshot" in user_input.lower():
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot{random.randint(1,1000)}.png")  # Save the screenshot as a PNG file
        print("Screenshot taken and saved.")
        speak("Screenshot taken and saved.")



    if "exit" in user_input.lower() :        
        print("Exiting the system.")
        speak("Exiting the system.")
        break

