import tkinter as tk # interfaccia grafica
from tkinter import Canvas #interfacia grafica
import pyautogui #volume
################-interfaccia grafica-####################
app = tk.Tk()
canvas = Canvas(app)
canvas.pack()
app.geometry("250x250")
app.title("JARVYS")
app.resizable(False,False)

#+----------------------------------------------+#
#|              INTERFACCIA GRAFICA             |#
#+----------------------------------------------+#

def interfaccia():
    def volume_up():
        print("volume up")
        pyautogui.press("volumeup")
        canvas.create_oval(10, 10, 240, 240, outline="#f11",width=10)
    def volume_down():
        print("volume down")
        pyautogui.press("volumedown")
        canvas.create_oval(10, 10, 240, 240, outline="#fb0",width=10)
    def no_voice():
        global testo
        print("no voce")
        p2 = Process(target = assstentevocale)
        p2.terminate()
    def voice():
        print("voce")
        p2 = Process(target = assstentevocale)
        p2.start()
        canvas.create_oval(10, 10, 240, 240, outline="#05f",width=10)

    bt_volume_up=tk.Button(text="+",command=volume_up,width=4,height=2)
    bt_volume_up.place(x=105,y=25)
    bt_volume_down=tk.Button(text="-",command=volume_down,width=4,height=2)
    bt_volume_down.place(x=105,y=185)
    bt_no_voice=tk.Button(text="/",command=no_voice,width=4,height=2)
    bt_no_voice.place(x=30,y=110)
    bt_voice=tk.Button(text="@",command=voice,width=4,height=2)
    bt_voice.place(x=180,y=110)
    app.mainloop()

#+----------------------------------------------+#
#|            ATTIVAZIONE ABE FUNZIONI          |#
#+----------------------------------------------+#

if __name__=='__main__':
     p1 = Process(target = interfaccia)
     p1.start()
     p2 = Process(target = assstentevocale)
     p2.start()