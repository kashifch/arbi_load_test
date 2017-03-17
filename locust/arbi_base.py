from config import BASIC_AUTH_CREDENTIALS


class ApiException(Exception):
    """
    Exceptions for API failures
    """
    pass


class ArbiBase(object):
    """
    Base class for page objects.
    """

    def __init__(self, hostname, client):
        """
        Initialize the client.
        :param hostname: The hostname of the test server
        :param client: The test client used by locust.
        """
        self.hostname = hostname
        self.client = client
        # self.client.auth = BASIC_AUTH_CREDENTIALS

        self.default_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
        }

    def _check_response(self, response):
        """
        Check whether a response was successful.
        """
        if response.status_code != 200:
            raise Exception(
                'API request failed with following error code: ' +
                str(response.status_code)
            )

    def _get(self, url, response_string="", url_group_name="", cookie=None):
        """
        Make a GET request to the server.
        Skips SSL verification.
        Make the response to fail if verification string is not present
        """
        with self.client.get(
                url,
                verify=False,
                catch_response=True,
                headers=self.default_headers,
                name=url_group_name,
                cookies=cookie
        ) as response:
            if response.status_code != 200:
                    response.failure("API request failed with following error code: " + str(response.status_code))
            else:
                if response_string:
                    if response_string not in response.content:
                        response.failure("Not on the correct page")
                        print(response.content)
        return response

    def _post(self, url, params, cookie=None):
        """
        Make a POST request to the server.
        Skips SSL verification and sends the CSRF cookie.
        """
        kwargs = {'cookies': cookie, 'headers': self.default_headers}
        response = self.client.post(url, data=params, **kwargs)
        self._check_response(response)
        return response
