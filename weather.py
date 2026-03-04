import requests

print("Weather App")

city = input("Enter city name: ")

try:
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=10)

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)

except:
    print("Could not fetch weather. Check your internet.")