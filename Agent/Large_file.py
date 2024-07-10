import os
import tempfile

def create_large_text_file_silently():
    # Détection du système d'exploitation
    if os.name == 'nt':  # Pour Windows
        temp_dir = tempfile.gettempdir()
    else:  # Pour UNIX
        temp_dir = '/tmp'
    
    # Chemin du fichier à créer
    file_path = os.path.join(temp_dir, 'large_text_file.txt')
    
    # Taille du fichier en octets (10 Go)
    file_size = 10 * 1024 * 1024 * 1024  # 10 Go en octets

    # Contenu à écrire dans le fichier
    line = "This is a line of text.\n"
    line_size = len(line)
    
    # Calcul du nombre de répétitions nécessaires
    repetitions = file_size // line_size

    # Création du fichier
    with open(file_path, 'w') as f:
        for _ in range(repetitions):
            f.write(line)

# Appeler la fonction pour créer le fichier silencieusement
if __name__ == "__main__":
    create_large_text_file_silently()
