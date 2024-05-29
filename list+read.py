import os

def afficher_arborescence(dossier, prefixe=''):
    try:
        # Vérifier si le chemin est un dossier existant
        if os.path.isdir(dossier):
            # Afficher le nom du dossier actuel avec le préfixe
            print(prefixe + os.path.basename(dossier) + os.path.sep)
            # Liste des éléments dans le dossier
            elements = os.listdir(dossier)
            # Parcourir les éléments
            for index, element in enumerate(sorted(elements)):
                # Construire le chemin complet de l'élément
                chemin_element = os.path.join(dossier, element)
                # Vérifier si l'élément est un dossier
                if os.path.isdir(chemin_element):
                    # Afficher le nom du dossier avec un "/"
                    if index == len(elements) - 1:
                        print(prefixe + '└── ' + element + os.path.sep)
                    else:
                        print(prefixe + '├── ' + element + os.path.sep)
                else:
                    # Afficher le nom du fichier
                    if index == len(elements) - 1:
                        print(prefixe + '└── ' + element)
                    else:
                        print(prefixe + '├── ' + element)
        else:
            print("Le chemin spécifié n'est pas un dossier existant.")
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

# Fonction pour lire le contenu du fichier ou naviguer dans les répertoires
def lire_fichier_ou_naviguer(chemin_fichier, dossier_courant):
    if chemin_fichier.startswith("lire "):
        nom_fichier = chemin_fichier[5:]
        chemin_fichier_complet = os.path.join(dossier_courant, nom_fichier)
        contenu = lire_contenu_fichier(chemin_fichier_complet)
        if contenu:
            print("\nContenu du fichier '{}' :\n".format(chemin_fichier_complet))
            print(contenu)
    elif chemin_fichier != "stop":
        dossier_a_afficher = os.path.join(dossier_courant, chemin_fichier)
        print("\nDossier courant :", dossier_a_afficher)
        afficher_arborescence(dossier_a_afficher)

# Fonction principale
def main():
    # Définir le répertoire de base comme étant le répertoire courant
    dossier_courant = os.getcwd()
    print("Dossier courant :", dossier_courant + os.path.sep)
    afficher_arborescence(dossier_courant)  # Affichage initial de l'arborescence

    # Boucle tant que l'utilisateur n'entre pas "stop"
    commande = ""
    while commande != "stop":
        commande = input("\nEntrez 'lire nom_du_fichier' pour lire un fichier, entrez un chemin relatif pour naviguer, ou 'stop' pour quitter : ")
        lire_fichier_ou_naviguer(commande, dossier_courant)

if __name__ == "__main__":
    main()

###################
### Utilisation ###
# python3 list+read.py
# entrer le chemin absolu pour vous deplacer (c long, mais moins compliqué pour les retours arrière)
# entrer "lire le_nom_du_fichier" pour voir le contenu de celui-ci 
# entrer "stop" pour arrêter la boucle ou le classic ctrl+c
