from flask import jsonify, request
class ThermostatControl:
    def __init__(self):
        self.temperature_data = {}
    
     # Função que ajusta a temperatura do termostato:
    def set_temperature(data):
        data = request.get_json()
        room_id = data['room_id']
        desired_temperature = data['desired_temperature']
        return jsonify({"status": "success"})
    
    def get_temperature_data(self):
        return self.temperature_data