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

    def visit_course_main_page(self):
        """
        Visit Course main page
        """
        self._get(
            COURSE_MAIN_PAGE_URL,
            response_string="Courseware",
            url_group_name="course_main_page"
        )

    def start_exam(self):
        """
        Start Exam
        """
        self.default_headers["Referer"] = self.hostname + EXAM_MAIN_PAGE_URL
        self.default_headers["X-CSRFToken"] = self.client.cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {
            "exam_id": "1",
            "start_exam": "true"
        }
        self._post(START_EXAM_URL, params = params)

    def visit_exam_main_page(self):
        """
        Visit Exam main page
        """
        self._get(
            EXAM_MAIN_PAGE_URL,
            response_string="Timed Exam",
            url_group_name="exam_main_page"
        )

    def visit_random_question(self, question_id):
        """
        Visit question  page
        """
        self._get(
            QUESTION_URL.format(question_id),
            url_group_name=question_id
        )

    def submit_answer_1(self, block_id, input_id, choice_id):
        """
        Submit answer
        :param block_id:
        :param input_id:
        :param choice_id:
        """
        self.default_headers["Referer"] = self.hostname + EXAM_MAIN_PAGE_URL
        self.default_headers["X-CSRFToken"] = self.client.cookies['csrftoken']
        self.default_headers["X-Requested-With"] = "XMLHttpRequest"
        params = {input_id: choice_id}
        self._post(SUBMIT_ANSWER_1_URL.format(block_id), params = params)

