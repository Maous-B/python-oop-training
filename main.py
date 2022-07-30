


class Personne(object):
    def __init__(self, nom : str, taille : int, age : int, poids : int):
        self.nom = nom
        self.taille = taille
        self.age = age
        self.poids = poids

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom}, je fais {self.taille} mètres, j'ai {self.age} ans et je fais {self.poids} kg")

    def est_majeur(self):
        if self.age < 18:
            print("La personne est mineure")
        else:
            print("La personne est majeure")

class Arme(object):
    def __init__(self, nom : str, taille_du_chargeur : int, cadence_de_tir : int):
        self.nom = nom
        self.taille_du_chargeur = taille_du_chargeur
        self.cadence_de_tir = cadence_de_tir

    def tirer(self):
        print(f"L'arme {self.nom} a tiré avec une cadence de tir de {self.cadence_de_tir} coups/min")

    def informations_de_l_arme(self):
        print(f"Nom de l'arme : {self.nom}\nTaille du chargeur : {self.taille_du_chargeur}\nCadence de tir : {self.cadence_de_tir} coups/min")

class Voiture(object):
    def __init__(self, marque: str, couleur: str, vitesse: int):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse
    
    def rouler(self):
        print(f"La {self.marque} de couleur {self.couleur} roule à {self.vitesse} km/h")

personne1 = Personne("Jean", 175, 18, 80)
personne1.se_presenter()
personne2 = Personne()
ak47 = Arme("AK47", 240, 450)
ak47.tirer()
ak47.informations_de_l_arme()
ferrari = Voiture("Ferrari", "rouge", 300)
ferrari.rouler()
personne1.est_majeur()