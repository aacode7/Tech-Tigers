
"""import pymongo
from gridfs import GridFS

# Replace with your MongoDB connection URI
mongo_uri = "mongodb://my-mongodb-container:27017/"

# Replace 'your_database' with the name of your database
database_name = "your_database"

# Replace 'image.jpg' with the path to the image file you want to store
image_file_path = "image.jpg"

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[database_name]

    # Initialize GridFS
    fs = GridFS(db)

    # Open and store the image in GridFS
    with open(image_file_path, "rb") as image_file:
        fs.put(image_file, filename="image.jpg")

    print("Image stored in MongoDB GridFS")

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Close the MongoDB connection when done
    client.close()
"""
