import pytest
import requests
link = "https://playground.learnqa.ru/api/homework_cookie"
print(requests.get(link).text)