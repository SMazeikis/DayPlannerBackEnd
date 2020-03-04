import requests


def distance_calculator(longitude1, latitude1, longitude2, latitude2):
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + latitude1 + "," + longitude1 + "&destinations=" + latitude2 + "%2C" + longitude2 + "&key=AIzaSyCj2T1Mdd-K7AtQh0SoO9-hWna1h8m-R_E")
    data = r.json()
    time = data["rows"][0]["elements"][0]["duration"]["text"]
    time = time.split()[0]
    return time

# print(distance_calculator("40.6655101", "-73.89188969999998", "40.6905615", "-73.9976592"))
# print(distance_calculator("53.3498", "6.2603","53.3373903","-6.239726"))