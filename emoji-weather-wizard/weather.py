# Create a dictionary of mock weather data
mock_weather_data = {
    "Pune": "sunny",
    "Tokyo": "rainy",
    "London": "cloudy",
    "NYC": "stormy",
    "Sydney": "snowy"
}

# Map weather conditions to emojis
weather_emojis = {
    "sunny": "☀️",
    "rainy": "🌧️",
    "cloudy": "☁️",
    "stormy": "⛈️",
    "snowy": "❄️"
}

# Function to get the weather emoji for a given city
def get_weather_emoji(city):
    try:
        weather_condition = mock_weather_data[city]
        return weather_emojis[weather_condition]
    except KeyError:
        return "Unknown city! Please provide a valid city name."