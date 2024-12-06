import firebase_admin
from firebase_admin import credentials, db
import flask
from flask import Flask, jsonify, request, render_template

# Initialize Firebase
cred = credentials.Certificate("my friend said write path/to/your/firebase-service-account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com'
})

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("offenderlistV2.html")

@app.route("/api/offenders", methods=["GET"])
def get_offenders():
    return jsonify(offenders)

@app.route("/api/offenders/<int:id>", methods=["DELETE"])
def delete_offender(id):
    ref = db.reference(f"offenders/{id}")
    if ref.get():
        ref.delete()
        return jsonify({"message": "Offender deleted successfully"}), 200
    return jsonify({"message": "Offender not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
