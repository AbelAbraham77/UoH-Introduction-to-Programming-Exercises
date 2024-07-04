import sys

try:
    import pyttsx3
except ImportError:
    print("The pyttsx3 module needs to be installed to run this program. On Windows, open a Command Prompt and run:")
    print("pip install pyttsx3")
    print("On macOS and Linux, open a Terminal and run:")
    print("pip3 install pyttsx3")
    sys.exit()

tts = pyttsx3.init()

print("Enter the text to speak, or QUIT to quit.")

while True:
    text = input("> ")

    if text.upper() == "QUIT":
        print("Thank you for using Text-to-Speech!")
        sys.exit()

    tts.say(text)
    tts.runAndWait()
