# importations et variables
import http.server, requests
server = http.server.HTTPServer    # classe du serveur HTTP
handler = http.server.CGIHTTPRequestHandler    # classe du gestionnaire
handler.cgi_directories = ["/cgi-bin"]
PORT = 8000
server_address = ("", PORT)

#TODO initialisation avec le contrôleur
print("Entrez l'ip et port du contrôleur :") 
ControllerIP = input("IP -> ")
ControllerPort = input("Port -> ")
print("Entrez le nom du nouvel agent :")
AgentName = input("Nom -> ")
ControllerUrl = "http://"+ControllerIP+":"+ControllerPort+"/cgi-bin/enroll.cgi?name="+AgentName
# envoi de la requête
response = requests.get(ControllerUrl)
if response.status_code == 200 :
	print("Connexion avec le contrôleur établie")
else :
	print("Echec de la connexion")

# lancement du serveur
print("Agent actif sur le port : ",PORT)
httpd = server(server_address, handler)   # objet "serveur"
httpd.serve_forever()
