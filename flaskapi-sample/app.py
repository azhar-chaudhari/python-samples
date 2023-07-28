from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root endpoint
@app.route("/")
def hello():
    return "Hello, World!"

# Define a route for a custom endpoint
@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Define a route that returns JSON data
@app.route("/data")
def get_data():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    return jsonify(data)

if __name__ == "__main__":
    # Run the Flask application on localhost and port 5000
    app.run(debug=True)
