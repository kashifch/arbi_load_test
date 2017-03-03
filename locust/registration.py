import uuid
import collections
from arbi_base import ArbiBase
from config import (
    REGISTRATION_PAGE_URL,
    REGISTER_URL,
    SURVEY_PAGE_URL,
    SURVEY_PARAMS,
    USER_PASSWORD
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
        return response.cookies

    def register_new_user(self, cookies):
        """
        Register new user
        :param cookies:
        :return: cookies
        """
        RegistrationInfo = collections.namedtuple('RegistrationInfo', 'session user')
        url = REGISTER_URL
        user_name = str(uuid.uuid4().node)
        email = user_name + "@example.com"
        registration_params = {
                    "email": email,
                    "name": "Test User",
                    "username": user_name,
                    "password": USER_PASSWORD,
                    "level_of_education": "master",
                    "gender": "m",
                    "year_of_birth": "1999",
                    "mailing_address": "abc def",
                    "goals": "",
                    "honor_code": "true"
        }
        self.default_headers["Referer"] = self.hostname + "/register?next=%2Fdashboard"
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        response = self._post(
            url,
            registration_params,
            cookies
        )
        return RegistrationInfo(session=response.cookies, user=email)

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
        """
        Submit survey
        :param cookies:
        :return: cookies
        """
        referer_url = self.hostname + SURVEY_PAGE_URL
        self.default_headers["Referer"] = referer_url
        SURVEY_PARAMS["csrfmiddlewaretoken"] = cookies["csrftoken"]
        response = self._post(SURVEY_PAGE_URL, params=SURVEY_PARAMS, cookie=cookies)
        return response.cookies
