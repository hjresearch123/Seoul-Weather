# 🌤️ Seoul Weather Tracker

<div align="center">

![Seoul Skyline](https://img.shields.io/badge/Seoul-Weather%20Tracker-blue?style=for-the-badge&logo=github)
![Auto Update](https://img.shields.io/badge/Auto%20Update-Every%20Hour-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Enabled-orange?style=for-the-badge&logo=github-actions)

*A beautiful GitHub profile README that automatically updates with Seoul's current weather every hour!*

</div>

---

## 🌦️ Current Weather in Seoul

<div align="center">

| 🌡️ Temperature | 🌤️ Weather | 💨 Wind | 🌡️ Feels Like |
|:---:|:---:|:---:|:---:|
| **Loading...** | 🌤️ Fetching... | Loading... | Loading... |

**Last updated:** Loading...

</div>

---

## 🚀 Features

- ⏰ **Auto-updates every hour** using GitHub Actions
- 🌍 **Real-time weather data** from Open-Meteo API (100% free!)
- 🎨 **Beautiful emoji-based weather display**
- 📱 **Responsive design** that looks great on all devices
- 🔄 **Automatic commits** with weather updates
- 🛡️ **Error handling** for API failures

## 🛠️ Setup Instructions

### 1. No API Key Required! 🎉
This project uses the completely free [Open-Meteo API](https://open-meteo.com/) - no registration or API key needed!

### 2. Enable GitHub Actions
The workflow will automatically run every hour. You can also trigger it manually from the **Actions** tab.

## 📁 Project Structure

```
Seoul-Weather/
├── .github/
│   └── workflows/
│       └── weather-update.yml    # GitHub Actions workflow
├── update_weather.py             # Python script for weather updates
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## 🔧 How It Works

1. **GitHub Actions** triggers every hour (`0 * * * *`)
2. **Python script** fetches weather data from Open-Meteo API (free!)
3. **README.md** gets updated with current weather information
4. **Changes are committed** and pushed back to the repository
5. **Your profile** shows the latest Seoul weather! 🌤️

## 🌟 Customization

You can easily customize this for any city by:
- Changing the coordinates in `update_weather.py`
- Modifying the emoji mappings
- Adjusting the update frequency in the workflow
- Customizing the README layout

## 📊 Weather Data Includes

- 🌡️ Current temperature
- 🌤️ Weather conditions with emojis
- 💨 Wind speed
- 🌡️ "Feels like" temperature
- ⏰ Last update timestamp (KST)

---

<div align="center">

**Made with ❤️ for Seoul weather enthusiasts**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com)
[![Open-Meteo](https://img.shields.io/badge/Weather%20Data-Open--Meteo%20(Free!)-green?style=for-the-badge)](https://open-meteo.com/)

</div>
