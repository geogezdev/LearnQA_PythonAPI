from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest


class TestUserRegister(BaseCase):
    exclude_params = [
        'password',
        'username',
        'firstName',
        'lastName',
        'email',
    ]

    def test_create_user_successfully(self):
        data = self.prepare_registration_date()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'

        data = self.prepare_registration_date(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    # Ex15
    def test_create_user_with_not_correct_email(self):
        email = 'vinkotovexample.com'

        data = self.prepare_registration_date(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_with_no_one_parameter(self, condition):
        data = self.prepare_registration_date()
        del data[condition]
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        data = self.prepare_registration_date()
        data['username'] = "a"
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        data = self.prepare_registration_date()
        data['username'] = "a" * 255
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"
