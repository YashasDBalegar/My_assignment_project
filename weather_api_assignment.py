import requests

# API URL for the OpenWeatherMap hourly forecast for London
API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve weather data.")
        return None

def get_weather_by_date(date):
    data = get_weather_data()
    if not data:
        return

    for forecast in data['list']:
        forecast_date = forecast['dt_txt'].split()[0]
        if forecast_date == date:
            return forecast['main']['temp'], forecast['weather'][0]['description']
    
    print(f"No weather data available for {date}.")
    return None, None

def get_wind_speed_by_date(date):
    data = get_weather_data()
    if not data:
        return

    for forecast in data['list']:
        forecast_date = forecast['dt_txt'].split()[0]
        if forecast_date == date:
            return forecast['wind']['speed']
    
    print(f"No weather data available for {date}.")
    return None

def get_pressure_by_date(date):
    data = get_weather_data()
    if not data:
        return

    for forecast in data['list']:
        forecast_date = forecast['dt_txt'].split()[0]
        if forecast_date == date:
            return forecast['main']['pressure']
    
    print(f"No weather data available for {date}.")
    return None

def main():
    data = get_weather_data()
    if not data:
        return

    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            temp, weather_description = get_weather_by_date(date)
            if temp is not None:
                print(f"Weather on {date}: {weather_description}, Temperature: {temp}°C")
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()