from flask import request, jsonify
from services import UserService, PilotService, VehicleService, MissionService
from models import User_Schema, Mission_Schema, Pilot_Schema, Vehicle_Schema

class Route_Controller:
    def __init__(self):
        self.user_service = UserService()
        self.pilot_service = PilotService()
        self.vehilce_service = VehicleService()
        self.mission_service = MissionService()

        # init them in resp mehtods
        # self.user_schema = User_Schema()
        # self.pilot_schema = Pilot_Schema()
        # self.vehilce_schema = Vehicle_Schema()
        # self.mission_schema = Mission_Schema()

    def register_user(self):

        data = request.get_json()

        user_schema = User_Schema(data)
        user_data = user_schema.to_dict()
        user_type = user_schema.user_type  
        user_name = user_schema.user_name   

        # register user and trigger DB, collections, bucket creation
        res = self.user_service.init_user(user_name, user_type, user_data)
        if res:
           return jsonify({'status': 'success', 'message':'user registered successfully'}), 201
        else:
           return jsonify({'status': 'error', 'message': 'an error occured, process aborted'}), 400
        
    def register_pilot(self):
        data = request.get_json()
        org_id = data.get_json('org_id') # expects organisation (user id) for CRUD in resp org DB
        pilot_data = data.get('pilot_data')

        # register pilot in their resp org
        res = self.pilot_service.save_pilot_details(org_id, pilot_data)
        if res:
           return jsonify({'status': 'success', 'message':'pilot registered successfully'}), 201
        else:
           return jsonify({'status': 'error', 'message': 'an error occured, process aborted'}), 400

        # register pilot  

    def get_user(self, user_id):
        ...

    def update_user(self, user_id):
        ...

    def list_users(self):
        ...

    def delete_user(self, user_id):
        ...
