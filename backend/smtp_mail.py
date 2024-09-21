from flask import Flask, request, render_template_string
import smtplib

app = Flask(__name__)

@app.route ("/mail", methods=["POST"]["GET"])
def email():
    email = "sharma.harshita9104@gmail.com"
    receiver_email = request.form['r']
    subject = request.form['s']
    message = request.form['m']

    text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, "your password")
        server.sendmail(email, receiver_email, text)
        server.quit()
        return render_template_string(success_page)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run()

# HTML page for the success response
success_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Sent</title>
    <style>
        /* Background styling */
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        /* Success message container */
        .container {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            text-align: center;
            animation: fadeInUp 1.5s ease-out, float 3s ease-in-out infinite;
            max-width: 400px;
            width: 100%;
        }

        /* Fade-in animation */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Float animation */
        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        /* Text styling */
        h2 {
            color: #333;
            font-size: 28px;
            font-weight: bold;
            animation: colorChange 3s infinite;
        }

        /* Text color change animation */
        @keyframes colorChange {
            0% {
                color: #333;
            }
            50% {
                color: #9face6;
            }
            100% {
                color: #333;
            }
        }

        /* Responsive design for smaller screens */
        @media (max-width: 480px) {
            .container {
                padding: 30px;
            }

            h2 {
                font-size: 24px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Email Sent Successfully!</h2>
    </div>
</body>
</html>
"""
