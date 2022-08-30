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
methods = ["get", "post", "put", "patch", "delete"]

for i in methods:
    if i == "get":
        print("параметр get")
        print(requests.get(link, params={"method":"GET"}).text, "get")
        print(requests.get(link, params={"method": "POST"}).text, "post")
        print(requests.get(link, params={"method": "PUT"}).text, "put")
        print(requests.get(link, params={"method": "DELETE"}).text, "delete")
        print(requests.get(link, params={"method": "OPTIONS"}).text, "options")
        print(requests.get(link, params={"method": "PATCH"}).text, "patch")
        print(requests.get(link, params={"method": "HEAD"}).text, "head")
    elif i == "post":
        print("параметр post")
        print(requests.post(link, data={"method": "GET"}).text, "get")
        print(requests.post(link, data={"method": "POST"}).text, "post")
        print(requests.post(link, data={"method": "PUT"}).text, "put")
        print(requests.post(link, data={"method": "DELETE"}).text, "delete")
        print(requests.post(link, data={"method": "OPTIONS"}).text, "options")
        print(requests.post(link, data={"method": "PATCH"}).text, "patch")
        print(requests.post(link, data={"method": "HEAD"}).text, "head")
    elif i == "put":
        print("параметр put")
        print(requests.put(link, data={"method": "GET"}).text, "get")
        print(requests.put(link, data={"method": "POST"}).text, "post")
        print(requests.put(link, data={"method": "PUT"}).text, "put")
        print(requests.put(link, data={"method": "DELETE"}).text, "delete")
        print(requests.put(link, data={"method": "OPTIONS"}).text, "options")
        print(requests.put(link, data={"method": "PATCH"}).text, "patch")
        print(requests.put(link, data={"method": "HEAD"}).text, "head")

    elif i == "delete":
        print("параметр delete")
        print(requests.delete(link, data={"method": "GET"}).text, "get")
        print(requests.delete(link, data={"method": "POST"}).text, "post")
        print(requests.delete(link, data={"method": "PUT"}).text, "put")
        print(requests.delete(link, data={"method": "DELETE"}).text, "delete")
        print(requests.delete(link, data={"method": "OPTIONS"}).text, "options")
        print(requests.delete(link, data={"method": "PATCH"}).text, "patch")
        print(requests.delete(link, data={"method": "HEAD"}).text, "head")
        #тип запроса delete не совпадает со значением параметра (get), но сервер отвечает так, словно все ок
    elif i == "patch":
        print("параметр patch")
        print(requests.patch(link, data={"method": "GET"}).text, "get")
        print(requests.patch(link, data={"method": "POST"}).text, "post")
        print(requests.patch(link, data={"method": "PUT"}).text, "put")
        print(requests.patch(link, data={"method": "DELETE"}).text, "delete")
        print(requests.patch(link, data={"method": "OPTIONS"}).text, "options")
        print(requests.patch(link, data={"method": "PATCH"}).text, "patch")
        #тип запроса patch совпадает со значением параметра (patch), но сервер отвечает выдает ошибку
        print(requests.patch(link, data={"method": "HEAD"}).text, "head")
