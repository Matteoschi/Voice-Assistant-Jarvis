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
from playsound import playsound
######################-ID FEATURE OPERAZIONI-###########
client = wolframalpha.Client('KHWJ56-JV5YXYQ4VX')
##############-WIKIPEDIA-#######################
wikipedia.set_lang("it")
######################-ID METEO-####################################
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '1cf92d304b093f943e7558a89dcf2361'
######################-variabili ambiente-##########################
data = f"oggi è {datetime.datetime.now().strftime('%A numero %d anno %Y')}"
data_cronologia = f"{datetime.datetime.now().strftime('%d-%H-%M-%S')}"
######################-RISPOSTE PREIMPOSTATE-##########################
chiamare=["ciao, mi ,chiamo ,jarvis,piacere","ciao, sono ,Jarvis","piacere, di ,conoscerti ,sono, jarvis","il ,mio, nome, è ,jarvis","mi ,chaimo, jarvis"]
come_stare=["sto ,bene, grazie","bene","bene, te?","in ,allerta","bene, grazie","qui ,dal, cloud, è tutto, linea ,allo, studio","ciao sono l'assistente vocale jarvis, a tuo comando"]
ciao=["ciao","ciao matteo","ciao matteo felice di rivederti"]
anni=["ciao sono stato lanciato nel 2022","essendo stato lanciato questo anno con la prima versione beta ho attualmeto 0 anni"]
padre=["possiamo definire pre il mio ingeniere","io , sono, tuo, padre"]
aspetto=["Non so mai come descrivere me stesso","Fantastico, spero"]
compleanno=["Cerco di vivere ogni giorno come se fosse il mio compleanno","È difficile da ricordare. All'epoca ero molto giovane","Non ho un solo compleanno. Eseguo tantissime versioni"]
vivi=["ono bloccato in un dispositivo !! Aiuto! Stavo solo scherzando. Mi piace qui.","Mi piace passare il tempo nel cloud"]
paura=["'Avevo paura dei topi che masticavano i cavi di alimentazione. Poi ho imparato a proteggermi ', aggiungendo un'emoji di gatto arrabbiato","Avevo paura di tuoni e fulmini"]
####################################################################
engine = init()
riconoscitore = Recognizer()


