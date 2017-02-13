from arbi_base import ArbiBase
from config import DASHBOARD_PAGE_URL


class DashboardPage(ArbiBase):

    """
    Dashboard page class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Task set.
        """
        super(DashboardPage, self).__init__(*args, **kwargs)

    def visit_dashboard_page(self, cookies):
        """
        Visit Dashboard
        :param cookies:
        """
        self._get(
            DASHBOARD_PAGE_URL,
            response_string='Dashboard"',
            url_group_name="dashboard_page",
            cookie=cookies
        )

