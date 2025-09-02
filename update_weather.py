#!/usr/bin/env python3
import os
import requests
import json
from datetime import datetime
import pytz

def get_weather_description(weather_code):
    """Convert Open-Meteo weather code to description and emoji"""
    weather_map = {
        0: ("Clear Sky", "☀️"),
        1: ("Mainly Clear", "🌤️"),
        2: ("Partly Cloudy", "⛅"),
        3: ("Overcast", "☁️"),
        45: ("Fog", "🌫️"),
        48: ("Depositing Rime Fog", "🌫️"),
        51: ("Light Drizzle", "🌦️"),
        53: ("Moderate Drizzle", "🌦️"),
        55: ("Dense Drizzle", "🌦️"),
        61: ("Slight Rain", "🌧️"),
        63: ("Moderate Rain", "🌧️"),
        65: ("Heavy Rain", "🌧️"),
        71: ("Slight Snow", "❄️"),
        73: ("Moderate Snow", "❄️"),
        75: ("Heavy Snow", "❄️"),
        77: ("Snow Grains", "❄️"),
        80: ("Slight Rain Showers", "🌦️"),
        81: ("Moderate Rain Showers", "🌧️"),
        82: ("Violent Rain Showers", "🌧️"),
        85: ("Slight Snow Showers", "❄️"),
        86: ("Heavy Snow Showers", "❄️"),
        95: ("Thunderstorm", "⛈️"),
        96: ("Thunderstorm with Hail", "⛈️"),
        99: ("Heavy Thunderstorm with Hail", "⛈️")
    }
    
    return weather_map.get(weather_code, ("Unknown", "🌤️"))

def get_seoul_weather():
    """Fetch current weather for Seoul using free Open-Meteo API"""
    # Seoul coordinates
    lat, lon = 37.5665, 126.9780
    
    try:
        # Open-Meteo API - completely free, no API key required
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=Asia%2FSeoul"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        current = data['current_weather']
        
        # Get Seoul timezone
        seoul_tz = pytz.timezone('Asia/Seoul')
        current_time = datetime.now(seoul_tz)
        
        # Convert weather code to description and emoji
        weather_code = current['weathercode']
        description, emoji = get_weather_description(weather_code)
        
        weather_info = {
            'temp': round(current['temperature']),
            'feels_like': round(current['temperature']),  # Open-Meteo doesn't provide feels_like
            'humidity': 0,  # Not available in current_weather endpoint
            'description': description,
            'weather_id': weather_code,
            'wind_speed': round(current['windspeed'], 1),
            'updated': current_time.strftime('%Y-%m-%d %H:%M KST')
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching weather data: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"❌ Error parsing weather data: {e}")
        return None

def update_readme(weather_info):
    """Update README.md with current weather information"""
    if not weather_info:
        print("❌ No weather data to update")
        return False
    
    try:
        # Read current README
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create weather section
        description, emoji = get_weather_description(weather_info['weather_id'])
        
        weather_section = f"""## 🌦️ Current Weather in Seoul

<div align="center">

| 🌡️ Temperature | 🌤️ Weather | 💨 Wind | 🌡️ Feels Like |
|:---:|:---:|:---:|:---:|
| **{weather_info['temp']}°C** | {emoji} {description} | {weather_info['wind_speed']} m/s | {weather_info['feels_like']}°C |

**Last updated:** {weather_info['updated']}

</div>

---
"""
        
        # Find and replace weather section
        start_marker = "## 🌦️ Current Weather in Seoul"
        end_marker = "---"
        
        start_idx = content.find(start_marker)
        if start_idx != -1:
            # Find the end of the weather section
            end_idx = content.find(end_marker, start_idx)
            if end_idx != -1:
                # Replace the entire weather section
                new_content = content[:start_idx] + weather_section + content[end_idx + len(end_marker):]
            else:
                # If no end marker, append after start marker
                new_content = content[:start_idx] + weather_section + content[start_idx + len(start_marker):]
        else:
            # If no weather section exists, add it at the beginning
            new_content = weather_section + "\n" + content
        
        # Write updated README
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ README.md updated successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error updating README: {e}")
        return False

if __name__ == "__main__":
    print("🌤️ Fetching Seoul weather data...")
    try:
        weather = get_seoul_weather()
        
        if weather:
            print(f"📍 Current weather: {weather['temp']}°C, {weather['description']}")
            success = update_readme(weather)
            if success:
                print("✅ Weather update completed successfully!")
            else:
                print("❌ Failed to update README")
                exit(1)
        else:
            print("❌ Failed to fetch weather data")
            exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        exit(1)
