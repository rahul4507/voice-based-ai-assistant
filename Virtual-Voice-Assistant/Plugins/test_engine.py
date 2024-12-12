import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}")

engine.setProperty('voice', voices[0].id)  # Set to the first voice in the list
engine.setProperty('rate', 185)  # Adjust the speaking rate

# Test speech output
engine.say("This is a test of the text-to-speech engine.")
engine.runAndWait()
