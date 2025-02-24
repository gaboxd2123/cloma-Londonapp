import requests
import csv
import os
from datetime import datetime

# Parámetros de la API y ubicación
API_KEY = '3dc4ae0d3bba7fc7163c2ef535777140'
LONDON_LAT = 51.5074
LONDON_LONGITUDE = -0.1278

def get_weather(lat, lon, api):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric'
    response = requests.get(url)
    return response.json()

def process(weather_data):
    # Procesa el JSON para extraer todos los campos relevantes
    processed_data = {
        'timestamp': datetime.now().isoformat(),
        'latitude': weather_data['coord']['lat'],
        'longitude': weather_data['coord']['lon'],
        'weather_id': weather_data['weather'][0]['id'],
        'weather_main': weather_data['weather'][0]['main'],
        'weather_description': weather_data['weather'][0]['description'],
        'weather_icon': weather_data['weather'][0]['icon'],
        'base': weather_data['base'],
        'temp': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
        'temp_min': weather_data['main']['temp_min'],
        'temp_max': weather_data['main']['temp_max'],
        'pressure': weather_data['main']['pressure'],
        'humidity': weather_data['main']['humidity'],
        'sea_level': weather_data['main'].get('sea_level', ''),
        'grnd_level': weather_data['main'].get('grnd_level', ''),
        'visibility': weather_data.get('visibility', ''),
        'wind_speed': weather_data['wind']['speed'],
        'wind_deg': weather_data['wind']['deg'],
        'wind_gust': weather_data['wind'].get('gust', ''),
        'clouds_all': weather_data['clouds']['all'],
        'dt': weather_data['dt'],
        'sys_type': weather_data['sys'].get('type', ''),
        'sys_id': weather_data['sys'].get('id', ''),
        'country': weather_data['sys']['country'],
        'sunrise': weather_data['sys']['sunrise'],
        'sunset': weather_data['sys']['sunset'],
        'timezone': weather_data['timezone'],
        'city_id': weather_data['id'],
        'city_name': weather_data['name'],
        'cod': weather_data['cod']
    }
    return processed_data

def write2csv(data, filename='clima-london-hoy.csv'):
    # Campos en el CSV
    fieldnames = data.keys()

    # Escribe los datos en el archivo CSV
    with open(filename, mode='a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()  # Escribe la cabecera si el archivo está vacío
        writer.writerow(data)

def main():
    print("===== Bienvenido a Londres-Clima =====")
    london_weather = get_weather(lat=LONDON_LAT, lon=LONDON_LONGITUDE, api=API_KEY)
    if london_weather['cod'] != 404:
        weather_data = process(london_weather)
        write2csv(weather_data)
        print(f"{weather_data['timestamp']}")
    else:
        print("Ciudad no disponible o API KEY no válida")

if __name__ == '__main__':
    main()
