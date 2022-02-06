from django.shortcuts import render
import requests
def home(request):
    city = request.GET.get('city', 'Visakhapatnam')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8021c8abadca8702b456adcfed474cfe'
    data = requests.get(url).json()
    payload = {
                'city' : data['name'], 
                'weather' : data['weather'][0]['main'], 
                'icon' : data['weather'][0]['icon'], 
                'kelvin_temperature' : int(data['main']['temp']), 
                'celcius_temperature' : int(data['main']['temp']-273), 
                'pressure' : data['main']['pressure'], 
                'humidity' : data['main']['humidity'],
                'description' : data['weather'][0]['description']
            }
    context = {'data' : payload}
    print(context)
    return render(request, 'home.html', context)