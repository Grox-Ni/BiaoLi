from ImgEmo import imgemo
from TextEmo import textemo
import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    BING_KEY = "7c9c086e169449e5bb48e6fb5ecc52b6"
    s_result = r.recognize_bing(audio, key=BING_KEY)

if s_result*i_result>0 :
    print "Same"
else :
    print "Diff"

