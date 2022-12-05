#import the google text to speech convertor pip 
from gtts import gTTS
# importing this to play the audio 
import os
# text to be converted
speech = "Hi Harsha, I think this is your first time to use pip and modules in python, I wonder how you fucking feel about it?"
# selecting english language
language = 'en'
# setting text, language and voice speed 
obj = gTTS(text=speech, lang=language, slow=True)
# saving the converted audio as beginning.mp3
obj.save('beginning.mp3')
# playing the fucking audio!!!
os.system('start beginning.mp3')