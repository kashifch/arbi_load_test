from locust import task, TaskSet
from login import LoginPage
from dashboard_page import DashboardPage
from course_page import CoursePage
from registration import RegistrationPage


class AllTasks(TaskSet):
    """
    User scripts that test complete cycle
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(AllTasks, self).__init__(*args, **kwargs)
        self.registration_page = RegistrationPage(
            self.locust.host,
            self.client
        )
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)
        self.course_page = CoursePage(self.locust.host, self.client)
        self.user_session = None

    def on_start(self):
        """
        View the pages repeatedly
        """
        registration_page_cookies = \
            self.registration_page.visit_registration_page()

        registration_info = self.registration_page.register_new_user(
            registration_page_cookies
        )
        registration_cookies = registration_info.session
        user_email = registration_info.user
        self.registration_page.visit_survey_page(registration_cookies)
        self.registration_page.submit_survey(registration_cookies)
        response = self.login_page.visit_login_page()
        self.user_session = self.login_page.login_new_user(response, user_email)
        # self.dahboard_page.visit_dashboard_page(self.user_session)
        # self.course_page.visit_course_main_page(self.user_session)
        # # self.course_page.start_exam(self.user_session)
        # self.course_page.visit_exam_main_page(self.user_session)

    @task(10)
    def dashboard_page(self):
        self.dahboard_page.visit_dashboard_page(self.user_session)

    # @task(20)
    # def course_main_page(self):
    #     self.course_page.visit_course_main_page(self.user_session)
    #
    # @task(8)
    # def exam_main_page(self):
    #     self.course_page.visit_exam_main_page(self.user_session)

    # @task(8)
    # def question_page(self):
    #     self.course_page.visit_random_question(self.user_session)
    #
    # @task(9)
    # def answer(self):
    #     self.course_page.submit_answer_1(self.user_session)




class LoginTasks(TaskSet):
    """
    User scripts that exercise the viewing of course material pages
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(LoginTasks, self).__init__(*args, **kwargs)
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)
        self.course_page = CoursePage(self.locust.host, self.client)

    @task(1)
    def login(self):
        """
        View the pages repeatedly
        """
        response = self.login_page.visit_login_page()
        login_cookies = self.login_page.login_existing_user(response)
        self.dahboard_page.visit_dashboard_page(login_cookies)


class CourseTasks(TaskSet):
    """
    User scripts that exercise the viewing of course material pages
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(CourseTasks, self).__init__(*args, **kwargs)
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)
        self.course_page = CoursePage(self.locust.host, self.client)

    def on_start(self):
        response = self.login_page.visit_login_page()
        self.login_cookies = self.login_page.login_existing_user(response)

    @task(1)
    def dashboard_page(self):
        self.dahboard_page.visit_dashboard_page(self.login_cookies)

    @task(1)
    def course_main_page(self):
        self.course_page.visit_course_main_page(self.login_cookies)

    @task(8)
    def exam_main_page(self):
        self.course_page.visit_exam_main_page(self.login_cookies)

    @task(8)
    def question_page(self):
        self.course_page.visit_random_question(self.login_cookies)

    @task(9)
    def answer(self):
        self.course_page.submit_answer_1(self.login_cookies)


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
    def registration(self):
        """
        Visit Registration page
        """
        registration_page_cookies = \
            self.registration_page.visit_registration_page()
        registration_info = self.registration_page.register_new_user(
            registration_page_cookies
        )
        registration_cookies = registration_info.session
        self.registration_page.visit_survey_page(registration_cookies)
        self.registration_page.submit_survey(registration_cookies)


class LogistrationTasks(TaskSet):
    """
    User scripts that exercise the viewing of course material pages
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(LogistrationTasks, self).__init__(*args, **kwargs)
        self.registration_page = RegistrationPage(
            self.locust.host,
            self.client
        )
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)
        self.user_email = None

    @task(1)
    def registration(self):
        """
        Visit Registration page
        """
        registration_page_cookies = \
            self.registration_page.visit_registration_page()
        registration_info = self.registration_page.register_new_user(
            registration_page_cookies
        )
        registration_cookies = registration_info.session
        self.user_email = registration_info.user
        self.registration_page.visit_survey_page(registration_cookies)
        self.registration_page.submit_survey(registration_cookies)

    @task(10)
    def login(self):
        """
        View the pages repeatedly
        """
        response = self.login_page.visit_login_page()
        login_cookies = self.login_page.login_existing_user(response)
        self.dahboard_page.visit_dashboard_page(login_cookies)
