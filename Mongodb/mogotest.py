import pymongo
client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@prince.todietu.mongodb.net/?retryWrites=true&w=majority")
# creating communication between mogodb and python
db = client.test # calling the connection

# we we are able to connect with the particular cluster
print(db)

# dumping some sort of record
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )