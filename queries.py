import pymongo

# Start connections
conn = pymongo.MongoClient('localhost', 27017)
db = conn['book_list']
collection = db['book_info']

# Find the document that contain the following title
query1 = collection.find({"title": "Libertarianism for Beginners"})
print('\nHere is the information for the book with the title you are looking for:')
for x in query1:
    print(x)


# Find the title and url using the keyword contained in the title
query2 = collection.find({"title": {"$regex": "Fire"}}, {"title": 1, "url": 1})
print('\nHere is the information for the books with the title that contains the keywords you are looking for:')
for x in query2:
    print(x)


# Find the books whose price are lower than £20
query3 = collection.find({"price": {"$lt":"£20"}}, {"title": 1, "price": 1, "url": 1})
print('\nHere is the information for the books whose price are lower than £20:')
for x in query3:
    print(x)


# Find the number of books whose price are lower than £20
query4 = collection.count_documents({"price": {"$lt":"£20"}})
print('\nThe number of books whose price are lower than £20 is:')
print(query4)
