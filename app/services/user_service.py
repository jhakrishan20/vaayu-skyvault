# user services

from factory.clients.mongo_client import MongoDBClient
from factory.clients.s3_client import S3Client
from dotenv import load_dotenv
import os
load_dotenv()

class UserService:
    def __init__(self):
        self.mongo = MongoDBClient()
        self.s3 = S3Client()
    
    # A transaction/process, aborts if any sub-process fails
    def init_user(self, user_name, user_type, user_data):

        res = self._save_user(user_type, user_data)
        if res:
            res = self._create_user_db(user_name)
            if res:
                res = self._create_user_bucket(user_name)
                if res:
                    return True
                else:
                    return False  
            else:
               return False    
        else:
           return False
        
    def _save_user(self, user_type, user_data):
        # register the user in 'users-database' 
        return self.mongo.insert(os.getenv("USERS"), user_type, user_data) 
    
    def _create_user_db(self, db_name):
        # Create personallised database with collections
        return self.mongo.create_database(db_name)
        
    def _create_user_bucket(self, bucket_name):
        # crete s3 bucket
        return self.s3.create_bucket(bucket_name)

    # def init_user_workspace(self, user_id):
    #   pass