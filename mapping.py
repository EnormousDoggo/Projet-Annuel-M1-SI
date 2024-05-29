import subprocess
import sys
import netifaces
import socket

def install_package(package):
    """Installe le package spécifié en utilisant pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Vérifie si 'nmap' est installé, sinon l'installe
try:
    import nmap
except ImportError:
    print("Le module 'python-nmap' n'est pas installé. Installation en cours...")
    install_package("python-nmap")
    import nmap

# Vérifie si 'netifaces' est installé, sinon l'installe
try:
    import netifaces
except ImportError:
    print("Le module 'netifaces' n'est pas installé. Installation en cours...")
    install_package("netifaces")
    import netifaces

def get_network_info():
    """Récupère l'adresse IP et le masque de sous-réseau des interfaces réseau sauf loopback."""
    interfaces = netifaces.interfaces() # Obtient la liste des interfaces réseau
    for iface in interfaces:
        if iface == 'lo':
            continue  # Ignorer l'interface loopback
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ip_info = addrs[netifaces.AF_INET][0]
            ip_address = ip_info['addr'] # Adresse IP de l'interface
            netmask = ip_info['netmask'] # Masque de sous-réseau de l'interface
            return ip_address, netmask # Retourne l'adresse IP et le masque
    return None, None # Retourne None si aucune interface valide n'est trouvée

def calculate_network_range(ip, netmask):
    """Calcule la plage de réseau à partir de l'adresse IP et du masque de sous-réseau."""
    ip_parts = list(map(int, ip.split('.')))
    netmask_parts = list(map(int, netmask.split('.')))
    network_parts = [ip_parts[i] & netmask_parts[i] for i in range(4)]
    network = '.'.join(map(str, network_parts))
    bits = sum([bin(part).count('1') for part in netmask_parts])
    return f"{network}/{bits}" # Retourne la plage de réseau en notation CIDR (ip/masque)

def get_hostname(ip):
    """Récupère le nom de l'hôte pour une adresse IP donnée."""
    try:
        return socket.gethostbyaddr(ip)[0] # Tente de résoudre le nom de l'hôte
    except socket.herror:
        return None # Retourne None si la résolution échoue

# Récupérer l'adresse IP et le masque de sous-réseau
ip_address, netmask = get_network_info()

if ip_address and netmask:
    network_range = calculate_network_range(ip_address, netmask)

    # Message indiquant que le script est en train d'analyser le réseau
    print(f"Analyse du réseau en cours ({network_range}), veuillez patienter...")

    # Initialiser le scanner
    nm = nmap.PortScanner()

    # Scanner le réseau local avec résolution DNS
    nm.scan(network_range, arguments='-sP -R')

    # Afficher les hôtes et leur état
    print("Résultats de l'analyse du réseau :")
    for host in nm.all_hosts():
        # Récupérer le nom de l'hôte avec Nmap, sinon utiliser la fonction de résolution alternative
        hostname = nm[host].hostname()
        if not hostname:
            hostname = get_hostname(host) or "unknown"
        print(f"Host : {host} ({hostname})")
        print(f"State : {nm[host].state()}")

        # Afficher les informations sur les interfaces réseau
        if 'addresses' in nm[host]:
            for addr_type, addr in nm[host]['addresses'].items():
                print(f"  {addr_type} : {addr}")
        print()
else:
    print("Impossible de récupérer les informations réseau.")

###################
### Utilisation ###
# python3 mapping.py
# attendre le résultat
