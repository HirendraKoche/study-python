import pymongo

db_url = 'mongodb+srv://hirendrakoche1:nCfLGcYH3NEswK4M@hkstudy.jq02hf0.mongodb.net/?retryWrites=true&w=majority&appName=HKStudy'

client = pymongo.MongoClient(db_url)

db = client['HKMongoDB']

query = {
    "city": "Stockholm",
    "age": {"$gt": 40}
}

for record in db.students.find(query, {"_id":0}):
    print(record)