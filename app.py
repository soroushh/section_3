from flask import Flask, request, jsonify
import json

app = Flask(__name__)

stores = []

# GET '/store/<string:name>'
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores :
        if store["name"]== name:
            return(jsonify(store))
    return(jsonify({"message":"store not found!"}))

#POST '/store' data {"name"}
@app.route('/store', methods=["POST"])
def create_store():
    data = request.get_json()
    stores.append({"name":data["name"], "items":[]})
    return(jsonify({"message":"store is created"}))

# GET '/store/<string:name>/item/<string:item_name>'
@app.route('/store/<string:name>/item/<string:item_name>')
def get_item_in_store(name, item_name):
    for store in stores:
        if store["name"]== name:
            for item in store["items"]:
                if item["name"] == item_name:
                    return(jsonify(item))
    return(jsonify({"message":"Item or store not found"}))
# POST '/store/<string:name>/item' data {"name", "price"}
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    data = request.get_json()
    for store in stores :
        if store["name"] == name:
            store["items"].append({"name": data["name"], "price": data["price"]})
            return(jsonify({"message":"item added"}))
    return(jsonify({"message":"store not found"}))
#  GET '/stores'
@app.route('/stores')
def show_stores():
    return(jsonify({"stores":stores}))

app.run(port = 5000)
