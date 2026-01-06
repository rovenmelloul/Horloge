import simpleaudio as sa

class Horloge: 
    """
    Docstring for Horloge
    """
    #Type of class variables 
    hour:int
    minute:int
    seconds:int

    regled_alarm:tuple
    set_timer:bool
    #Type of class variables
    # 
    # 
    def __init__(self)->None:
        self.set_timer = True
        pass

    #TODO:make it private
    def take_all_inputs(self)->tuple:
        try:
            afficher_heure = (
                int(input("choisir heure : ")),
                int(input("choisir minute : ")),
                int(input("choisir seconde : ")))
            print("")
            regler_alarme = (
                int(input("choisir heure : ")),
                int(input("choisir minute : ")),
                int(input("choisir seconde : ")))
            return regler_alarme
        except ValueError:
            print("Nombres uniquement")
            return (0,0,0)
        pass

    def wait_for_options()->None:
        pass

    def change_mode(self):
        pass

    def set_time(self):
        pass

    def ajust_time(self):
        pass

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
    def start_main_loop(self)->function:
        while self.set_timer is True:
            self.seconds += 1
            
            pass
        pass


h = Horloge()
h.take_all_inputs()