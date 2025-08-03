import requests
from django.shortcuts import render

def index(request):
    weather_data = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'your api key'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            print(response.status_code)
            data = response.json()
            print(data)

            weather_data = {
                'city': data['name'],  # actual city name with correct capitalization
                'country': data['sys']['country'],  # country code like 'IN'
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),  # capitalize each word
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] = "City not found."

    return render(request, 'weather/index.html', {'weather_data': weather_data})
