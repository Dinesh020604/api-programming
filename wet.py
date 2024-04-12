from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '30d4741c779ba94c470ca1f63045390a'

def get_weather_data(city_name):
    try:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}")
        weather_data.raise_for_status()  
        return weather_data.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def get_user_location():
    try:
        ip_api_response = requests.get('https://ipapi.co/json/')
        ip_api_response.raise_for_status()
        user_location = ip_api_response.json()
        return user_location
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

@app.route('/')
def index():
    return render_template('index.html', weather=None, city=None, temp=None)

@app.route('/weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    user_location = get_user_location()

    if city_name:
        weather_data = get_weather_data(city_name)
    elif 'error' in user_location:
        return render_template('index.html', error=user_location['error'])
    else:
        user_city = user_location.get('city', 'Unknown')
        weather_data = get_weather_data(user_city)

    if 'error' in weather_data:
        return render_template('index.html', error=weather_data['error'])

    weather = weather_data['weather'][0]['main']
    temp = round(weather_data['main']['temp'])
    city = weather_data['name']

    return render_template('index.html', weather=weather, city=city, temp=temp)

if __name__ == '__main__':
    app.run(debug=True)
