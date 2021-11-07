import Challenge_8
from tud_test_base import set_keyboard_input, get_display_output

# This test will simply require a new account to have been created with the username allenda and
# password dsdas123A- and that same account have no profile and have had seven days elapsed since they
# last looked for a job


def test_seven_day_job_notification():
    set_keyboard_input(["allenda", "dsdas123A-", "13"])
    Challenge_8.login()
    output = get_display_output()
    assert output == [
        '\n'
        'Log In',
        'Please Enter Your UserName: ',
        'Please Enter Your Password: ',
        '\n'
        'You Have Successfully Logged In\n',
        'Don\'t forget to create a profile.',
        'Remember – you\'re going to want to have a job when you graduate. \n'
        'Make sure that you start to apply for jobs today!',
        '\n'
        'Menu',
        '[1] Log In',
        '[2] Create an Account',
        '[3] Search for a Job',
        '[4] Find Someone You Know',
        '[5] Learn a New Skill',
        '[6] Not Sure About InCollege? Watch this Video!',
        '[7] Useful Links',
        '[8] InCollege Important Links',
        '[9] Personal Profile',
        '[10] Show My Network',
        '[11] See Friend Requests',
        '[12] Messages',
        '[13] Exit the Program',
        'Enter your option: '
    ]