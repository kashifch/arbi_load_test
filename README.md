Locust Tests
============
The tests in this directory utilize the [Locust](http://docs.locust.io/en/latest/) load testing tool.

Getting Started
---------------

Get started by first installing Locust and any other prerequisites using the below command (optionally you could 
create a virtual env before installing the software)  

    $ pip install -r requirements.txt

The locust folder contains a `locustfile.py`. In order to run the tests, cd into the locust folder and run the 
`locust` command as shown below. Remember to replace `<host>` with the hostname of the actual server being tested.

    $ locust --host=<host>
Example:  
 
    $ ARBISOFT_USER_EMAIL=*** locust --host=http://site_name
    
The Tasks are mainly divided in two Parts, the Registration Tasks and the Logged In Tasks.

To run these tasks seperately you can specify a single task in command

    $ ARBISOFT_USER_EMAIL=*** LOCUST_TASK_SET=RegistrationTasks locust --host=http://site_name
    $ ARBISOFT_USER_EMAIL=*** LOCUST_TASK_SET=LoggedInTasks locust --host=http://site_name
    
After running the command visit `http://127.0.0.1:8089` and provide number of users and hatch rate (how many 
users to add per second)