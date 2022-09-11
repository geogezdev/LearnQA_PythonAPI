from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure

# ex18
@allure.epic("User deletion cases")
class TestUserDelete(BaseCase):
  @allure.tag("User deletion")
  @allure.suite("Negative cases")
  @allure.description("This test unsuccessfully delete default user with id 2")
  def test_delete_user_id2(self):
    data = {
    'email': 'vinkotov@example.com',
    'password': '1234'
    }
    
    response1 = MyRequests.post("/user/login", data=data)

    Assertions.assert_code_status(response1, 200)

    auth_sid = self.get_cookie(response1, "auth_sid")
    token = self.get_header(response1, "x-csrf-token")
    user_id_from_auth_method = self.get_json_value(response1, "user_id")

    response2 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                             headers={"x-csrf-token": token},
                             cookies={"auth_sid": auth_sid})

    Assertions.assert_code_status(response2, 400)

  @allure.tag("User deletion")
  @allure.suite("Positive cases")
  @allure.description("This test successfully delete just created user")
  def test_delete_user_just_created(self):
    #Register
    register_data = self.prepare_registration_date()
    response1 = MyRequests.post("/user/", data=register_data)

    Assertions.assert_code_status(response1, 200)
    Assertions.assert_json_has_key(response1, "id")

    email = register_data['email']
    first_name = register_data['firstName']
    password = register_data['password']
    user_id = self.get_json_value(response1, "id")

    #Login
    login_date = {
        'email': email,
        'password': password
    }

    response2 = MyRequests.post("/user/login", data=login_date)

    Assertions.assert_code_status(response2, 200)

    auth_sid = self.get_cookie(response2, "auth_sid")
    token = self.get_header(response2, "x-csrf-token")

    #Delete
    new_name = "Changed Name"

    response3 = MyRequests.delete(
        f"/user/{user_id}",
        headers={"x-csrf-token": token},
        cookies={"auth_sid": auth_sid},
    )

    Assertions.assert_code_status(response3, 200)

    #Get
    response4 = MyRequests.get(
        f"/user/{user_id}",
        headers={"x-csrf-token": token},
        cookies={"auth_sid": auth_sid}
    )

    print(response4.text)

    Assertions.assert_code_status(response4, 404)

  @allure.tag("User deletion")
  @allure.suite("Negative cases")
  @allure.description("This test unsuccessfully delete user 1 under user 2")
  def test_delete_u1_authorized_under_u2(self):
    #Register user_1
    data_u1 = self.prepare_registration_date()
    for data in data_u1:
      if data != "email":
        data_u1[data] = "user1"
    response_u1 = MyRequests.post("/user/", data=data_u1)

    Assertions.assert_code_status(response_u1, 200)
    Assertions.assert_json_has_key(response_u1, "id")

    email_u1 = data_u1['email']
    first_name_u1 = data_u1['firstName']
    password_u1 = data_u1['password']
    id_u1 = self.get_json_value(response_u1, "id")

    #Register user_2
    data_u2 = self.prepare_registration_date()
    for data in data_u2:
      if data != "email":
        data_u2[data] = "user2"
    response_u2 = MyRequests.post("/user/", data=data_u2)

    Assertions.assert_code_status(response_u2, 200)
    Assertions.assert_json_has_key(response_u2, "id")

    email_u2 = data_u2['email']
    first_name_u2 = data_u2['firstName']
    password_u2 = data_u2['password']
    id_u2 = self.get_json_value(response_u2, "id")

    #Login
    response_login_u2 = MyRequests.post(
        "/user/login", data=data_u2)

    auth_sid_u2 = self.get_cookie(response_login_u2, "auth_sid")
    token_u2 = self.get_header(response_login_u2, "x-csrf-token")

    #Delete u1 under u2
    response_deleting_u1_auth_under_u2 = MyRequests.delete(
        f"/user/{id_u1}",
        headers={"x-csrf-token": token_u2},
        cookies={"auth_sid": auth_sid_u2},
    )

    Assertions.assert_code_status(
        response_deleting_u1_auth_under_u2, 200)  # ?????

    #Login as u1
    login_date_u1 = {
        'email': email_u1,
        'password': password_u1
    }

    response_login_u1 = MyRequests.post("/user/login", data=login_date_u1)

    Assertions.assert_code_status(response_login_u1, 200)
    auth_sid_u1 = self.get_cookie(response_login_u1, "auth_sid")
    token_u1 = self.get_header(response_login_u1, "x-csrf-token")

    #??????????? user 2 not found
    # login_date_u2 = {
    #     'email': email_u2,
    #     'password': password_u2
    # }
    # response_login_u2 = MyRequests.post("/user/login", data=login_date_u2)
    # Assertions.assert_code_status(response_login_u2, 200)

    #Check data u1
    response_response_u1_check = MyRequests.get(
        f"/user/{id_u1}",
        headers={"x-csrf-token": token_u1},
        cookies={"auth_sid": auth_sid_u1})

    Assertions.assert_code_status(response_response_u1_check, 200)
