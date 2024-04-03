#Test


import platform
import subprocess
import requests

def get_os_version():
    return platform.platform()

def get_installed_applications():
    if platform.system() == "Windows":
        # Commande pour obtenir la liste des programmes installés sur Windows
        command = "wmic product get name"
    elif platform.system() == "Linux":
        # Commande pour obtenir la liste des packages installés sur Linux (Debian/Ubuntu)
        command = "dpkg-query -f '${binary:Package}\n' -W"
    elif platform.system() == "Darwin":
        # Commande pour obtenir la liste des applications installées sur macOS
        command = "ls /Applications"
    else:
        return "Unsupported OS"
    
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return output.strip().split('\n')[1:]  # Ignorer le premier élément qui est l'en-tête de la sortie de la commande
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def send_data_to_server(data):
    url = "http://localhost:8888/enroll.cgi"  # Endpoint pour l'enregistrement des agents sur le serveur local
    try:
        response = requests.post(url, data={"name": "Scanner", "info": data})
        if response.status_code == 200:
            print("Données envoyées avec succès.")
        else:
            print(f"Erreur lors de l'envoi des données: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'envoi des données: {e}")

def main():
    os_version = get_os_version()
    installed_applications = get_installed_applications()

    data = {
        "OS Version": os_version,
        "Installed Applications": installed_applications
    }

    send_data_to_server(data)

if __name__ == "__main__":
    main()
