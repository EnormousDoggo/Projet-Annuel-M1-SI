import os

def afficher_arborescence(dossier, prefixe=''):
    try:
        # Vérifier si le chemin est un dossier existant
        if os.path.isdir(dossier):
            # Afficher le nom du dossier actuel avec le préfixe
            print(prefixe + os.path.basename(dossier) + os.path.sep)
            # Liste des éléments dans le dossier
            elements = os.listdir(dossier)
            return elements
        else:
            print("Le chemin spécifié n'est pas un dossier existan  t.")
    except Exception as e:
        print("Une erreur s'est produite :", e)

def lire_contenu_fichier(nom_fichier):
    try:
        # Ouvrir le fichier en mode lecture
        with open(nom_fichier, 'r') as fichier:
            # Lire le contenu du fichier
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        print("Le fichier '{}' n'existe pas.".format(nom_fichier))
    except PermissionError:
        print("Vous n'avez pas la permission de lire le fichier '{}'.".format(nom_fichier))
    except Exception as e:
        print("Une erreur s'est produite :", e)
