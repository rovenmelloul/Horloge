import time

class Horloge:
    afficher_heure = (0,0,0)
    try:
        afficher_heure = (
            int(input("choisir heure : ")),
            int(input("choisir minute : ")),
            int(input("choisir seconde : "))
        )
    except ValueError:
        print("Nombres uniquement")

    def __init__(self):
        self.heures, self.minutes, self.secondes = self.afficher_heure
        

    def temps(self):
        try:
            regler_alarme = (
                    int(input("choisir heure : ")),
                    int(input("choisir minute : ")),
                    int(input("choisir seconde : ")))
        except ValueError:
            regler_alarme = (0,0,0)
            print("Nombres uniquement")
        print(regler_alarme)


        if regler_alarme == (0, 0, 0):
            print("pas d'alarme")
            return self.temps()
        while True:
            time.sleep(1)
            print(self.heures, "h", self.minutes, "m", self.secondes, "s")
            if regler_alarme[0] == self.heures and regler_alarme[1] == self.minutes and regler_alarme[2] == self.secondes:
                    print("alarme sonne")
            if self.secondes < 60:
                self.secondes += 1  
            else:
                self.secondes = 0
                self.minutes +=1
            if self.minutes == 60:
                self.minutes = 0
                self.heures += 1
                if self.heures == 24:
                    self.heures = 0
    
 
horloge = Horloge()
horloge.temps()