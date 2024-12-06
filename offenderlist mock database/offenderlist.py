from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Mock database
offenders = [
    {"id": 1, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 2, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 3, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 4, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 5, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 6, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 7, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 8, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 9, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 10, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 11, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 12, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 13, "day": "Monday", "date": "2024-01-01", "time": "10:00", "crime": "Theft", "images": ["https://via.placeholder.com/150"] * 10},
    {"id": 14, "day": "Tuesday", "date": "2024-01-02", "time": "11:00", "crime": "Assault", "images": ["https://via.placeholder.com/150"] * 10},
]

@app.route("/")
def homepage():
    return render_template("offenderlist.html")

@app.route("/api/offenders", methods=["GET"])
def get_offenders():
    return jsonify(offenders)

@app.route("/api/offenders/<int:id>", methods=["DELETE"])
def delete_offender(id):
    global offenders
    offenders = [offender for offender in offenders if offender["id"] != id]
    return jsonify({"message": "Offender deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
