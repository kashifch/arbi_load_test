from arbi_base import ArbiBase
from config import COURSE_MAIN_PAGE_URL, EXAM_MAIN_PAGE_URL, QUESTION_URL, SUBMIT_ANSWER_1_URL, START_EXAM_URL


class CoursePage(ArbiBase):

    """
    Course page Class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(CoursePage, self).__init__(*args, **kwargs)

    def visit_course_main_page(self, cookies):
        """
        Visit Course main page
        :param cookies:
        """
        self._get(
            COURSE_MAIN_PAGE_URL,
            response_string="Courseware",
            url_group_name="course_main_page",
            cookie=cookies
        )


    def start_exam(self, cookies):
        self.default_headers["Referer"] = self.hostname + EXAM_MAIN_PAGE_URL
        self.default_headers["X-CSRFToken"] = cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {
            "exam_id": "1",
            "start_exam": "true"
        }
        self._post(
            START_EXAM_URL,
            params = params,
            cookie=cookies
        )


    def visit_exam_main_page(self, cookies):
        """
        Visit Exam main page
        :param cookies:
        """
        self._get(
            EXAM_MAIN_PAGE_URL,
            response_string="Timed Exam",
            url_group_name="exam_main_page",
            cookie=cookies
        )

    def visit_random_question(self, cookies):
        """
        Visit question  page
        :param cookies:
        """
        self._get(
            QUESTION_URL,
            url_group_name="question_2",
            cookie=cookies
        )

    def submit_answer_1(self, cookies, block_id, input_id, choice_id):
        """
        Visit question  page
        :param cookies:
        """

        self.default_headers["Referer"] = self.hostname + EXAM_MAIN_PAGE_URL
        self.default_headers["X-CSRFToken"] = cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {
            input_id: choice_id
        }
        self._post(
            SUBMIT_ANSWER_1_URL.format(block_id),
            params = params,
            cookie=cookies
        )

