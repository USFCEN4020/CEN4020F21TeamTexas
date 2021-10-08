import Challenge_3
from tud_test_base import set_keyboard_input, get_display_output


def test_create_good_unique_non_log_in():
    set_keyboard_input(["2", "John", "Smith", "allenda", "dsdas123A-", "9"])
    Challenge_3.signedIn = False
    Challenge_3.menu()
    # Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: ",
                      "\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "\nAccount Created.\nNow You Can Log-In!",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_non_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A-", "John", "Smith", "dasbnnud", "dasdA123-=", "9"])
    Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "Username Already Exists, Please Try Again.",
                      "\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "\nAccount Created.\nNow You Can Log-In!",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_bad_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A", "dasbnnud1", "dasdA123-=", "9"])
    Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "The password should have at least one non-alpha character.",
                      "Please Input a UserName: ",
                      "Please Input a Password: ",
                      "\nAccount Created.\nNow You Can Log-In!",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_login_good():
    set_keyboard_input(["allenda", "dsdas123A-", "9"])
    Challenge_3.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_login_bad():
    set_keyboard_input(["allenda", "dsdas123-", "allenda", "dsdas123A-", "9"])
    Challenge_3.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "Incorrect UserName/Password, Please Try Again",
                      "\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_unique_log_in():
    set_keyboard_input(["John", "Smith", "allenda2", "dsdas123A-", "9"])
    Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "\nAccount Created.\nNow You Can Log-In!",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_non_unique_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A-", "John", "Smith",
                        "dasbnnud2", "dasdA123-=", "9"])
    Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "Username Already Exists, Please Try Again.",
                      "\nCreate A Account",
                      "First Name: ",
                      "Last Name: ",
                      "Username: ",
                      "Password: ",
                      "\nAccount Created.\nNow You Can Log-In!",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_maximum_accounts_number():
    set_keyboard_input(["9"])
    Challenge_3.create(Challenge_3.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "\nAll permitted accounts have been created, please come back later.",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_pass_non_alpha():
    assert Challenge_3.passCheck("dsadAda123") == False


def test_pass_8_char():
    assert Challenge_3.passCheck("dsad2-A") == False


def test_pass_12_char():
    assert Challenge_3.passCheck("dasbdui123abduas-Abdia") == False


def test_pass_upper():
    assert Challenge_3.passCheck("dsa12331-") == False


def test_pass_digit1():
    assert Challenge_3.passCheck("saas=A=+a=-") == False


def test_learn_skill_beta():
    set_keyboard_input(["1"])
    Challenge_3.learnSkill()
    output = get_display_output()
    assert output == ["\nLearn a New Skill",
                      "[1] Learn ...",
                      "[2] Learn ...",
                      "[3] Learn ...",
                      "[4] Learn ...",
                      "[5] Learn ...",
                      "[6] Return",
                      "Choose What You Want to Learn: ",
                      "Under Construction."
                      ]


def test_learn_skill_return():
    set_keyboard_input(["6", "9"])
    Challenge_3.learnSkill()
    output = get_display_output()
    assert output == ["\nLearn a New Skill",
                      "[1] Learn ...",
                      "[2] Learn ...",
                      "[3] Learn ...",
                      "[4] Learn ...",
                      "[5] Learn ...",
                      "[6] Return",
                      "Choose What You Want to Learn: ",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
    ]


def test_menu_return():
    set_keyboard_input(["9"])
    Challenge_3.menu()
    output = get_display_output()
    assert output == ["\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_posting_a_job_logged_in():
    set_keyboard_input(["1", "Software Engineer", "You have to develop software", "Google",
                        "California", "$80000", "2", "9"])
    Challenge_3.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "[1] Post a Job",
                      "[2] Return to menu",
                      "Enter Your Option: ",
                      "\nPost a Job!",
                      "Enter a Title: ",
                      "Enter a Description: ",
                      "Enter an Employer: ",
                      "Enter a Location: ",
                      "Enter a Salary: ",
                      "Job Posted!",
                      "\nSearch for a Job",
                      "[1] Post a Job",
                      "[2] Return to menu",
                      "Enter Your Option: ",
                      "Returning to Menu",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_posting_a_job_not_logged_in():
    set_keyboard_input(["1", "9"])
    Challenge_3.signedIn = False
    Challenge_3.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "[1] Return to Options",
                      "Enter Your Option: ",
                      "Returning to Menu",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_video_being_played():
    set_keyboard_input(["6", "9"])
    Challenge_3.signedIn = False
    Challenge_3.menu()
    output = get_display_output()
    assert output == ["\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: ",
                      "Video is now playing",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_search_for_user_successful():
    set_keyboard_input(["John", "Smith", "3", "9"])
    Challenge_3.findSomeone()
    output = get_display_output()
    assert output == ["\nFind Someone You Know",
                      "Enter Their First Name: ",
                      "Enter Their Last Name: ",
                      "They are a part of the InCollege system!",
                      "[1] Log In",
                      "[2] Sign Up to Join Friend",
                      "[3] Return to Options",
                      "Please Select an Option: ",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]


def test_search_for_user_failed():
    set_keyboard_input(["John", "Smithhh", "9"])
    Challenge_3.findSomeone()
    output = get_display_output()
    assert output == ["\nFind Someone You Know",
                      "Enter Their First Name: ",
                      "Enter Their Last Name: ",
                      "They are not yet a part of the InCollege system yet!",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Exit the Program",
                      "Enter your option: "
                      ]
