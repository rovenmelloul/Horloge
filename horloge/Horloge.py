import simpleaudio as sa

class Horloge: 
    """
    Docstring for Horloge

    """
    #Type of class variables 
    hour:int
    minute:int
    seconds:int
    set_timer:bool
    #Type of class variables 

    def __init__(self):
        pass

    def change_mode(self):
        pass

    def set_time(self):
        pass

    def ajust_time(self):
        pass
    
    def play_sound(self):
        wave_obj = sa.WaveObject.from_wave_file("C:/Users/woter/LaPlateforme/Horloge/horloge/alarm-clock-1-29480.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        pass 

h = Horloge()
h.play_sound()