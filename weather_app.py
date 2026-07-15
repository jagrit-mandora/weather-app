import requests

def get_location(city,country):
    url=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
    
    try:
        location_response=requests.get(url,timeout=10)
    except requests.exceptions.RequestException:
        print("Unable to connect...")
        return None,None

    status=location_response.status_code

    if status==200:
        print("retrieving location...")
    elif status!=200:
        print("Error retrieving data...")
        return(None,None)

    dictionary=(location_response.json())

    if results not in dictionary:
        print("City not found")
        return(None,None)

    results=(dictionary["results"])

        
    found=False

    for i in results:
        if i["country"].lower() == country.lower():
            list1=i
            found=True
            break

    if not found:
        print("country not found!!")
        return(None,None)

    latitude=list1["latitude"]

    longitude=list1["longitude"]

    return(latitude,longitude)

def get_weather(latitude,longitude,city,country):
    url=(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&"
     f"longitude={longitude}&current=temperature_2m,relative_humidity_2m,"
     "rain,precipitation,apparent_temperature,wind_speed_10m&forecast_days=1"
     "&timezone=auto")

    try:
        weather_response=requests.get(url,timeout=10)
    except requests.exceptions.RequestException:
        print("Unable to connect...")
        return

    status=weather_response.status_code
    
    if status==200:
        print("retrieving weather...")

    weather_dictionary=weather_response.json()
    current=(weather_dictionary["current"])
    #print(current.keys())
    time=current["time"]
    temperature=current["temperature_2m"]
    humidity=current["relative_humidity_2m"]
    rain=current["rain"]
    precipitation=current["precipitation"]
    apparent_temperature=current["apparent_temperature"]
    wind=current["wind_speed_10m"]
    print()
    print("=====================================")
    print("           WEATHER REPORT            ")
    print("=====================================")
    print()
    print(f"Location: {city}, {country}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print()
    print(f"time: {time}")
    print(f"temperature: {temperature} °C")
    print(f"humidity: {humidity} %")
    print(f"rain: {rain} mm")
    print(f"feels like temperature: {apparent_temperature} °C")
    print(f"wind speed: {wind} km/h")
   

def main():
        running=True
        while running:

            print()
            print("WEATHER APP")
            print("1. START")
            print("2. END")

            choice_1=input("ENTER choice:1 or 2: ")
            while choice_1 not in ["1","2"]:
                choice_1=input("ENTER choice:1 or 2: ")
            choice=int(choice_1)

            if choice==1:
                city=input("enter the city: ")

                country=input("enter the country: ")

                latitude,longitude=get_location(city,country)

                if latitude is None:
                    continue

                get_weather(latitude,longitude,city,country)

            if choice==2:
                 running=False


if __name__=="__main__":
    main()





