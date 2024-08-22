import requests

WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5'
WEATHER_API_KEY = '0b8d09a948a2c1cea572edac718ac320'
GEO_API_URL = 'https://wft-geo-db.p.rapidapi.com/v1/geo'
GEO_API_KEY = '4f0dcce84bmshac9e329bd55fd14p17ec6fjsnff18c2e61917'

GEO_API_HEADERS = {
    'X-RapidAPI-Key': GEO_API_KEY,
    'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com',
}

def fetch_weather_data(lat, lon):
    try:
        weather_url = f"{WEATHER_API_URL}/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        forecast_url = f"{WEATHER_API_URL}/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"

        weather_response = requests.get(weather_url)
        forecast_response = requests.get(forecast_url)

        weather_response.raise_for_status()
        forecast_response.raise_for_status()

        weather_data = weather_response.json()
        forecast_data = forecast_response.json()
        
        return weather_data, forecast_data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None, None

def fetch_cities(input):
    try:
        cities_url = f"{GEO_API_URL}/cities?minPopulation=10000&namePrefix={input}"

        response = requests.get(cities_url, headers=GEO_API_HEADERS)

        response.raise_for_status()

        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching cities data: {e}")
        return None

def main():
    while True:
        print("type 'end' to terminate")
        city_name = input("Enter the name of the city:").strip()
        
        if city_name.lower() == 'end':
            print("Terminating the program.")
            break

        city_data = fetch_cities(city_name)
        
        if city_data and 'data' in city_data and len(city_data['data']) > 0:

            city = city_data['data'][0]
            lat = city['latitude']
            lon = city['longitude']
            city_name = city['name']

            weather, forecast = fetch_weather_data(lat, lon)
            
            if weather and forecast:
                print(f"Weather in {city_name}:")
                print(f"Temperature: {weather['main']['temp']}°C")
                print(f"Condition: {weather['weather'][0]['description'].capitalize()}")
            else:
                print("Failed to fetch weather data.")
        else:
            print("City not found or no data available.")

if __name__ == "__main__":
    main()
