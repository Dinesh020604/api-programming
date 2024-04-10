from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "city": "New York",
    "temperature": 22,
    "humidity": 60
}

@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

@app.route('/weather', methods=['POST'])
def update_weather():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    weather_data.update(data)
    return jsonify({"message": "Weather data updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
