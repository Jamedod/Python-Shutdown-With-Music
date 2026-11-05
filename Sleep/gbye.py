import os
from playsound import playsound

script_folder = os.path.dirname(os.path.abspath(__file__))
mp3_path = os.path.join(script_folder, "ppp.mp3")
playsound(mp3_path)
