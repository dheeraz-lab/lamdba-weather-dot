import os
import requests

def lambda_handler(event, context):
    city = os.getenv("CITY", "New York")
    api_key = os.getenv("API_KEY")
    if not api_key:
        return {"error": "API Key not found"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch weather data", "details": response.text}

    data = response.json()
    temperature = data.get('main', {}).get('temp')

    print(f"Current temperature in {city}: {temperature}°C")
    return {
        "city": city,
        "temperature": temperature
    }
