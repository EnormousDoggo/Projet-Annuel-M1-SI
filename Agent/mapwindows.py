import socket
import threading

""" Fonction pour obtenir l'adresse IP locale et le masque de sous-réseau """
def get_local_ip_and_subnet_mask():
    try:
        # Obtenir l'adresse IP locale
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Connexion à une adresse quelconque pour obtenir l'adresse locale
        local_ip = sock.getsockname()[0]
        sock.close()

        # Obtenir le masque de sous-réseau correspondant à l'adresse IP locale
        parts = local_ip.split('.')
        if len(parts) != 4:
            return None, None

        first_octet = int(parts[0])
        if first_octet <= 127:
            subnet_mask = '255.0.0.0'
        elif first_octet <= 191:
            subnet_mask = '255.255.0.0'
        elif first_octet <= 223:
            subnet_mask = '255.255.255.0'
        else:
            return None, None

        return local_ip, subnet_mask

    except (socket.error, ValueError):
        return None, None

""" Dictionnaire permettant de recueillir les hostnames des machines connectées sur un réseau """
host = {}

""" Classe définissant le thread de scan d'adresse IP servant à récupérer le hostname """
class NetscanThread(threading.Thread):

    def __init__(self, address):
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        try:
            hostname, alias, _ = socket.gethostbyaddr(address)
            global host
            host[address] = hostname
        except socket.herror:
            host[address] = None

def scanNetwork():
    local_ip, subnet_mask = get_local_ip_and_subnet_mask()
    print("Agent : "+local_ip, subnet_mask)

    if local_ip and subnet_mask:
        # Générer la liste des adresses IP à scanner
        network_prefix = '.'.join(local_ip.split('.')[:3])  # Obtient les trois premiers octets de l'adresse IP
        addresses = [network_prefix + '.' + str(ping) for ping in range(1, 255)]
        # todo scan selon le masque subnet_mask

        print()
        
        threads = []

        # Créer les threads de scan
        netscanthreads = [NetscanThread(address) for address in addresses]
        for thread in netscanthreads:
            thread.start()
            threads.append(thread)

        # Attendre que tous les threads se terminent
        for t in threads:
            t.join()
        
        output = {}
        # Afficher les résultats
        for address, hostname in host.items():
            if hostname is not None:
                output[address]=hostname
        return output
        
    else:
        return("Unable to retrieve local IP address and subnet mask.")