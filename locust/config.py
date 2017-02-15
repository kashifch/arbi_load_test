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
SURVEY_PAGE_URL = u"/application_form"

# Parameters
SURVEY_PARAMS = {
"csrfmiddlewaretoken":"Pid0y0LxjDuYLIU3FX33ER6RjjjJXPs1",
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
