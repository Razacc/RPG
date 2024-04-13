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


if __name__ == '__main__':
    unittest.main()
