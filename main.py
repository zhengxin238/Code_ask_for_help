from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mycollection']

optimal_solution = {'status':1,'location':2}

collection.insert_one(optimal_solution)