# coding: utf-8
import re
"""

MUSICIEN(#id_mus,nom,prenom,instrument,style_musical,estLive,estDemat,estDispo,visuel)
CONTENU_MUSICIEN(#id_con,url)
GROUPE(#id_gro, nom,style_musical, estLive, estDemat, visuel)
je mets les entites telles quelles ds une liste de relations



MUSICIEN-(O,n)-APPARTIENTA-(1,n)-GROUPE
MUSICIEN-(O,n)-POSSEDE-(1,1)-CONTENU_MUSICIEN
"""

# doit donner :
#
def isEntite(ligne):
    """DEBUT_LIGNE,MOT,'(',NIMP """
    """re.match(pat, ch, drap) -> objet_match
    objet_match.group(0) renvoie tt le match
    """
    debut_ligne='^'
    mot='\w+'
    parenth_ouvrante='[(]'
    nimp='.+'
    liste_regexp = [ debut_ligne, mot, parenth_ouvrante,
            nimp ]
    pattern_entite = ''.join(liste_regexp)
    #pattern_entite = "\w+\(.*"
    objet_pattern = re.match(pattern_entite,ligne)
    if objet_pattern is not None:
        verite = True
    else:
        verite = False
    return verite
 
def isAssoc(ligne):
    debut_ligne='^'
    mot='\w+'
    tiret_separatif='-'
    nimp='.+'
    liste_regexp = [ debut_ligne, mot, tiret_separatif,
            nimp ]
    pattern_assoc = ''.join(liste_regexp)
    #pattern_assoc = "^\w+-[(].+"
    objet_pattern = re.search(pattern_assoc, ligne)
    if objet_pattern is not None:
        verite = True
    else:
        verite = False
    return verite
 
 

def parse_entite(ligne_entite):
    nom = extraireNom(ligne_entite)
    print("nom:",nom)
    parametres = extraireParams(ligne_entite)
    print("chaine_params:", parametres)
    liste_params = getListeParams(parametres)
    print("liste_params:", liste_params)
    return {'nom': nom, 'liste_params': liste_params} 

def parse_assoc(ligne_assoc):
    pass
    TODO


def extraireNom(chaine):
    nom, _  = chaine.split("(")
    return nom

def extraireParams(chaine):
    avant_parent, _ = chaine.split(")")
    _, chaine_champs = avant_parent.split("(")
    return chaine_champs


def getListeParams(chaine):
    #met les parametres separes par une virgule dans une liste.
    #s il n y a pas de param, parce qu on a appele getListeParams avec une chaine '',
    # split va renvoyer [''] (chaine vide de lg1
    # je souhaite qu elle renvoie [] (chaine vide de lg 0 )
    liste_params = chaine.split(",")
    if liste_params == ['']:
        liste_params = []

    return liste_params


"""
def isEntite(ligne):
    "DEBUT_LIGNE,MOT,'(',NIMP "
    "re.match(pat, ch, drap) -> objet_match
    objet_match.group(0) renvoie tt le match
    "
    debut_ligne='^'
    mot='\w+'
    parenth_ouvrante='[(]'
    nimp='.+'
    fin_ligne='$'
    liste_regexp = [ debut_ligne, mot, parenth_ouvrante,
            nimp, fin_ligne ]
    chaine_regexp = ''.join(liste_regexp)
    print(chaine_regexp)
    objet_pattern = re.compile(chaine_regexp)
    objet_match = objet_pattern.search(ligne)
    chaine_resultat = objet_match.group(0)
    return chaine_resultat
"""


"""
memoriser liste des enttites telles quues 
MUSICIEN(#id_mus,nom,....), CONTENU_MUSICIEN, GROUPE.

une association n,m devient une relation (#id_mus#,#id_groupe)

rien à faire
APPARTIENTA relation n,m. donc APPARTIENTA devient une relation



"""
"""
regle1 les entites

MUSICIEN(#id_mus, nom, prenom, instrument, style_musical, estLive, estDemat, estDispo, visuel)
CONTENU_MUSICIEN(#id_con,url)
GROUPE(#id_gro, nom,style_musical, estLive, estDemat, visuel)

regle2 trier asso binaire 
-> prendre les card max de chaque coté de l association, 
assobinaire 1:1 si aucun à n, 1:n si une des 2 à n, n:m si 2 cardinalites à n

regle 1:n l identite but coté n donne identifiant comme fk à la source


regle3 n:m l association est representee comme une relation, dont la pk est composée des deux pk des relations . cette clef est à la fois primaire et etrangere. à priori elle doit porter une autre ppt. 

regle 4 asso 1:1
comme 1:n . en prendre un au pif qui donne à l autre
la clef etrangere recoit contrainte d unicite et de non vacuité

regle 5
entite reflexive (meme entite de chaque coté de l asso) et 1,n:
  -> rajouter une fk de meme nom que la pk comme 1,n
  MAIS il faudra renommer cette fk puisque pk du meme nom existe deja
  ds la meme relaiton. donc mettre commentaires pour guider dans
  ce sens 
entite reflexive et n,m:
    -> comme n:m: creer une asso. l asso recoit les deux pk MAIS il faudra renommer une des deux fk l une impliquant la source, l autre la dest, donc mes petites notatons de medre ne marcheront pas, il faudra retoucher la source ou revoir la notaiton
generer des commentaires pour guider suffiront je pense




entite n aire 

"""
