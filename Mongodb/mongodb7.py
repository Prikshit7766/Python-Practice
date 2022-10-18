# extracting data from monfodb

import pymongo
client = pymongo.MongoClient("mongodb+srv://Prikshit7766:prikshit@cluster0.bb7u7jb.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client["inventory"]

collection=database["table"]


record=collection.find()
for i in record:
    print(i)

print("-----------------------------------------------")

#loking for those data where status will be  A

record=collection.find({"status":"A"})
for i in record:
    print(i)

#loking for those data where status will be  A or P
# always remember you wirte $ when you are writing condion
# what ever start with $ then it will be a inbuild keyword
record=collection.find({"status":{'$in':['A','P']}})
for i in record:
    print(i)

print("-----------------------------------------------")


#loking for those data where status greater than P

record=collection.find({"status":{'$gt':"C"}})
for i in record:
    print(i)

print("-----------------------------------------------")


# filter out those record where quantity is greater than equal to 100
record=collection.find({"qty":{'$gte': 100}})
for i in record:
    print(i)

print("-----------------------------------------------")


# filter out those record where quantity is greater than  equal to 100
record=collection.find({"qty":{'$gte': 75}})
for i in record:
    print(i)

print("-----------------------------------------------")

# filter out those record where quantity is equal to 95 and item = sketc pad

record=collection.find({"item":"sketch pad","qty":95})
for i in record:
    print(i)

print("-----------------------------------------------")

# filter out those record where quantity is greater than equal to 75 and item = sketc pad

record=collection.find({"item":"sketch pad","qty":{"$gte":75}})
for i in record:
    print(i)

print("-----------------------------------------------")


# filter out those record where quantity is greater than equal to 100 or item = sketc pad  by using $or

record=collection.find({"$or":[{"item":"sketch pad"},{"qty":{"$gte":100}}]})
for i in record:
    print(i)

print("-----------------------------------------------")



#update operation where we have item = canvas to item= sudhanshu

collection.update_one({"item":"canvas"},{"$set":{"item":"sudhanshu"}})
record=collection.find()
for i in record:
    print(i)

print("-----------------------------------------------")


collection.update_one({"item":"canvas"},{"$set":{"item":"sudhanshu"}})
record=collection.find({"item":"sudhanshu"})
for i in record:
    print(i)

print("-----------------------------------------------")

# deletion operation
collection.delete_one({"item":"sudhanshu"})
record=collection.find({"item":"sudhanshu"})
for i in record:
    print(i)

print("-----------------------------------------------")