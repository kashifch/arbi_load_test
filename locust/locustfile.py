import os
from locust import HttpLocust, TaskSet
from ArbiLocustTasks import LoggedInTasks, RegistrationTasks


class ArbiTest(TaskSet):
    """
    Execute Load tests
    """
    tasks = {
        LoggedInTasks: 1,
        RegistrationTasks: 1
    }


class ArbisoftLocust(HttpLocust):
    """
    Representation of an HTTP "user".
    Defines how long a simulated user should wait between executing tasks, as
    well as which TaskSet class should define the user's behavior.
    """
    task_set = globals()[os.getenv('LOCUST_TASK_SET', 'ArbiTest')]
    min_wait = 60000
    max_wait = 90000
