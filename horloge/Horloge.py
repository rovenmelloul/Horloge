import simpleaudio as sa
import time
from datetime import datetime
from threading import Thread, Event

class Horloge(Thread): 
    """
    Docstring for Horloge
    """
    #----------------Type of class variables---------------------#
    hour:int
    minute:int
    seconds:int
    regled_alarm:tuple
    set_timer:bool
    mode:str
    #----------------Type of class variables---------------------#

    def __init__(self)->None:
        super().__init__()
        self.set_timer = Event()
        self.set_timer.set()   
        self.mode = ""

    def run(self):
        self.start_main_loop()
        pass

    #TODO:make it private
    def take_all_inputs(self)->tuple:
        try:
            self.mode = input("Mode d'affichage : ") 
            afficher_heure = (
                int(input("Configurer votre Horloge : ")),
                int(input("Configurer votre Horloge : ")),
                int(input("Configurer votre Horloge : ")))
            self.hour,self.minute,self.seconds = afficher_heure
            regler_alarme = (
                int(input("Configurer votre alarme : ")),
                int(input("Configurer votre alarme : ")),
                int(input("Configurer votre alarme : ")))
            self.regled_alarm = regler_alarme
            return regler_alarme
        except ValueError:
            print("Nombres uniquement")
            self.regled_alarm = (0,0,0)
            return (0,0,0)
        pass

    def change_mode(self):
        copy_ = self.hour
        if self.mode == "PM/AM":
            if copy_ <= 12:
                suffixe = "AM"
            else:
                copy_ = self.hour-12
                suffixe = "PM"
            print(f"Time now: {copy_:02d}:{self.minute:02d}{suffixe}")
            print(f"""
                        ┌──────────────────────────┐
                        │      !!! ALARM !!!       │
                        │      !!! ALARM !!!       │
                        │                          │
                        │     ████  ██  ████  ████ │
                        │   ██      ██ ██    ██    │
                        │     ██    ██  ████  ████ │
                        │       ██  ██     ██    ██│
                        │     ████  ██  ████  ████ │
                        │                          │
                        │{self.hour}:{self.minute} AM       │
                        │                          │
                        │    Press ENTER to stop   │
                        └──────────────────────────┘
    """)
            time.sleep(1)
        else:
            print(self.hour, "h", self.minute, "m", self.seconds, "s")
            
            time.sleep(1)


    def ajust_time(self):
        print("Ajust time?")
        option = input("1 - Oui | 2 - Non: ")

        if option == "1":
            now = datetime.now()
            self.hour = now.hour
            self.minute = now.minute
            self.seconds = now.second
        else:
            return

    # “afficher_heure” 
    def show_time(hour):
        '''
        @parametr (heures, minutes, secondes)
        Docstring for show_time
        '''
        pass

    def play_sound(self):
        wave_obj = sa.WaveObject.from_wave_file("C:/Users/woter/LaPlateforme/Horloge/horloge/alarm-clock-1-29480.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        pass 

    # This function start counting time and have all main logic 
    def start_main_loop(self):
        while True:
            self.set_timer.wait()  
            self.change_mode()
            if self.regled_alarm[0] == self.hour and  self.regled_alarm[1] == self.minute and  self.regled_alarm[2] == self.seconds:
                    print("alarme sonne")
            if self.seconds < 60:
                self.seconds += 1  
            else:
                self.seconds = 0
                self.minute +=1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
        pass

