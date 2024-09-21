from flask import Flask, jsonify, request
from twilio.rest import Client
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms():
    account_sid = 'account_sid'
    auth_token = 'auth_token'
    client = Client(account_sid, auth_token)

    twilio_phone_number = '+18148084218'
    recipient_phone_number = request.form['r']
    message_body = request.form['m']

    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    return jsonify({"message": "SMS sent successfully", "sid": message.sid})


if __name__ == "__main__":
    app.run(debug=True)
