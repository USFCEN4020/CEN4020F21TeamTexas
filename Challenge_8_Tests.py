import Challenge_8
from tud_test_base import set_keyboard_input, get_display_output

# This first test will simply require a new account to have been created with the username allenda and
# password dsdas123A-, and for 7 days to NOT have ellapsed since said account has last looked for a job
# Also the account can't have a profile to have been created


def test_create_profile_message():
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


def test_setting_up_like_Allen_told_me_to_do():
    set_keyboard_input(["2", "Dylan", "Bradford", "allende", "dsdas123A-", "S", "1", "allende", "dsdas123A-",
                        "10", "1", "1", "Bradford", "1", "1", "allenda", "dsdas123A-", "11", "1", "1", "allenda",
                        "dsdas123A-", "13"])
    Challenge_8.menu()


def test_sending_a_message_from_allende_to_allenda():
    set_keyboard_input(["1", "allende", "dsdas123A-", "12", "1", "1", "I like chicken", "3", "13"])
    Challenge_8.menu()


def test_getting_notification_for_message():
    set_keyboard_input(["1", "allenda", "dsdas123A-", 13])
    Challenge_8.menu()
    output = get_display_output()
    assert output == [
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
        'Enter your option: ',
        '\n'
        'Log In',
        'Please Enter Your UserName: ',
        'Please Enter Your Password: ',
        '\n'
        'You Have Successfully Logged In\n',
        'Don\'t forget to create a profile.',
        'You have 1 new message in your inbox!\n',
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


def test_create_new_student_for_new_student_message():
    set_keyboard_input(["2", "Sammy", "Hagar", "allendi", "dsdas123A-", "S", "13"])
    Challenge_8.menu()


def test_new_student_notification():
    set_keyboard_input(["1", "allenda", "dsdas123A-", 13])
    Challenge_8.menu()
    output = get_display_output()
    assert output == [
        'You have 1 new message in your inbox!\n',
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
        'Enter your option: ',
        '\n'
        'Log In',
        'Please Enter Your UserName: ',
        'Please Enter Your Password: ',
        '\n'
        'You Have Successfully Logged In\n',
        'Don\'t forget to create a profile.',
        'New member joined: Sammy Hagar\n',
        'You have 1 new message in your inbox!\n',
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

