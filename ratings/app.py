from flask import Flask, jsonify

app = Flask(__name__)

# List of musical instrument types
instrument_types = [
    "String instruments",
    "Woodwind instruments",
    "Brass instruments",
    "Percussion instruments",
    "Keyboard instruments",
    "Electronic instruments"
]

@app.route('/instruments/types', methods=['GET'])
def get_instrument_types():
    return jsonify(instrument_types)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

