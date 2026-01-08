from pynput import keyboard
from .Horloge import Horloge
from threading import Thread, Event

class InputChecker(Thread):
    def __init__(self,horloge:Horloge):
        super().__init__() #heritage for 
        self.on = False  # définition de l'état
        self.horloge = horloge

    def run(self):
        print("\"Q\" pour activer et désactiver")
        print("appuie sur Echap pour arrêter")

        def on_press(key):
            try:
                if key.char == 'q':
                    self.on = not self.on  # interupteur
                    state = "activer" if self.on else "desactiver"
                    print(f" état: {state}")
                    if self.horloge.set_timer.is_set():
                        self.horloge.set_timer.clear()  # pquse
                    else:
                        self.horloge.set_timer.set() 
                    print("Alarm was stopped")
            except AttributeError:
                if key == keyboard.Key.esc:
                    print("arrêt...")
                    return False  # arrêter la fonction

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

