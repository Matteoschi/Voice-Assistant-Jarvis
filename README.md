# Jarvis
Voice assistant made with python.Voice assistant uses several libraries including the most important one speech_recognition.
```
from speech_recognition import Microphone, Recognizer
```
To activate voice assistant just say aloud Javrvis 
```
if "jarvis" in testo or "service" in testo or "davis" in testo:
```
in this way various functions will be activated including the possibility of opening a folder or a file , doing elementary calculations, knowing the weather of a city. Assistant also identifies the state of mood through the textblob module.
```
from textblob import TextBlob
```
```
translator=Translator(from_lang='it',to_lang='en')
translation=translator.translate(testo)
blob=TextBlob(translation)
sentiment=blob.sentiment.polarity
```
All requests that are made are written to a text file in which the day and time of the same is written.
```
with open(r"SELECT THE FILE .txt","a") as scrittura_su_file:
  scrittura_su_file.write("\n")
  scrittura_su_file.write(data_cronologia)
  scrittura_su_file.write(" -> ")
  scrittura_su_file.write(testo)
```




It is also possible to use the wikipedia library to do research.
```
import wikipedia
```
We find a translator available in 4 different languages including: French German Spanish and English
```
from translate import Translator
```
In the code there are also some preset answers to answer for example questions like how are you, what's your name.

## Authors

- [@Matteoschi](https://github.com/Matteoschi)
