import requests
import time

link = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(link)
print(response.text)
obj = response.json()
seconds = (obj["seconds"])
token = (obj["token"])
time.sleep(seconds)
response2 = requests.get(link, params={"token": token})
print(response2.text)