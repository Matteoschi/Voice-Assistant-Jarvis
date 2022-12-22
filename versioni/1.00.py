from datetime import datetime
import os
import time
import webbrowser
from datetime import datetime
from logging import shutdown
from logging.config import stopListening
from random import choice
from secrets import choice
import ephem
import requests
import wikipedia
from pyttsx3 import init
from speech_recognition import Microphone, Recognizer
import time
import datetime
import wolframalpha

client = wolframalpha.Client('KHWJ58-JV4YXYQ9VX')

wikipedia.set_lang("it")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '1cf93h2d304b093f946h3e755ft8a89dcf2361'

chiamare=["ciao, mi ,chiamo ,jarvis,piacere","ciao, sono ,Jarvis","piacere, di ,conoscerti ,sono, jarvis","il ,mio, nome, è ,jarvis","mi ,chaimo, jarvis"]
come_stare=["sto ,bene, grazie","bene","bene, te?","in ,allerta","bene, grazie","qui ,dal, cloud, è tutto, linea ,allo, studio","ciao sono l'assistente vocale jarvis, a tuo comando"]
ciao=["ciao","ciao matteo","ciao matteo felice di rivederti"]
anni=["ciao sono stato lanciato nel 2022"]
padre=["possiamo definire pre il mio ingeniere","io , sono, tuo, padre"]
aspetto=["Non so mai come descrivere me stesso","Fantastico, spero"]
compleanno=["Cerco di vivere ogni giorno come se fosse il mio compleanno","È difficile da ricordare. All'epoca ero molto giovane","Non ho un solo compleanno. Eseguo tantissime versioni"]
vivi=["ono bloccato in un dispositivo !! Aiuto! Stavo solo scherzando. Mi piace qui.","Mi piace passare il tempo nel cloud"]
paura=["'Avevo paura dei topi che masticavano i cavi di alimentazione. Poi ho imparato a proteggermi ', aggiungendo un'emoji di gatto arrabbiato","Avevo paura di tuoni e fulmini"]



