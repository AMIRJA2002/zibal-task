from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

connect(
    db=os.getenv('MONGODB_NAME'),
    host=os.getenv('MONGODB_URL')
)
