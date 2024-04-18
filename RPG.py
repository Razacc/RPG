class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.niveau = 1
        self.points_de_vie = 10
        self.points_d_attaque = 5
        self.points_de_defense = 5
      
    def changer_classe(self, nouvelle_classe):
        if nouvelle_classe in ["Guerrier", "Mage", "Archer"]:
            self.classe = nouvelle_classe
        else:
            print("Classe invalide.")

    def increment_niveau(self):
        self.niveau += 1

    def reduire_points_de_vie(self, points):
        self.points_de_vie -= points
        if self.points_de_vie <= 0:
            print("Le personnage est mort.")
            self.points_de_vie = 0

    def augmenter_points_d_attaque(self, points):
        self.points_d_attaque += points

    def augmenter_points_de_defense(self, points):
        self.points_de_defense += points
