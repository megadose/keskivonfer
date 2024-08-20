import requests
import json
import logging

from fake_useragent import UserAgent

class UserNotFound(Exception):
    def __init__(self):
        self.msg = "User not found!"

MAX_RETRIES = 10
ua = UserAgent()
HEADERS = {
        'User-Agent': ua.firefox,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers'

        }

class Requester:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.VINTED_AUTH_URL = f"https://www.vinted.com/auth/token_refresh"
        self.params = ('localize', 'true')


    def get_information(self, username, vinted_extension="com"):
        if vinted_extension is None:
            vinted_extension = "com"

        tried = 0

        while tried < MAX_RETRIES:
            tried += 1
            with self.session.get(f"https://www.vinted.{vinted_extension}/api/v2/users/{username}") as response:

                if response.status_code == 401 and tried < MAX_RETRIES:
                    logging.info(f"Cookies invalid retrying {tried}/{MAX_RETRIES}")
                    self.set_cookies()

                elif response.status_code == 200 or tried == MAX_RETRIES:
                    json_content = json.loads(response.content.decode("utf-8"))

                    if json_content["code"] == 104:
                        raise UserNotFound

                    return json.loads(response.content.decode("utf-8"))["user"]


    def post(self,url, params=None):
        response = self.session.post(url, params)
        response.raise_for_status()
        return response

    def set_cookies(self):
        self.session.cookies.clear_session_cookies()

        try:
            self.post(self.VINTED_AUTH_URL)
            logging.info("Cookies set!")

        except Exception as e:
            print(f"There was an error fetching cookies for vinted\n Error : {e}")