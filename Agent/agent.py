# importations et variables
import requests, re, time, sys

PORT = 12345
run = True

arguments = sys.argv[1:]
try:
	ControllerIP = arguments[0]
except:
	print("Entrez l'ip du contrôleur :") 
	ControllerIP = input("IP -> ")
try:
	ControllerPort = arguments[1]
except:
	print("Entrez le port du contrôleur :") 
	ControllerPort = input("Port -> ")
try:
	AgentName = arguments[2]
except:
	print("Entrez le nom du nouvel agent :")
	AgentName = input("Nom -> ")
ControllerUrl = "http://"+ControllerIP+":"+ControllerPort
# envoi de la requête
response = requests.get(ControllerUrl+"/enroll/"+AgentName)
if response.status_code == 200 :
	print("Connexion avec le contrôleur établie")
else :
	print("Echec de la connexion")
	run=False

# lancement du serveur
while run == True :
    response = requests.get(ControllerUrl+"/instruction/"+AgentName)
    if response.text == "quit":
        run = False
    if response.text == "whoami":
        # appeler le script 
        requests.post(ControllerUrl+"/")
    if response.text == "list directories":
        # appeler le script 
        requests.post(ControllerUrl+"/")
    if response.text == "drop file ":
        # appeler le script 
        requests.post(ControllerUrl+"/")
    time.sleep(2)
        