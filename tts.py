import pyttsx3


def speak(text):
    # Initialize the library
    engine = pyttsx3.init()
    # specify the text you want to listen
    engine.say(text)
    # Flush the say() queue to play the audio
    engine.runAndWait()


if __name__ == '__main__':

    from pdfReader import read_pdf

    for i in read_pdf('FI/Background and Orientation – Varsity by Zerodha.pdf'):
        text = i.replace('\n', ' ')
        print(text)
        speak(text)
