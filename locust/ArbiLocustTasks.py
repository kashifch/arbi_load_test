from locust import task, TaskSet
from login import LoginPage
from dashboard_page import DashboardPage
from course_page import CoursePage
from registration import RegistrationPage


class LoggedInTasks(TaskSet):
    """
    User scripts that exercise the viewing of course material pages
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(LoggedInTasks, self).__init__(*args, **kwargs)
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)
        self.course_page = CoursePage(self.locust.host, self.client)

    @task(1)
    def login(self):
        """
        View the pages repeatedly
        """
        response = self.login_page.visit_login_page()
        cookies = self.login_page.login_existing_user(response)
        self.dahboard_page.visit_dashboard_page(cookies)
        self.course_page.visit_course_main_page(cookies)


class RegistrationTasks(TaskSet):
    """
    User scripts that exercise the viewing of course material pages
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(RegistrationTasks, self).__init__(*args, **kwargs)
        self.registration_page = RegistrationPage(
            self.locust.host,
            self.client
        )

    @task(1)
    def visit_registration_page(self):
        """
        Visit Registration page
        """
        registration_page_cookies = \
            self.registration_page.visit_registration_page()
        registration_cookies = self.registration_page.register_new_user(
            registration_page_cookies
        )
        self.registration_page.visit_survey_page(registration_cookies)
        self.registration_page.submit_survey(registration_cookies)
