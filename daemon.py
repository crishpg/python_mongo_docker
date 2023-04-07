import pymongo
from faker import Faker
faker = Faker()
   
   
# establishing connection
# to the database
client = pymongo.MongoClient("mongodb://172.17.0.2:27017/")
   
# Database name
#db = client["meudb"]
   
# Collection name
#col = db["tmp"]

db = client["meudb"]
mycol = db["customers"]

#for i in range(10):
mydict = { "name": faker.name(), "address": faker.address(),"job":faker.job(),"phone_numer":faker.phone_number(),"profile":faker.simple_profile()}
x = mycol.insert_one(mydict)
 
# if we don't want to print id then pass _id:0
for x in mycol.find({}, {"name": 1}):
    print(x)