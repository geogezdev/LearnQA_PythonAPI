from json.decoder import JSONDecodeError
import requests

link = "https://playground.learnqa.ru/ajax/api/compare_query_type"


#1 - В случае вызова без requests без метода будет показана ошибка вызова запроса

try:
    response = requests(link)
    print(response)
except BaseException:
    print("Без метода response не работает")

#2 Код ответа сервера 400
response = requests.head(link)
print(f"пункт дз 2, {response}")

#3 Код ответа сервера 200
response = requests.get(link, params={"method":"GET"})
print(f"пункт дз 3, {response}")

#4
methods = ["get", "post", "put", "delete"]


for i in methods:
    if i == "get":
        print("параметр get")
        print(requests.get(link, params={"method":"GET"}).text)
        print(requests.get(link, params={"method": "POST"}).text)
        print(requests.get(link, params={"method": "PUT"}).text)
        print(requests.get(link, params={"method": "DELETE"}).text)
    elif i == "post":
        print("параметр post")
        print(requests.post(link, data={"method": "GET"}).text)
        print(requests.post(link, data={"method": "POST"}).text)
        print(requests.post(link, data={"method": "PUT"}).text)
        print(requests.post(link, data={"method": "DELETE"}).text)
    elif i == "put":
        print("параметр put")
        print(requests.put(link, data={"method": "GET"}).text)
        print(requests.put(link, data={"method": "POST"}).text)
        print(requests.put(link, data={"method": "PUT"}).text)
        print(requests.put(link, data={"method": "DELETE"}).text)
    elif i == "delete":
        print("параметр delete")
        print(requests.delete(link, data={"method": "GET"}).text)
        print(requests.delete(link, data={"method": "POST"}).text)
        print(requests.delete(link, data={"method": "PUT"}).text)
        print(requests.delete(link, data={"method": "DELETE"}).text)