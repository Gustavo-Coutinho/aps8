class PresenceMonitor:
        
def PresenceMonitor():
    data = request.get_json()
    room_id = data['room_id']
    presence_status = detect_presence(room_id)  # Função que se comunica com o sensor de presença
    return jsonify({"presence_status": presence_status})

