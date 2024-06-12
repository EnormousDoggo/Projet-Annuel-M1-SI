# importations et variables
import requests, re, time, sys
import screenshot, power, scan

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

def sendJsonData(instruction, data):
    url=ControllerUrl+"/data/"+AgentName+"/"+instruction
    requests.post(url, json=data)

# lancement du serveur
while run == True :
    response = requests.get(ControllerUrl+"/instruction/"+AgentName)
    if response.status_code != 200 or response.text == "quit":
        run = False
        print("Connexion avec le contrôleur terminée")
    if response.text == "screenshot":
        print("taking screenshot")
        screenshot.capture()
    if response.text == "restart":
        print("restarting")
        power.restart()
    if response.text == "scanapps":
        print("scanning installed applications")
        sendJsonData("scanapps",scan.get_installed_applications())
    if response.text == "scanos":
        print("scanning os version")
        sendJsonData("scanos",scan.get_os_version())
 
    time.sleep(2)
        