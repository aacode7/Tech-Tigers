from pymongo import MongoClient
from gridfs import GridFS

# Replace "<mongodb_host_ip>" with the actual IP address "10.32.44.84"
connection_url = "mongodb://10.32.44.84:27017/"

# Create a MongoClient and connect to the remote MongoDB server
client = MongoClient(connection_url)

# Replace 'test' with the name of your database (which is "test" in this case)
database_name = "test"

# Replace 'image.jpg' with the path to the image file you want to store
image_file_path = "rail.jpg"

try:
    # Access the desired database
    db = client[database_name]

    # Initialize GridFS
    fs = GridFS(db)

    # Open and store the image in GridFS
    with open(image_file_path, "rb") as image_file:
        fs.put(image_file, filename="rail.jpg")

    print("Image stored in MongoDB GridFS")

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Close the MongoDB connection when done
    client.close()