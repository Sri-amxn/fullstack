from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = [
    {"id": 1, "name": "Aman", "course": "React"},
    {"id": 2, "name": "Riya", "course": "Python"},
    {"id": 3, "name": "Rahul", "course": "SQL"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, port=5000)