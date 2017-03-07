"""
Configurations shared across load tests.
"""
import os
import csv

# HTTP authentication credentials
BASIC_AUTH_USER = os.environ['BASIC_AUTH_USER']
BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD']
BASIC_AUTH_CREDENTIALS = (BASIC_AUTH_USER, BASIC_AUTH_PASSWORD)

# User credentials
EXISTING_USER_EMAIL = os.getenv('ARBISOFT_USER_EMAIL', 'kashif.chaudhry@arbisoft.com')
USER_PASSWORD = 'edx'

USER_FILE = os.getenv('USER_FILE', 'users')

# URLS
LOGIN_PAGE_URL = u"/login"
REGISTRATION_PAGE_URL = u"/register"
REGISTER_URL = u"/user_api/v1/account/registration/"
SURVEY_PAGE_URL = u"/application_form"
LOGIN_URL = u"/user_api/v1/account/login_session/"
DASHBOARD_PAGE_URL = u"/dashboard"
COURSE_MAIN_PAGE_URL = u"/courses/course-v1:Arbisoft+Hiring_1+2017_1/courseware/b9c7266533ea42cba4ea23d8f8d2144f/ccf2696e7f6a463b8ed438a3ccb49fa6/"
START_EXAM_URL = u"/api/edx_proctoring/v1/proctored_exam/attempt"
EXAM_MAIN_PAGE_URL = u"/courses/course-v1:Arbisoft+Hiring_1+2017_1/courseware/b9c7266533ea42cba4ea23d8f8d2144f/9dd501863ddc42f08e38087dc8a654b3/"
QUESTION_URL = u"/asset-v1:Arbisoft+Hiring_1+2017_1+type@asset+block@{}"
SUBMIT_ANSWER_1_URL = u"/courses/course-v1:Arbisoft+Hiring_1+2017_1/xblock/block-v1:Arbisoft+Hiring_1+2017_1+type@problem+block@{}/handler/xmodule_handler/problem_check"

# Parameters
SURVEY_PARAMS = {
"graduation_date":"2017-02-01",
"phone_number":"12224545678",
"cgpa":"4",
"position_in_class":"1",
"academic_projects":"abc+and+def",
"extra_curricular_activities":"none+",
"freelance_work":"none",
"accomplishment":"none",
"individuality_factor":"nothing",
"ideal_organization":"competent",
"why_arbisoft":"good+environment",
"expected_salary":"50000",
"career_plan":"nothing",
"studied_course":"Programming",
"studied_course":"Object+Oriented+Programming",
"studied_course":"Data+Structures",
"other_studied_course":"abc%2C+def%2C+ghi",
"technology":"Web+Development",
"technology":"Mobile+Development+%28Android%29",
"other_technology":"abc%2C+def",
"ranking-TOTAL_FORMS":"8",
"ranking-INITIAL_FORMS":"0",
"ranking-MIN_NUM_FORMS":"0",
"ranking-MAX_NUM_FORMS":"1000",
"ranking-0-expertise":"Programming",
"ranking-0-rank":"2",
"ranking-0-id": "",
"ranking-1-expertise":"Object+Oriented+Programming",
"ranking-1-rank":"3",
"ranking-1-id":"",
"ranking-2-expertise":"Data+Structures",
"ranking-2-rank":"3",
"ranking-2-id":"",
"ranking-3-expertise":"Software+Engineering",
"ranking-3-rank":"4",
"ranking-3-id":"",
"ranking-4-expertise":"Artificial+Intelligence",
"ranking-4-rank":"5",
"ranking-4-id":"",
"ranking-5-expertise":"Databases",
"ranking-5-rank":"5",
"ranking-5-id":"",
"ranking-6-expertise":"Operating+System",
"ranking-6-rank":"4",
"ranking-6-id":"",
"ranking-7-expertise":"Algorithms",
"ranking-7-rank":"5",
"ranking-7-id":"",
"reference-TOTAL_FORMS":"2",
"reference-INITIAL_FORMS":"0",
"reference-MIN_NUM_FORMS":"0",
"reference-MAX_NUM_FORMS":"1000",
"reference-0-name":"abc",
"reference-0-position":"1",
"reference-0-phone_number":"0222434566",
"reference-0-id":"",
"reference-1-name":"def",
"reference-1-position":"2",
"reference-1-phone_number":"0222345667",
"reference-1-id":""
}


def fetch_emails():
    file_name = USER_FILE + '.csv'
    with open(file_name, 'U') as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)

USER_EMAILS = fetch_emails()

PROBLEM_DATA = {
    'problem_1': {
        'block_id': '906f1d62bab5b1bcf7e7',
        'input_id': 'input_906f1d62bab5b1bcf7e7_2_1',
        'choice_id': 'choice_2'
    },
    'problem_2': {
        'block_id': 'd6c410d4e850e223e3fc',
        'input_id': 'input_d6c410d4e850e223e3fc_2_1',
        'choice_id': 'choice_3'
    },
    'problem_3': {
        'block_id': '272144c43564a4069e81',
        'input_id': 'input_272144c43564a4069e81_2_1',
        'choice_id': 'choice_4'
    },
    'problem_4': {
        'block_id': 'cdc59713246ec7f7c445',
        'input_id': 'input_cdc59713246ec7f7c445_2_1',
        'choice_id': 'choice_2'
    },
    'problem_5': {
        'block_id': '02558815761b2a959dcd',
        'input_id': 'input_02558815761b2a959dcd_2_1',
        'choice_id': 'choice_2'
    },
    'problem_6': {
        'block_id': '8d96920a9b519d8982d7',
        'input_id': 'input_8d96920a9b519d8982d7_2_1',
        'choice_id': 'choice_2'
    },
    'problem_7': {
        'block_id': '0eeba9376a99a6846451',
        'input_id': 'input_0eeba9376a99a6846451_2_1',
        'choice_id': 'choice_2'
    },
    'problem_8': {
        'block_id': '02558815761b2a959dcd',
        'input_id': 'input_02558815761b2a959dcd_2_1',
        'choice_id': 'choice_2'
    },
    'problem_9': {
        'block_id': '5d8c208cd2f79cee254f',
        'input_id': 'input_5d8c208cd2f79cee254f_2_1',
        'choice_id': 'choice_2'
    },
    'problem_10': {
        'block_id': '62266522e32dcdcc2af8',
        'input_id': 'input_62266522e32dcdcc2af8_2_1',
        'choice_id': 'choice_2'
    }
}

QUESTIONS_ID = [
    'Screen_Shot_2017-02-03_at_11.52.12_PM.png',
    'Screen_Shot_2017-02-15_at_10.26.36_PM.png',
    'Screen_Shot_2017-02-15_at_9.35.04_PM.png'
]