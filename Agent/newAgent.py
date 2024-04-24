import requests, re, time

PORT = 12345
run = True

# connect to the controller
print("Entrez l'ip et port du contrôleur :") 
ControllerIP = input("IP -> ")
ControllerPort = input("Port -> ")
print("Entrez le nom du nouvel agent :")
AgentName = input("Nom -> ")
ControllerUrl = "http://"+ControllerIP+":"+ControllerPort
# send the request
response = requests.get(ControllerUrl+"/enroll/"+AgentName)
if response.status_code == 200 :
	print("Connexion avec le contrôleur établie")
else :
	print("Echec de la connexion")

# ask the controller for instructions every 2 seconds
while run == True :
    response = requests.get(ControllerUrl+"/instruction/"+AgentName)
    if response.text == "quit":
        print("fin du programme")
        run = False
    if response.text == "whoami":
        # appeler le script 
        # renvoyer le résultat au controleur
        requests.post(ControllerUrl+"/")
    if response.text == "list directories":
        # appeler le script 
        # renvoyer le résultat au controleur
        requests.post(ControllerUrl+"/")
    if response.text == "drop file ":
        # appeler le script 
        # renvoyer le résultat au controleur 
        requests.post(ControllerUrl+"/")
    time.sleep(2)
        