# Logic for pilots

from factory.clients.mongo_client import MongoDBClient
from factory.clients.s3_client import S3Client
from dotenv import load_dotenv
import os
load_dotenv()

class PilotService:
    def __init__(self):
        self.mongo = MongoDBClient()
        self.s3 = S3Client()
     
    def save_pilot_details(self, org_id, pilot_data):

        
        # register the pilot in their resp org db 
        return self.mongo.insert("resp_org", os.getenv("COLLECTION_PILOTS"), pilot_data)