import flask
from flask import Flask,request
app=Flask(_name_)
import subprocess

@app.route('/dockerps',methods=["POST","GET"])
def docker_run():

    command="sudo " + request.args.get('n')
    output=subprocess.getoutput(command)

    return f"<pre>{output}</pre>"
app.run(host='0.0.0.0')