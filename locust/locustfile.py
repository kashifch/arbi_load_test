import os
from locust import HttpLocust, TaskSet
from ArbiLocustTasks import LoginTasks, RegistrationTasks, CourseTasks, AllTasks, LogistrationTasks


class ArbiTest(TaskSet):
    """
    Execute Load tests
    """
    tasks = {
        LoginTasks: 10,
        RegistrationTasks: 1,
        CourseTasks: 10,
        AllTasks: 10,
        LogistrationTasks: 1
    }


class ArbisoftLocust(HttpLocust):
    """
    Representation of an HTTP "user".
    Defines how long a simulated user should wait between executing tasks, as
    well as which TaskSet class should define the user's behavior.
    """
    task_set = globals()[os.getenv('LOCUST_TASK_SET', 'ArbiTest')]
    min_wait = 70000
    max_wait = 120000
