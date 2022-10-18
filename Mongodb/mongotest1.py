import pymongo
client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# now we have to insert data
#here we are storing document based data
# like we are storing some thing in the form of dictionary or json format

#lest create a data

d = {
    "name":"Prikshit",
    "email" : "prikshit@gmail.com",

    "subject" : ["big data","full stack","data analytics"]
} # terms of mogodb it is document

# now creating data base
#data base is kind of a folder structure where you will able to store tables

database=client["myinfo"]
 # now we have to create collections ( collection of data)
 # colection is equivalent to a table
 # in sql there is tables
 # in mogodb it is collection
collection= database["sudh"] # here we are creating collection sudh inside database myinfo

 # now inside collection we are storing our data
collection.insert_one(d)


list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
