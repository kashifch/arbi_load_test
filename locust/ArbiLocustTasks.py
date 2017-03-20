import random
from locust import task, TaskSet
from login import LoginPage
from dashboard_page import DashboardPage
from course_page import CoursePage
from registration import RegistrationPage
from config import USER_EMAILS, PROBLEM_DATA, QUESTIONS_ID


class LoginTasks(TaskSet):
    """
    User scripts that tests the login
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(LoginTasks, self).__init__(*args, **kwargs)
        self.login_page = LoginPage(self.locust.host, self.client)
        self.dahboard_page = DashboardPage(self.locust.host, self.client)

    @task(1)
    def login(self):
        """
        View the pages repeatedly
        """
        self.login_page.visit_login_page()
        self.login_page.login_existing_user()


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
        """
        Login and start exam
        :return:
        """
        user_email = USER_EMAILS.pop()
        self.login_page.visit_login_page()
        self.login_page.login_new_user(user_email)
        self.course_page.start_exam()

    @task(1)
    def dashboard_page(self):
        """
        Visit dashboard page
        """
        self.dahboard_page.visit_dashboard_page()

    @task(1)
    def course_main_page(self):
        """
        Visit course page
        """
        self.course_page.visit_course_main_page()

    @task(1)
    def exam_main_page(self):
        """
        Visit exam page
        """
        self.course_page.visit_exam_main_page()

    @task(8)
    def question_page(self):
        """
        Visit question page
        """
        for q_id in QUESTIONS_ID:
            self.course_page.visit_random_question(q_id)

    @task(20)
    def answer(self):
        """
        Submit answer
        """
        for key in PROBLEM_DATA:
            self.course_page.submit_answer_1(
                PROBLEM_DATA[key]['block_id'],
                PROBLEM_DATA[key]['input_id'],
                PROBLEM_DATA[key]['choice_id']
            )


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
        self.registration_page.visit_registration_page()
        self.registration_page.register_new_user()
        self.registration_page.visit_survey_page()
        self.registration_page.submit_survey()


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

    def on_start(self):
        """
        Create a new user
        """
        self.registration_page.visit_registration_page()
        self.user_email = self.registration_page.register_new_user()
        self.registration_page.visit_survey_page()
        self.registration_page.submit_survey()

    @task(1)
    def login(self):
        """
        View the pages repeatedly
        """
        self.login_page.visit_login_page()
        self.login_page.login_new_user(self.user_email)
        self.dahboard_page.visit_dashboard_page()

    @task(10)
    def dashboard_page(self):
        """
        View Dashboard page
        :return:
        """
        self.dahboard_page.visit_dashboard_page()
