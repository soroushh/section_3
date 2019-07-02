from flask import Flask, jsonify, request, render_template
from person import *

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
@app.route('/older', methods =["POST"])
def show_older_person():
    data = request.get_json()
    first_person = Person(data["name1"], data["age1"])
    second_person = Person(data["name2"], data["age2"])
    older_person = Person.older(first_person, second_person)
    return(jsonify({"older person name":older_person.name , "older person age":older_person.age }))













app.run(port = 5000)
