from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

people = []

@app.route('/person', methods=["POST"])
def create_person():
    data = request.get_json()
    people.append({"name":data["name"], "family":data["family"], "properties":[]})
    return(jsonify({"message":"Person is created"}))

@app.route('/persons')
def all_people():
    return jsonify({"people":people})

@app.route('/person/<string:name>/property', methods=["POST"])
def add_property(name):
    data = request.get_json()
    for person in people:
        if person["name"] == name:
            person["properties"].append({"name":data["name"], "price": data["price"]})
            return(jsonify({"message": "property added to person"}))
    return(jsonify({"message":"person was not found"}))













app.run(port = 5000)
