import Challenge_8
from tud_test_base import set_keyboard_input, get_display_output
# This file expects three users, bradfordd, bradforda, plusmember
# bradfordd and bradforda are standard members that are friends with each other
# plusmember is a premium member


def test_send_Message_to_friends_mailbox():
    set_keyboard_input(["1", "I like pie", "3", "13"])
    Challenge_8.userName = "bradfordd"
    Challenge_8.subscription = "S"
    Challenge_8.sendMessage()
    output = get_display_output()
    assert output == ['S',
                      '\n'
                      'Send A Message!',
                      '\n'
                      'This is your list of friends!\n',
                      '1. bradforda\n',
                      '\n'
                      "Enter number corresponding with the student you'd like to send a message "
                      'to: ',
                      'Enter Message: '
                      ]


def test_view_and_delete_message():
    set_keyboard_input(["1", "2", "3", "13"])
    Challenge_8.userName = "bradforda"
    Challenge_8.subscription = "S"
    Challenge_8.viewMessages();
    output = get_display_output()
    assert output == [
                        '\n'
                        'Here are all your messages.',
                        'Messages with a * are New.',
                        '1. bradfordd*',
                        'Enter number option: ',
                        '\n'
                        'From: bradfordd\n'
                        'I like pie',
                        '\n'
                        '[1] Return To Messages Page',
                        '[2] Delete Message',
                        '[3] Reply to Message',
                        'Enter Option: ',
                      ]


def test_create_an_account_with_premium_account():
    set_keyboard_input(["2", "Not", "AName", "allenda", "dsdas123A-", "P", "13"])
    Challenge_8.menu()
    output = get_display_output()
    assert output == ['\nWant to hear what students have to say about InCollege?',
                      '\nRead about how InCollege helped Ethan Timor:',
                       '\t "I was never able to land an interview or internship in college. ',
                       "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                       '\t Within days, I had interviews, and offers from companies like:',
                       '\t Tesla, Microsoft, Google, and Apple',
                       '\t I was able to graduate and find a starting job as the lead Senior VP of '
                       'Programming at NASA.',
                       '\t It would not be possible without InCollege."',
                       '\nMenu',
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
                       '\nCreate A Account',
                       'First Name: ',
                       'Last Name: ',
                       'Username: ',
                       'Password: ',
                      'Input S for Standard or P for Plus Membership: ',
                       '\nAccount Created.\nNow You Can Log-In!',
                       '\nWant to hear what students have to say about InCollege?',
                       '\nRead about how InCollege helped Ethan Timor:',
                       '\t "I was never able to land an interview or internship in college. ',
                       "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                       '\t Within days, I had interviews, and offers from companies like:',
                       '\t Tesla, Microsoft, Google, and Apple',
                       '\t I was able to graduate and find a starting job as the lead Senior VP of '
                       'Programming at NASA.',
                       '\t It would not be possible without InCollege."',
                       '\nMenu',
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


def test_send_messages_to_all_with_premium_account():
    set_keyboard_input(["1", "I like pie", "3", "13"])
    Challenge_8.userName = "plusmember"
    Challenge_8.subscription = "P"
    output = get_display_output()
    Challenge_8.sendMessage()
    output = get_display_output()
    assert output == [ 'P',
                       '\n'
                       'Send A Message!',
                       '\n'
                       'This is a list of InCollege students!\n',
                       '1. bradfordd',
                       '2. bradforda',
                       '3. allenda',
                       '\n'
                       "Enter number corresponding with the student you'd like to send a message "
                       'to: ',
                       'Enter Message: ',
                       ]


def test_view_and_delete_message_from_premium_account():
    set_keyboard_input(["1", "3", "Stop talking to me, you aren't my friend!", "3", "13"])
    Challenge_8.userName = "bradfordd"
    Challenge_8.subscription = "S"
    Challenge_8.viewMessages();
    output = get_display_output()
    assert output == ['\nHere are all your messages.',
                      'Messages with a * are New.',
                      '1. plusmember*',
                      'Enter number option: ',
                      '\n'
                      'From: plusmember\n'
                      'I like pie',
                      '\n'
                      '[1] Return To Messages Page',
                      '[2] Delete Message',
                      '[3] Reply to Message',
                      'Enter Option: ',
                      '\n'
                      'Enter Reply Message: '
                      ]