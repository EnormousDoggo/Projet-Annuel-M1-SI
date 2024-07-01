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

def get_domain():
    if platform.system() == "Windows":
        # Commande pour obtenir le nom du domaine sur Windows
        command = "echo %userdomain%"
        try:
            domain = subprocess.check_output(command, shell=True, universal_newlines=True)
            return domain.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Not applicable"
