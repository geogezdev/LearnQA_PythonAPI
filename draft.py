# from json.decoder import JSONDecodeError
# import requests
#
# payload = {"name" : "User"}
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text["answer"])
# except:
#     print("Response is not a JSON format")

# import requests
#
# headers = {"some_headers":"123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
# print(response.text)
# print(response.headers)

import requests
payload = {"login" : "secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get("auth_cookie")
cookies = {'auth_cookie': cookie_value}
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)
print(response2.text)
# print(response.status_code)
# print(dict(response.cookies))
# print(response.headers)