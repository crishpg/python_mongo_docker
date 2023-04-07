import pymongo
from faker import Faker
   
   
# establishing connection
# to the database
client = pymongo.MongoClient("mongodb://172.17.0.2:27017/")
   
# Database name
db = client["meudb"]
   
# Collection name
col = db["tmp"]
 
# if we don't want to print id then pass _id:0
for x in col.find({}, {"coursename": 1}):
    print(x)