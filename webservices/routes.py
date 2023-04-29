from flask import request, jsonify
from . import PresenceMonitor, ThermostatControl, SmartShowerControl, ProgrammableOutletControl

presence_monitor = PresenceMonitor()
thermostat_control = ThermostatControl()
smart_shower_control = SmartShowerControl()
programmable_outlet_control = ProgrammableOutletControl()
def init_app(app):
    @app.routes('/presence_monitor', methods=['GET', 'POST'])
    def presence_monitor_route():
        if request.method == 'GET':
            return jsonify(presence_monitor.get_presence_data())
        elif request.method == 'POST':
            presence_data = request.json
            presence_monitor.update_presence_data(presence_data)
            return jsonify({"message": "Presence data updated"}), 200

    @app.routes('/thermostat_control', methods=['GET', 'POST'])
    def thermostat_control_route():
        if request.method == 'GET':
            return jsonify(thermostat_control.get_temperature_data())
        elif request.method == 'POST':
            temperature_data = request.json
            thermostat_control.update_temperature_data(temperature_data)
            return jsonify({"message": "Temperature data updated"}), 200

    @app.routes('/smart_shower_control', methods=['GET', 'POST'])
    def smart_shower_control_route():
        if request.method == 'GET':
            return jsonify(smart_shower_control.get_shower_data())
        elif request.method == 'POST':
            shower_data = request.json
            smart_shower_control.update_shower_data(shower_data)
            return jsonify({"message": "Shower data updated"}), 200

    @app.routes('/programmable_outlet_control', methods=['GET', 'POST'])
    def programmable_outlet_control_route():
        if request.method == 'GET':
            return jsonify(programmable_outlet_control.get_outlet_data())
        elif request.method == 'POST':
            outlet_data = request.json
            programmable_outlet_control.update_outlet_data(outlet_data)
            return jsonify({"message": "Outlet data updated"}), 200