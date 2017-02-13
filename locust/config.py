"""
Configurations shared across load tests.
"""
import os
import uuid

# User credentials
EXISTING_USER_EMAIL = os.environ['ARBISOFT_USER_EMAIL']
EXISTING_USER_PASSWORD = 'edx'

# URLS
LOGIN_PAGE_URL = u"/login"
REGISTRATION_PAGE_URL = u"/register"
REGISTER_URL = u"/user_api/v1/account/registration/"
LOGIN_URL = u"/user_api/v1/account/login_session/"
DASHBOARD_PAGE_URL = u"/dashboard"
COURSE_MAIN_PAGE_URL = u"/courses/course-v1:Arbisoft+Hiring_1+2017_1/" \
                       u"courseware/b9c7266533ea42cba4ea23d8f8d2144f/" \
                       u"9dd501863ddc42f08e38087dc8a654b3/"
SURVEY_PAGE_URL = u"/arbisoft_survey"

# Parameters
SURVEY_PARAMS = {
    "graduation_date":"2017-02-08",
    "phone_number":"5345345",
    "cgpa":"4",
    "position_in_class":"7",
    "academic_projects":"gfhfghfg",
    "extra_curricular_activities":"fghfghfg",
    "freelance_work":"vbgfdgdf",
    "accomplishment":"dfgfhghjg",
    "individuality_factor":"gfhghfd",
    "ideal_organization":"fgdgbfbfgh",
    "why_arbisoft":"hfghfghfghg",
    "expected_salary":"5",
    "career_plan":"fgdfjhggf",
    "references":"fghfhgfhg",
    "studied_course":"Computer+Organization+and+Assembly+Language",
    "other_studied_course":"",
    "technology":"Android",
    "other_technology":"",
    "form-TOTAL_FORMS":"12",
    "form-INITIAL_FORMS":"0",
    "form-MIN_NUM_FORMS":"0",
    "form-MAX_NUM_FORMS":"1000",
    "form-0-expertise":"Introduction+to+computing",
    "form-0-rank":"1",
    "form-0-id":"",
    "form-1-expertise":"Programming",
    "form-1-rank":"1",
    "form-1-id":"",
    "form-2-expertise":"Object+oriented+programming",
    "form-2-rank":"1",
    "form-2-id":"",
    "form-3-expertise":"Data+Structures",
    "form-3-rank":"1",
    "form-3-id":"",
    "form-4-expertise":"Computer+Organization+and+Assembly+Language",
    "form-4-rank":"1",
    "form-4-id":"",
    "form-5-expertise":"Software+Engineering",
    "form-5-rank":"1",
    "form-5-id":"",
    "form-6-expertise":"Computer+networks",
    "form-6-rank":"1",
    "form-6-id":"",
    "form-7-expertise":"Artificial+intelligence",
    "form-7-rank":"1",
    "form-7-id":"",
    "form-8-expertise":"Databases",
    "form-8-rank":"1",
    "form-8-id":"",
    "form-9-expertise":"Operating+System",
    "form-9-rank":"1",
    "form-9-id":"",
    "form-10-expertise":"Algorithms",
    "form-10-rank":"1",
    "form-10-id":"",
    "form-11-expertise":"Bio-Informatics",
    "form-11-rank":"1",
    "form-11-id":""
}