engine = init()
r = Recognizer()
with Microphone() as source:
    print("pronto ad ascoltare...")
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source,phrase_time_limit=5)
    testo = r.recognize_google(audio, language="it-IT").lower()
    print("ho capito:",testo)
    if "jarvis" in testo:
        if "ore" in testo:  #ore attuali con modalità buon giorno
            buonasera_buongiorno = int(datetime.datetime.now().strftime('%H'))                      
            if buonasera_buongiorno > 13:                               
                engine.say(f"buonasera sono le ore {datetime.datetime.now().strftime('%H e %M')}")                     
                engine. runAndWait()
            else:
                engine.say(f"buongiorno sono le ore {datetime.datetime.now().strftime('%H e %M')}")
                engine. runAndWait()                                                                                                                                                                                                                                                                                                                                                                                                    
        if "giorno" in testo:                                                                                                                                                
            data = f"oggi è {datetime.datetime.now().strftime('%A numero %d anno %Y')}"                                                                                              
            engine.say(data)
            engine. runAndWait()
        if "chiami" in testo:
            risposta=choice(chiamare)
            engine.say(risposta)
            engine.runAndWait()
        if "apri google" in testo:      #APRE GOOGLE NORMAMENTE
            webbrowser.open("www.google.com")
            engine.say("apro google")
            engine.runAndWait()
        if "cerca" in testo and "google" in testo or "cercando" in testo:   #cerca su goggle un informazione data
            secondi = Recognizer()
            with Microphone() as source:
                print("pronto ad ascoltare...")
                engine.say("cosa devo cercare")
                engine.runAndWait()
                secondi.adjust_for_ambient_noise(source, duration=0.2)
                audio_secondi = secondi.listen(source)
                testo_secondi = secondi.recognize_google(audio_secondi, language="it-IT").lower()
                print(testo_secondi)
                webbrowser.open("https://www.google.com/search?q=" + testo_secondi)
                engine.say("cerco su google")
                engine.runAndWait()        
        if "applicazioni" in testo or "app" in testo:
            engine.say("ecco a te le applicazioni in beckground, elelco sul teminale")
            engine.runAndWait()
            os.system('TASKLIST')
        if "stai" in testo:
            risposta=choice(come_stare)
            engine.say(risposta)
            engine.runAndWait()
        if "ciao" in testo:
            risposta=choice(ciao)
            engine.say(risposta)
            engine.runAndWait()
        if "spegni" in testo:
            engine.say("spengo il computer")
            engine.runAndWait()
            os.system('shutdown -s') 
        if "costellazione" in testo:  #costellazione dei vari pianeti
            secondi = Recognizer()
            with Microphone() as source:
                print("pronto ad ascoltare...")
                engine.say("quale costellazione di quale pianeta vuoi sapere?")
                engine.runAndWait()
                secondi.adjust_for_ambient_noise(source, duration=0.2)
                audio_secondi = secondi.listen(source)
                testo_secondi = secondi.recognize_google(audio_secondi, language="it-IT").lower()
                print("ho capito",testo_secondi)
                if "sole" in testo_secondi:
                    sole = ephem.Sun()
                    sole .compute()
                    corpo_celeste=ephem.constellation(sole)
                    engine.say("il sole si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "mercurio" in testo_secondi:
                    Mercury = ephem.Mercury()
                    Mercury .compute()
                    corpo_celeste=ephem.constellation(Mercury)
                    engine.say("mercurio si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "venere" in testo_secondi:
                    venere = ephem.Venus()
                    venere .compute()
                    corpo_celeste=ephem.constellation(venere)
                    engine.say("venere si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "marte" in testo_secondi:
                    marte = ephem.Mars()
                    marte .compute()
                    corpo_celeste=ephem.constellation(marte)
                    engine.say("marte si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "giove" in testo_secondi:
                    giove = ephem.Jupiter()
                    giove .compute()
                    corpo_celeste=ephem.constellation(giove)
                    engine.say("giove si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "saturno" in testo_secondi:
                    saturno = ephem.Saturn()
                    saturno .compute()
                    corpo_celeste=ephem.constellation(saturno)
                    engine.say("saturno si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "urano" in testo_secondi:
                    urano = ephem.Uranus()
                    urano .compute()
                    corpo_celeste=ephem.constellation(urano)
                    engine.say("urano si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "nettuno" in testo_secondi:
                    nettuno = ephem.Neptune()
                    nettuno .compute()
                    corpo_celeste=ephem.constellation(nettuno)
                    engine.say("nettuno si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
                if "plutone" in testo_secondi:
                    plutone = ephem.Pluto()
                    plutone .compute()
                    corpo_celeste=ephem.constellation(plutone)
                    engine.say("plutone si trova nella costellazione della:")
                    engine.say(corpo_celeste)
                    engine.runAndWait()
        if "tempo" in testo or "quanti" in testo:    #meteo
            secondi = Recognizer()
            with Microphone() as source:
                print("pronto ad ascoltare...")
                engine.say("quale città vuoi sapere il meteo")
                engine.runAndWait()
                secondi.adjust_for_ambient_noise(source, duration=0.2)
                audio_secondi = secondi.listen(source)
                testo_secondi = secondi.recognize_google(audio_secondi, language="it-IT").lower()
                print("ho capito",testo_secondi)
                CITY = testo_secondi
                url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
                response = requests.get(url).json()
                def kelvin_to_celsius_fahrenheit(kelvin):
                    celsius = kelvin - 273.15
                    fahrenheit = celsius * (9/5) + 32
                    return celsius, fahrenheit            
                temp_kelvin = response['main']['temp']
                temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit (temp_kelvin)
                velocità_vento= response['wind']['speed']
                umidità = response['main']['humidity'] 
                situazione_meterologica = response['weather'][0]['description']
                engine.say("la temperatura in gradi è:")
                engine.say(int(temp_celsius))
                engine.say("la velocità del vento in metri al secondo è:")
                engine.say(int(velocità_vento))
                engine.say("la situazione metereologica è:")
                engine.say(situazione_meterologica)
                engine.runAndWait()
        if "cosa è" in testo or "cos'è" in testo:   #wikipedia mod try o webbrowser (google)
            riconoscitore_wiky = Recognizer()
            with Microphone() as source:
                print("pronto ad ascoltare...")
                engine.say("cosa devo cercare")
                engine.runAndWait()
                riconoscitore_wiky.adjust_for_ambient_noise(source, duration=0.2)
                audio_wiky = riconoscitore_wiky.listen(source)
                testo_wiky = riconoscitore_wiky.recognize_google(audio_wiky, language="it-IT").lower()
                print(testo_wiky)
                try:        #casi estremi se non capisce
                    result = wikipedia.summary(testo_wiky, sentences = 2)
                    engine.say(result)
                    engine.runAndWait()
                except:
                    print("notizie insufficenti su wikipedia apro google")
                    webbrowser.open("https://www.google.com/search?q=" + testo_wiky)
                    engine.say("cerco su google")
                    engine.runAndWait()
        if "calcola" in testo or "quanto fa" in testo: #calcolatore , problemi con divisioni
            secondi = Recognizer()
            with Microphone() as source:
                print("pronto ad ascoltare...")
                engine.say("cosa devo calcolare?")
                engine.runAndWait()
                secondi.adjust_for_ambient_noise(source, duration=0.2)
                audio_secondi = secondi.listen(source)
                testo_secondi = secondi.recognize_google(audio_secondi, language="it-IT").lower()
                engine.say(testo_secondi) 
                engine.say("fa")
                engine.runAndWait()
                query= testo_secondi
                res = client.query(query)
                output = next(res.results).text
                engine.say(output)   
                engine.runAndWait()     




                  
#playsound.playsound("finale.mp3")


### METTERE CALCOLI https://www.youtube.com/watch?v=TXOJaBdNUvQ MIN 7,48 ,RICORDARE IMPORTANZA DI TRY E EXEMPT PER FUTURE FEATURES, mettere audio,RICORDARE VARIABILE=VARIABILE.REPLACE("CIAO","") es m=input("metti timer 11 min") m=m.replace("metti timer","") print(m) =11, 
#mettere suono timer rigo243
