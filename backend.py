import requests

API_KEY="dac88ba6dbad3f45769efae44b8d7755"
def get_data(place,days):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    req = requests.get(url)
    data = req.json()
    filtered_data = data['list'] #list of dictionaries
    nr_results = 8*days #obs done every 3 hours , so 8 times in a day
    filtered_data = filtered_data[0:nr_results]


    return filtered_data

if __name__ == "__main__":
    x=get_data("Dhaka",days=3)
    print(x)
    print(len(x))