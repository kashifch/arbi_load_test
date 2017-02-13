from arbi_base import ArbiBase
from config import COURSE_MAIN_PAGE_URL


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