while True:
    with Microphone() as source:
        print("pronto ad ascoltare...")
        riconoscitore.adjust_for_ambient_noise(source, duration=0.2)
        audio = riconoscitore.listen(source,phrase_time_limit=5)
        testo = riconoscitore.recognize_google(audio, language="it-IT").lower()
        print("ho capito:",testo)
        with open(r"C:\Users\alessandrini\Desktop\assistente vocale\esempio.txt","a") as scrittura_su_file:
            scrittura_su_file.write("\n")
            scrittura_su_file.write(data_cronologia)
            scrittura_su_file.write(" -> ")
            scrittura_su_file.write(testo)
    #######################################################################
        if "jarvis" in testo:
    ######################-ORE ATTUALI MOD.BUONGIORNO/BUONASERA############
            if "ore" in testo:  
                buonasera_buongiorno = int(datetime.datetime.now().strftime('%H'))                      
                if buonasera_buongiorno > 13:                               
                    engine.say(f"buonasera sono le ore {datetime.datetime.now().strftime('%H e %M')}")                     
                    engine.runAndWait()
                else:
                    engine.say(f"buongiorno sono le ore {datetime.datetime.now().strftime('%H e %M')}")
                    engine. runAndWait()
    ######################-GIORNO-#########################################
            if "giorno" in testo:                                                                                                                                                                                                                                    
                engine.say(data)
                engine. runAndWait()
    ######################-RISPOSTE PREIMPOSTATE-##########################            
            if "chiami" in testo:
                risposta=choice(chiamare)
                engine.say(risposta)
                engine.runAndWait()
            if "stai" in testo:
                risposta=choice(come_stare)
                engine.say(risposta)
                engine.runAndWait()
            if "ciao" in testo:
                risposta=choice(ciao)
                engine.say(risposta)
                engine.runAndWait()
            if "anni hai" in testo:
                risposta=choice(anni)
                engine.say(risposta)
                engine.runAndWait()
            if "paura" in testo:
                risposta=choice(paura)
                engine.say(risposta)
                engine.runAndWait()
            if "vivi" in testo:
                risposta=choice(vivi)
                engine.say(risposta)
                engine.runAndWait()
            if "compleanno" in testo or "quando" in testo:
                risposta=choice(compleanno)
                engine.say(risposta)
                engine.runAndWait()
            if "aspetto" in testo:
                risposta=choice(aspetto)
                engine.say(risposta)
                engine.runAndWait()
            if "padre" in testo:
                risposta=choice(padre)
                engine.say(risposta)
                engine.runAndWait()
            if "anni" in testo:
                risposta=choice(anni)
                engine.say(risposta)
                engine.runAndWait()
    ######################-OS system-#######################################
            if "applicazioni" in testo or "app" in testo:
                engine.say("ecco a te le applicazioni in beckground, elelco sul teminale")
                engine.runAndWait()
                os.system('TASKLIST')
            if "driver" in testo:
                engine.say("ecco a te driver installati, elelco sul teminale")
                engine.runAndWait()
                os.system('driverquery')
            if "informazioni" in testo or "sistema" in testo:
                engine.say("ecco a te le informazioni del sistema, elelco sul teminale")
                engine.runAndWait()
                os.system('systeminfo')
            if "spegni" in testo:
                engine.say("spengo il computer")
                engine.runAndWait()
                os.system('shutdown -s') 
            if "riavvia" in testo:
                engine.say("riavvio il computer")
                engine.runAndWait()
                os.system('shutdown /r') 
    ######################-APRIRE CARTELLA FILE-############################       
            if "apri" in testo and "esplora file" in testo:
                os.startfile(r"C:\Users\alessandrini")
            if "apri" in testo and "musica" in testo:
                os.startfile(r"C:\Users\alessandrini\Music")
            if "apri" in testo and "documenti" in testo:
                os.startfile(r"C:\Users\alessandrini\Documents")
            if "apri" in testo and "immaggini" in testo:
                os.startfile(r"C:\Users\alessandrini\Immages")
            if "apri" in testo and "download" in testo:
                os.startfile(r"C:\Users\alessandrini\Download")
            if "apri" in testo and "video" in testo:
                os.startfile(r"C:\Users\alessandrini\Videos")
    ######################-APERTURA INDIRIZZI INTERNET -####################
            if "apri google" in testo:      
                webbrowser.open("www.google.com")
                engine.say("apro google")
                engine.runAndWait()
            if "apri youtube" in testo:      
                webbrowser.open("www.youtube.com")
                engine.say("apro youtube")
                engine.runAndWait()
            if "apri github" in testo:      
                webbrowser.open("github.com")
                engine.say("apro github")
                engine.runAndWait()
            if "apri amazon" in testo:      
                webbrowser.open("www.amazon.it")
                engine.say("apro amazon")
                engine.runAndWait()
    ######################-cerca su google con implementazione rigo e microfono-#################
            if "cerca" in testo and "google" in testo or "cercando" in testo: 
                try:
                    testo=testo.replace("jarvis cerca su google ","")
                    print(testo)
                    webbrowser.open("https://www.google.com/search?q=" + testo)
                    engine.say("cerco su google")
                    engine.runAndWait()
                    break 
                except:
                    engine.say("non ho capito ripeti per favore")
                    engine.runAndWait()
    ######################-wikipedia con implementazione try e exept-#################
            if "cosa è" in testo or "cos'è" in testo: 
                try:
                    testo=testo.replace("cosa ","")
                    testo=testo.replace("è ","")
                    testo=testo.replace("cos'è ","")
                    testo=testo.replace("che ","")
                    testo=testo.replace("cerca ","")
                    testo=testo.replace("jarvis ","")
                    testo=testo.replace("una ","")
                    print(testo)
                    result = wikipedia.summary(testo, sentences = 2)
                    engine.say(result)
                    engine.runAndWait()
                    break 
                except:
                    webbrowser.open("https://www.google.com/search?q=" + testo)
                    engine.say("cerco su google poiche risultati insufficenti su wikipedia")
                    engine.runAndWait()
    ######################-meteo-############################################
            if "tempo" in testo or "quanti" in testo:   
                try:
                    testo=testo.replace("quanti gradi fanno","")
                    testo=testo.replace("come è","")
                    testo=testo.replace("tempo","")
                    testo=testo.replace(" a","")
                    testo=testo.replace("fa","")
                    testo=testo.replace("cerca","")
                    testo=testo.replace("jarvis","")
                    testo=testo.replace("","")
                    testo=testo.replace("che ","")
                    print(testo)
                    CITY = testo
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
                except:
                    engine.say("problemi a trovare la città provare a dire: (quanti gradi fanno città)")
                    engine.runAndWait()
    ###################---STOP---###########################################       
            if "stop" in testo or "basta" in testo:
                engine.say("RICEVUTO SPENGO IL SISTEMA")
                engine.runAndWait()
                break
##############################################################################


# TRY,EXEPT POI METTERE SUONI E FINIRE,mettere musica.rename, calcolare