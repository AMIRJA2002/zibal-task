from mongoengine import connect

connect(
    db="zibal_db",
    host="mongodb://mongodb:27017/zibal_db",
)
