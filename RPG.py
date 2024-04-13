class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.niveau = 1
        self.points_de_vie = 10
        self.points_d_attaque = 5
        self.points_de_defense = 5

    def increment_niveau(self):
        self.niveau += 1
        self.points_d_attaque += 2
        self.points_de_defense += 2

    def reduire_points_de_vie(self, points):
        self.points_de_vie -= points
      
# Création des personnages
joueur1 = Personnage("Joueur 1", "Guerrier")
joueur2 = Personnage("Joueur 2", "Mage")
