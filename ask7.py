
import urllib
import json

#coords for the place that the user wants to see
lat = raw_input("x ")
lon = raw_input("y ")

# Search for current weather in coords that the user gives
url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=a7f701d058a48460fe51269e28888592"%(lon, lat)
#Open the url to get data from OpenWeathermap
Response = urllib.urlopen(url)

data = json.loads(Response.read())
for item in data["weather"]:
    if item["main"] == "Rain":
        print "I'm singing in the rain!"

t = data["main"]["temp"]
#convert temperature from kelvin to celsius
k = 273.15
tempCelsius = t - k

if tempCelsius > 20:
    print "nice..."
elif tempCelsius < 5:
        print "brrrr"
