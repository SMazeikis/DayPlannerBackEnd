import requests


def distance_calculator(lo1, la1, lo2, la2):
    longitude1 = lo1
    latitude1 = la1
    longitude2 = lo2
    latitude2 = la2
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + longitude1 + "," + latitude1 + "&destinations=" + longitude2 + "%2C" + latitude2 + "&key=AIzaSyCj2T1Mdd-K7AtQh0SoO9-hWna1h8m-R_E")
    # response = requests.get(url=endpoint)
    data = r.json()
    time = data["rows"][0]["elements"][0]["duration"]["text"]
    return time

print(distance_calculator("40.6655101", "-73.89188969999998", "40.6905615", "-73.9976592"))