from flask import Flask, request, jsonify
from googlesearch import search  # Ensure this is correctly installed

app = Flask(__name__)

@app.route("/google_search", methods=['POST'])
def google_search():
    try:
        # Get the search query from the form data
        query = request.form['q']
        
        # Perform the search and store the top 5 results
        results = []
        for j in search(query,num_results=10):
            results.append(j)
        
        # Return the search results as a JSON response
        return jsonify(results)
    
    except Exception as e:
        # Log the error and return a 500 response with error details
        return jsonify({"error": str(e)}), 500


app.run(port=5000)