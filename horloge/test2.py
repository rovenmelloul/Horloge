import time

class Horloge:
    # -------------------------
    # EXISTANT
    afficher_heure = (
        int(input("choisir heure : ")),
        int(input("choisir minute : ")),
        int(input("choisir seconde : "))
    )

    # 🔹 AJOUT 1 : choix du mode d'affichage
    mode_affichage = int(input("Choisir mode d'affichage (12 ou 24) : "))

    # -------------------------
    def __init__(self):
        self.heures, self.minutes, self.secondes = self.afficher_heure

    # 🔹 AJOUT 2 : fonction d'affichage
    def afficher(self):
        if self.mode_affichage == 24:
            print(self.heures, "h", self.minutes, "m", self.secondes, "s")
        else:
            heure = self.heures
            suffixe = "AM"

            if heure == 0:
                heure = 12
            elif heure == 12:
                suffixe = "PM"
            elif heure > 12:
                heure -= 12
                suffixe = "PM"

            print(f"{heure:02d}:{self.minutes:02d}:{self.secondes:02d} {suffixe}")

    # -------------------------
    def temps(self):
        while True:
            time.sleep(1)

            # 🔹 MODIFICATION 3 : on remplace le print par l'affichage dynamique
            self.afficher()

            if regler_alarme == 0:
                print("pas d'alarme")
            else:
                if self.regler_alarme[0] == self.heures and self.regler_alarme[1] == self.minutes and self.regler_alarme[2] == self.secondes:
                    print("alarme sonne")

            if self.secondes < 60:
                self.secondes += 1
            else:
                self.secondes = 0
                self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0
                self.heures += 1
                if self.heures == 24:
                    self.heures = 0

    # -------------------------
    # EXISTANT
    regler_alarme = (
        int(input("choisir heure si 0 partout pas d'alarme : ")),
        int(input("choisir minute : ")),
        int(input("choisir seconde : "))
    )


# -------------------------
horloge = Horloge()
horloge.temps()