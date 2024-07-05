from pymongo import MongoClient
from bson import ObjectId
 
client = MongoClient("mongodb_URI", tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube manager app")
        print("1. List video")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter your choice")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video_id name: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video_id name: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
