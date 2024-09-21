from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docker', methods=["POST"])
def run_docker_command():
    command = request.form.get('command')  # Get the command from the form data
    
    if not command:  # Check if the command is empty
        return "No command provided", 400
    
    # Execute the command and get the output
    output = subprocess.getoutput(command)
    
    return output  # Return the output as plain text

if __name__ == '__main__':
    app.run(debug=True)
