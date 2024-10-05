import google.generativeai as genai
import speech_recognition as sr
import win32com.client
import os
import webbrowser
import datetime

os.environ["GEMINI_API_KEY"] = ""
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def ai(prompt):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Hello",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Hello! It's nice to hear from you. What can I do for you today? \n",
                ],
            },
        ]
    )

    response = chat_session.send_message(prompt)

    r=response.text
    return r


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognising !")
        audio=r.listen(source)
        said=""

        try:
            print("Recognising...")
            said = r.recognize_google(audio, language="en-in")
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said


if __name__ == '__main__' :
    say("Hello I am Growler,your virtual assistant")
    while True:
        print("Listening ...")
        query = takeCommand()
        sites=[["youtube", "https://www.youtube.com/"], ["google", "https://www.google.com/"],["Shaurya's website", "https://shaurya-thareja.vercel.app/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} Sir...")

        if "Play Spotify".lower() in query.lower():
            webbrowser.open("https://open.spotify.com/playlist/6Rku2rOImlR4evxbM829VN")
            say("Playing Playlist 1 from spotify")

        elif "What is the time".lower() in query.lower():
            strfTime=datetime.datetime.now().strftime("%H:%M")
            say(f"Time is {strfTime}")

        elif "Open Chrome".lower() in query.lower():
            os.system('start C:/Users/Shaur/Desktop/"Shaurya - Chrome."lnk')

        elif "Wake Up growler Daddy back".lower() in query.lower():
            say("Welcome Back Sir, it's been a while.")

        else:
            response=ai(query.lower())
            print(response)
            #say(response)