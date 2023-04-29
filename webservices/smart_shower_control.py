from flask import jsonify, request


class smartShowerControl:
    def __init__(self):
        self.shower_data = {
            "room_id": 1,
            "desired_flow": 0,
            "desired_temperature": 0
        }

    def get_shower_data(self):
        return self.shower_data
    
    def update_shower_data(self, shower_data):
        self.shower_data = shower_data
        return self.shower_data
    
    def set_shower_settings(self, room_id, desired_flow, desired_temperature):
        self.shower_data['room_id'] = room_id
        self.shower_data['desired_flow'] = desired_flow
        self.shower_data['desired_temperature'] = desired_temperature
        return jsonify({"status": "success"})
    
    def get_shower_settings(self):
        return self.shower_data
    
    data = request.get_json()
    if data:
        room_id = data['room_id']
        desired_flow = data['desired_flow']
        desired_temperature = data['desired_temperature']
        set_shower_settings(room_id, desired_flow, desired_temperature)  # Função que ajusta o chuveiro inteligente
        