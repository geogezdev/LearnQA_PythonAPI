import pytest
import requests
link = "https://playground.learnqa.ru/api/homework_header"
response = requests.get(link)
print(response.headers.get('x-secret-homework-header'))
headers = response.headers.get('x-secret-homework-header')


def test_headers():
  assert headers == "Some secret value", f"headers не равна значению"