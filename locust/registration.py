import uuid
from arbi_base import ArbiBase
from config import (
    REGISTRATION_PAGE_URL,
    REGISTER_URL,
    SURVEY_PAGE_URL,
    SURVEY_PARAMS
)


class RegistrationPage(ArbiBase):

    """
    Registration Page Class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(RegistrationPage, self).__init__(*args, **kwargs)

    def visit_registration_page(self):
        """
        Visit Registration page
        :return: cookies
        """
        response = self._get(
            REGISTRATION_PAGE_URL,
            url_group_name="registration_page"
        )
        c_list = ["csrftoken"]
        return self.cookies_dict(response, c_list )

    def register_new_user(self, registration_page_cookies):
        """
        Register new user
        :param registration_page_cookies:
        :return: cookies
        """
        url = REGISTER_URL
        user_name = str(uuid.uuid4().node)
        email = user_name + "@example.com"
        REGISTRATION_PARAMS = {
                    "email": email,
                    "name": "Test User",
                    "username": user_name,
                    "password": 'arbi',
                    "level_of_education": "",
                    "gender": "",
                    "year_of_birth": "",
                    "mailing_address": "",
                    "goals": "",
                    "honor_code": "true"
        }
        referer_url = self.hostname + "/register?next=%2Fdashboard"
        self.default_headers["Referer"] = referer_url
        response = self._post(
            url,
            REGISTRATION_PARAMS,
            registration_page_cookies
        )
        c_list = ["csrftoken", "sessionid", "edx-user-info", "edxloggedin"]
        return self.cookies_dict(response, c_list )

    def visit_survey_page(self, cookies):
        """
        Visit survey page
        :param cookies:
        """
        self._get(
            SURVEY_PAGE_URL,
            response_string="Arbisoft Hiring",
            url_group_name="survey_page",
            cookie=cookies
        )

    def submit_survey(self, cookies):
        referer_url = self.hostname + SURVEY_PAGE_URL
        self.default_headers["Referer"] = referer_url
        SURVEY_PARAMS["csrfmiddlewaretoken"] = cookies["csrftoken"]
        self._post(SURVEY_PAGE_URL, params=SURVEY_PARAMS, cookie=cookies)
