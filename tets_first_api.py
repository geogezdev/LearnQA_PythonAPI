import requests

class testFirstAPI:
    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/api/hello'
        name = 'Vitalii'
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"


        response_dict = response.json()
        assert "answer" response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
