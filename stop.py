from pynput import keyboard
import threading


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.on = False  # définition de l'état

    def run(self):
        print("\"Q\" pour activer et désactiver")
        print("appuie sur Echap pour arrêter")

        def on_press(key):
            try:
                if key.char == 'q':
                    self.on = not self.on  # interupteur
                    state = "activer" if self.on else "desactiver"
                    print(f" état: {state}")
            except AttributeError:
                if key == keyboard.Key.esc:
                    print("arrêt...")
                    return False  # arrêter la fonction

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


thread = MyThread()
thread.start()