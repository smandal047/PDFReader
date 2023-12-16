from tts import speak
from pdfReader import read_pdf

for i in read_pdf('FI/Background and Orientation – Varsity by Zerodha.pdf'):
    text = i.replace('\n', ' ')
    print(text)
    speak(text)


# create a django site
# the site should be able to alter the speed of speech on fly
# show the highlighted text -> -> https://stackoverflow.com/questions/71989908/how-to-highlight-text-as-per-audio-on-a-website-in-realtime-as-the-audio-narrate
# user able to upload the pdf and convert it speech
#