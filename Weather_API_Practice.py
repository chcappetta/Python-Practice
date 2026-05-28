import requests


def get_grid(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "results" not in data:
        print("City not found")
        return None

    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]

    return lat, lon

def get_weather(lat,lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "current_weather":True
        }
    response=requests.get(url,params=params)
    data=response.json()
    print(data)
    print("temperature (Celsius): ",data["current_weather"]["temperature"])
    return


def main():
    city = input("City: ")
    lat,lon=get_grid(city)
    get_weather(lat,lon)
    
main()
