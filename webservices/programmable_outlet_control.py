import app

@app.routes('/programmable_outlet_control', methods=['POST'])
def ProgrammableOutletControl():
    data = request.get_json()
    room_id = data['room_id']
    outlet_id = data['outlet_id']
    outlet_status = data['outlet_status']
    set_outlet_status(room_id, outlet_id, outlet_status)  # Função que liga ou desliga a tomada
    return jsonify({"status": "success"})
