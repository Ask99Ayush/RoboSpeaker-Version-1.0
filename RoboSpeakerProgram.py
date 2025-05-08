import pyttsx3

# Welcome Message
print("Welcome To RoboSpeaker Version 1.0")

# Initialize text-to-speech engine
engine = pyttsx3.init()

while True:
    # Take user input
    x = input("Enter what you want me to pronounce or (Enter quit to exit): ")
    
    if x.lower() == "quit":
        print("Exiting RoboSpeaker... Goodbye!")
        break
    
    
    # Speak the text
    engine.say(x)
    engine.runAndWait()
