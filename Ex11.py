import pytest
import requests

# link = "https://playground.learnqa.ru/api/homework_cookie"
# response = requests.get(link).json()
# print(response)


link = "https://playground.learnqa.ru/api/homework_cookie"
response = requests.get(link)
print(response.cookies.get('HomeWork'))
cookies = response.cookies.get('HomeWork')


def test_cookie():
    assert cookies == "hw_value", f"Кука не равна значению 'hw_value'"


