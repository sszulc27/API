import requests

url = "https://dog.ceo/api/breeds/list/all"

resp = requests.get(url)
if resp.status_code != 200:
    # This means something went wrong.
    print("Error!")

for item in resp.json()['message'].keys():
    print(item)
    print(item)
