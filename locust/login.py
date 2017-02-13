from arbi_base import ArbiBase
from config import (
    LOGIN_PAGE_URL,
    LOGIN_URL,
    EXISTING_USER_EMAIL,
    EXISTING_USER_PASSWORD
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
        return response.cookies['csrftoken']

    def login_existing_user(self, login_page_csrf):
        """
        Login Existing user
        :param login_page_csrf:
        :return: cookies
        """
        url = LOGIN_URL
        cookie = {'csrftoken': login_page_csrf}
        referer_url = self.hostname + LOGIN_PAGE_URL
        self.default_headers["Referer"] = referer_url
        self.default_headers["X-CSRFToken"] = login_page_csrf
        params = {
            "email": EXISTING_USER_EMAIL,
            "password": EXISTING_USER_PASSWORD,
            "remember": "false"
        }
        response = self._post(url, params, cookie)
        c_list = ["csrftoken", "sessionid", "edx-user-info", "edxloggedin"]
        return self.cookies_dict(response, c_list )
