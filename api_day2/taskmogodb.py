from flask import Flask,request, jsonify
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client["api_day2"]
collection = database["ineuron"]
@app.route("/insert/mongo",methods=["GET", "POST"])
def insert():
    if  (request.method=="POST"):
        name= request.json["name"]
        number=request.json["number"]
        collection.insert_one({name:number})
        return jsonify(str("done"))



if __name__=='__main__':

    app.run(port=8000)