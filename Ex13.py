import requests
import pytest


class TestUserAgent:
    user_agents_list = [
        {
            'user_agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {
            'user_agent': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
            'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
         'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
            'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {
            'user_agent': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'},
    ]

    @pytest.mark.parametrize('user_agent', user_agents_list)
    def test_user_agent(self, user_agent):
        print(
            "--------------------------------------------------------------------------------------------------------------")
        print(user_agent['user_agent'])
        url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        data_user_agent = user_agent['user_agent']

        response = requests.get(url, headers={'User-agent': data_user_agent})
        response_json = response.json()

        platform = response_json['platform']
        browser = response_json['browser']
        device = response_json['device']

        print(f"{'platform:':>10} {platform:>7} {'=> response answer':>15}")
        print(f"{'browser:':>10} {browser:>7} {'=> response answer':>15}")
        print(f"{'device:':>10} {device:>7} => response answer")
        print("-/-")
        print(f"{'platform:':>10} {user_agent['platform']:>7} {'=> expected answer':>15}")
        print(f"{'browser:':>10} {user_agent['browser']:>7} {'=> expected answer':>15}")
        print(f"{'device:':>10} {user_agent['device']:>7} {'=> expected answer':>15}")

        assert platform == user_agent['platform'], f"ОР и ФР не равны для: {user_agent}"
        assert browser == user_agent['browser'], f"ОР и ФР не равны для: {user_agent}"
        assert device == user_agent['device'], f"ОР и ФР не равны для: {user_agent}"
