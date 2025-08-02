 🖥️ DesktopAssistant\_mini

An AI-powered voice-controlled desktop assistant built using Python. It uses speech recognition, text-to-speech, and integrates with services like Google Gemini, Wikipedia, Weather API, and YouTube. The assistant can open/close apps, answer queries, generate passwords, and more.

 ✨ Features

* 🎤 Voice command recognition (using `speech_recognition`)
* 🗣️ Text-to-speech responses (`pyttsx3`)
* 📚 Wikipedia search
* ☁️ Real-time weather updates (WeatherAPI)
* 💬 AI Chatbot (Google Gemini)
* 📺 YouTube control (`pywhatkit`)
* 🔐 Password generator
* 📷 Screenshot capture
* 💻 Launch and control apps via keyboard automation (`pyautogui`)

 🛠️ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
speechrecognition
pyttsx3
pyautogui
wikipedia
google-generativeai
requests
pywhatkit
```

 🔑 Setup

1. Get your **Google Gemini API key** from [Google AI Studio](https://makersuite.google.com/app).
2. Get a **Weather API key** from [WeatherAPI](https://www.weatherapi.com/).
3. Replace the keys in the script:

```python
genAi.configure(api_key="YOUR_GEMINI_API_KEY")
weather_api_key = "YOUR_WEATHER_API_KEY"
```

 🚀 How to Use

1. Run the script:

```bash
python desktop_assistant.py
```

2. Speak your commands like:

   * "Hello"
   * "Launch calculator"
   * "Search Python programming"
   * "Weather at Delhi"
   * "Play Shape of You on YouTube"
   * "Generate password"
   * "Take screenshot"
   * "Exit"

🧠 Sample Prompts for Chatbot Mode

Say `"Act as chatbot"` and then enter any of the following:

* `"Tell me a joke"`
* `"Summarize the French Revolution"`
* `"Write a Python function for Fibonacci"`

Type `'exit'` to leave chatbot mode.



---
📄 License
This project is open source and free to use under the [MIT License](LICENSE).

---
