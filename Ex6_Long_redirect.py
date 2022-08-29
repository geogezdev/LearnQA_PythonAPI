import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

response_histoty = response.history

count = 0
for i in response_histoty:
    count +=1
print(count)
#print(response_histoty)
#или так
#print(len(response.history))

print(response.url)