from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '30d4741c779ba94c470ca1f63045390a'

@app.route('/')
def index():
    return render_template('index.html', weather=None, city=None, temp=None)

@app.route('/weather', methods=['GET'])
def get_weather():
    user_input = request.args.get('city')

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        return render_template('index.html', weather=None, city=None, temp=None)
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        return render_template('index.html', weather=weather, city=user_input, temp=temp)

if __name__ == '__main__':
    app.run(debug=True)
