import requests

url = "https://dog.ceo/api/breeds/list/all"

resp = requests.get(url)
if resp.status_code != 200:
    # This means something went wrong.
    print("Error!")

breed_list = resp.json()['message'].keys()

for dog in breed_list:
    print(dog)
