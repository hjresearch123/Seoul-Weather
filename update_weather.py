#!/usr/bin/env python3
import requests
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
    print("🌤️ Fetching weather data from Open-Meteo API...")
    
    try:
        # Seoul coordinates
        lat, lon = 37.5665, 126.9780
        
        # Open-Meteo API - completely free, no API key required
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=Asia%2FSeoul"
        print(f"📡 API URL: {url}")
        
        response = requests.get(url, timeout=30)
        print(f"📊 Response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ API returned status {response.status_code}")
            return None
            
        data = response.json()
        print(f"📋 API Response: {data}")
        
        if 'current_weather' not in data:
            print("❌ No current_weather data in API response")
            return None
            
        current = data['current_weather']
        
        # Get Seoul timezone
        seoul_tz = pytz.timezone('Asia/Seoul')
        current_time = datetime.now(seoul_tz)
        
        # Convert weather code to description and emoji
        weather_code = current.get('weathercode', 0)
        description, emoji = get_weather_description(weather_code)
        
        weather_info = {
            'temp': round(current.get('temperature', 0)),
            'feels_like': round(current.get('temperature', 0)),
            'description': description,
            'weather_id': weather_code,
            'wind_speed': round(current.get('windspeed', 0), 1),
            'updated': current_time.strftime('%Y-%m-%d %H:%M KST')
        }
        
        print(f"✅ Weather data parsed successfully: {weather_info}")
        return weather_info
        
    except Exception as e:
        print(f"❌ Error in get_seoul_weather: {e}")
        import traceback
        traceback.print_exc()
        return None

def update_readme(weather_info):
    """Update README.md with current weather information"""
    print("📝 Updating README.md...")
    
    if not weather_info:
        print("❌ No weather data to update")
        return False
    
    try:
        # Read current README
        print("📖 Reading README.md...")
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
        
        print("🔍 Looking for weather section in README...")
        
        # Find and replace weather section
        start_marker = "## 🌦️ Current Weather in Seoul"
        end_marker = "---"
        
        start_idx = content.find(start_marker)
        print(f"📍 Found start marker at index: {start_idx}")
        
        if start_idx != -1:
            # Find the end of the weather section
            end_idx = content.find(end_marker, start_idx)
            print(f"📍 Found end marker at index: {end_idx}")
            
            if end_idx != -1:
                # Replace the entire weather section
                new_content = content[:start_idx] + weather_section + content[end_idx + len(end_marker):]
                print("✅ Replaced existing weather section")
            else:
                # If no end marker, append after start marker
                new_content = content[:start_idx] + weather_section + content[start_idx + len(start_marker):]
                print("✅ Appended to existing weather section")
        else:
            # If no weather section exists, add it at the beginning
            new_content = weather_section + "\n" + content
            print("✅ Added new weather section at beginning")
        
        # Write updated README
        print("💾 Writing updated README.md...")
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ README.md updated successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error updating README: {e}")
        import traceback
        traceback.print_exc()
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
