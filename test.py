import unittest
from RPG import Personnage

class TestPersonnage(unittest.TestCase):
    def test_creation_personnage(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        self.assertEqual(joueur.nom, "Joueur 1")
        self.assertEqual(joueur.classe, "Guerrier")
        self.assertEqual(joueur.niveau, 1)
        self.assertEqual(joueur.points_de_vie, 10)
        self.assertEqual(joueur.points_d_attaque, 5)
        self.assertEqual(joueur.points_de_defense, 5)

    def test_changement_classe(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.changer_classe("Mage")
        self.assertEqual(joueur.classe, "Mage")

    def test_increment_niveau(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.increment_niveau()
        self.assertEqual(joueur.niveau, 2)

    def test_reduire_points_de_vie(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.reduire_points_de_vie(3)
        self.assertEqual(joueur.points_de_vie, 7)

    def test_augmenter_points_d_attaque(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.increment_niveau()
        joueur.augmenter_points_d_attaque(2)
        self.assertEqual(joueur.points_d_attaque, 7)

    def test_augmenter_points_de_defense(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.increment_niveau()
        joueur.augmenter_points_de_defense(2)
        self.assertEqual(joueur.points_de_defense, 7)

    def test_points_de_vie_negatifs(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.reduire_points_de_vie(15)
        self.assertLessEqual(joueur.points_de_vie, 0)

    def test_niveau_tres_eleve(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        for _ in range(1000):
            joueur.increment_niveau()
        self.assertGreaterEqual(joueur.niveau, 1000)

    def test_creation_personnage_vide(self):
        joueur = Personnage("", "")
        self.assertEqual(joueur.nom, "")
        self.assertEqual(joueur.classe, "")

    def test_personnage_avec_nom_long(self):
        nom_long = "a" * 100
        joueur = Personnage(nom_long, "Guerrier")
        self.assertEqual(joueur.nom, nom_long)

    def test_changement_classe_invalide(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.changer_classe("Invalide")
        self.assertNotEqual(joueur.classe, "Invalide")

    def test_augmenter_points_d_attaque_max(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.augmenter_points_d_attaque(100)
        self.assertGreaterEqual(joueur.points_d_attaque, 100)

    def test_augmenter_points_de_defense_max(self):
        joueur = Personnage("Joueur 1", "Guerrier")
        joueur.augmenter_points_de_defense(100)
        self.assertGreaterEqual(joueur.points_de_defense, 100)

if __name__ == '__main__':
    unittest.main()
