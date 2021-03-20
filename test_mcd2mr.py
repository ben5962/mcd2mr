# encoding: utf-8


# je veux ecrire une methode qui, recevant une ligne 
# indique s il s agit d une ligne contenant la declaration d une entite
# ou la ligne contenant la declaration d une association

import unittest
import mcd2mr


class TestMcd2Mr(unittest.TestCase):
    def test_reconnait_entiteOK(self):
        ligne_entite = "Musicien(#id_mus, nom, prenom)"
        resultat_obtenu = mcd2mr.isEntite(ligne_entite)
        resultat_attendu = True
        self.assertEqual(resultat_attendu, resultat_obtenu)

    def test_reconnait_pas_nonentiteOK(self):
        ligne_entite = "Musicien-(1,n)-APPARTIENT..."
        resultat_obtenu = mcd2mr.isEntite(ligne_entite)
        resultat_attendu = False
        self.assertEqual(resultat_attendu, resultat_obtenu)

    def test_reconnait_assocOk(self):
        ligne_asso = "Musicien-(1,n)-..."
        resultat_obtenu = mcd2mr.isAssoc(ligne_asso)
        resultat_attendu = True
        self.assertEqual(resultat_attendu, resultat_obtenu)

    def test_reconnaitpas_nonassocOK(self):
        ligne_entite = "Musicien(#id,"
        resultat_obtenu = mcd2mr.isAssoc(ligne_entite)
        resultat_attendu = False
        self.assertEqual(resultat_attendu, resultat_obtenu)
    def test_parse_entite(self):
        ligne_entite = "Musicien(#id,essai,autre_essai,troisieme)"
        resultat_obtenu = mcd2mr.parse_entite(ligne_entite)
        resultat_attendu = {'nom': "Musicien", 'liste_params': ["#id", "essai", "autre_essai", "troisieme"]} 
        self.assertEqual(resultat_obtenu, resultat_attendu)


