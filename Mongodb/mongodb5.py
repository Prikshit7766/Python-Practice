# extracting data from monfodb

import pymongo
client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database=client["myinfo"]
collection1= database["sudh"]
collection2= database["dpkt"]

record1=collection1.find()
record2=collection2.find()


# to fetch all the record
for i in record1:

    print(i)

'''for i in record2:
    print(i)

'''

# to see record in formatted way

# find those record  where we have company name or where ever we have product

# how ----> to do that we have to fire queries

print("-----------------------------------------------")

data= collection1.find({"companyName":"iNeuron"})
for i in data:
    print(i)

print("-----------------------------------------------")
data= collection1.find({"packetType": "D"})
for i in data:
    print(i)

print("-----------------------------------------------")
data=collection1.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)
    
