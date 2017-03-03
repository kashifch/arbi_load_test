from arbi_base import ArbiBase
from config import (
    LOGIN_PAGE_URL,
    LOGIN_URL,
    EXISTING_USER_EMAIL,
    USER_PASSWORD
)


class LoginPage(ArbiBase):

    """
    Login Page Class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(LoginPage, self).__init__(*args, **kwargs)

    def visit_login_page(self):
        """
        Visit the Login page and return response
        :return:
        """
        response = self._get(LOGIN_PAGE_URL, url_group_name="login_page")
        return response.cookies

    def login_existing_user(self, cookies):
        """
        Login Existing user
        :param cookies:
        :return: cookies
        """
        referer_url = self.hostname + LOGIN_PAGE_URL
        self.default_headers["Referer"] = referer_url
        self.default_headers["X-CSRFToken"] = cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {
            "email": EXISTING_USER_EMAIL,
            "password": USER_PASSWORD,
            "remember": "false"
        }
        response = self._post(LOGIN_URL, params, cookies)
        return response.cookies

    def login_new_user(self, cookies, user_email):
        """
        Login New user
        :param cookies:
        :param user_email:
        :return: cookies
        """
        referer_url = self.hostname + LOGIN_PAGE_URL
        self.default_headers["Referer"] = referer_url
        self.default_headers["X-CSRFToken"] = cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {
            "email": user_email,
            "password": USER_PASSWORD,
            "remember": "false"
        }
        response = self._post(LOGIN_URL, params, cookies)
        return response.cookies
