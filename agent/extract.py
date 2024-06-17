import os
import socket
import netifaces
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Chemin du dossier de téléchargements
DOWNLOADS_DIR = "/home/kali/Downloads"

class DownloadsHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DOWNLOADS_DIR, **kwargs)

def get_local_ip():
    # Obtient l'adresse IP de l'interface réseau principale
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface != "lo":  # Ignorer l'interface loopback
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addrs:
                return addrs[netifaces.AF_INET][0]['addr']
    return None

def run_server(): # Fonction qui va démarrer le serveur HTTP.
    try:
        server_address = ('', 8888) # Démarrer le serveur HTTP sur le port 8888 et l'ip disponible du serveur
        httpd = HTTPServer(server_address, DownloadsHTTPRequestHandler)
        
        # Obtenir l'adresse IP de l'interface réseau principale
        local_ip = get_local_ip()
        if local_ip:
            print(f"Serveur démarré sur http://{local_ip}:8888")
        else:
            print("Impossible de récupérer l'adresse IP de l'interface réseau.")
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")


###################
### Utilisation ###
# Lancer le script : python3 extract.py
# Sur le PC (contrôleur) :
# - Ouvrir un navigateur web.
# - http://adresse_ip_de_votre_vm:8888). 
# - On devrait voir la liste des fichiers et dossiers dans le dossier de téléchargements de la VM.
# - Cliquer sur les liens pour visualiser les fichiers.
# !!! la VM et le PC sont sur le même réseau + pare-feu de la VM autorise les connexions entrantes sur le port 8000. !!! 
