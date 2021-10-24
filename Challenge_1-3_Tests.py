import Challenge_6
from tud_test_base import set_keyboard_input, get_display_output


def test_create_good_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A-", "12"])
    Challenge_6.create(Challenge_6.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_non_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A-", "John", "Smith", "dasbnnud", "dasdA123-=", "12"])
    Challenge_6.create(Challenge_6.accountCount())
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_bad_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A", "dasbnnud1", "dasdA123-=", "12"])
    Challenge_6.create(Challenge_6.accountCount())
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_login_good():
    set_keyboard_input(["allenda", "dsdas123A-", "12"])
    Challenge_6.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In\n",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_login_bad():
    set_keyboard_input(["allenda", "dsdas123-", "allenda", "dsdas123A-", "12"])
    Challenge_6.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "Incorrect UserName/Password, Please Try Again",
                      "\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In\n",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_unique_log_in():
    set_keyboard_input(["John", "Smith", "allenda2", "dsdas123A-", "12"])
    Challenge_6.create(Challenge_6.accountCount())
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_create_good_non_unique_log_in():
    set_keyboard_input(["John", "Smith", "allenda", "dsdas123A-", "John", "Smith",
                        "dasbnnud2", "dasdA123-=", "12"])
    Challenge_6.create(Challenge_6.accountCount())
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_pass_non_alpha():
    assert Challenge_6.passCheck("dsadAda123") == False


def test_pass_8_char():
    assert Challenge_6.passCheck("dsad2-A") == False


def test_pass_12_char():
    assert Challenge_6.passCheck("dasbdui123abduas-Abdia") == False


def test_pass_upper():
    assert Challenge_6.passCheck("dsa12331-") == False


def test_pass_digit1():
    assert Challenge_6.passCheck("saas=A=+a=-") == False


def test_learn_skill_beta():
    set_keyboard_input(["1"])
    Challenge_6.learnSkill()
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
    set_keyboard_input(["6", "12"])
    Challenge_6.learnSkill()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
    ]


def test_menu_return():
    set_keyboard_input(["12"])
    Challenge_6.menu()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_posting_a_job_logged_in():
    set_keyboard_input(["1", "Software Engineer", "You have to develop software", "Google",
                        "California", "$80000", "5", "12"])
    Challenge_6.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "[1] Post a Job",
                      "[2] Search for a job",
                      "[3] Generate saved jobs",
                      "[4] Generate unsaved jobs",
                      "[5] Return to menu",
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
                      "[2] Search for a job",
                      "[3] Generate saved jobs",
                      "[4] Generate unsaved jobs",
                      "[5] Return to menu",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_posting_a_job_not_logged_in():
    set_keyboard_input(["1", "12"])
    Challenge_6.signedIn = False
    Challenge_6.searchJob()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_video_being_played():
    set_keyboard_input(["6", "12"])
    Challenge_6.signedIn = False
    Challenge_6.menu()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_search_for_user_successful():
    set_keyboard_input(["John", "Smith", "3", "12"])
    Challenge_6.findSomeone()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_search_for_user_failed():
    set_keyboard_input(["John", "Smithhh", "12"])
    Challenge_6.findSomeone()
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]


def test_copyright_notice():  # SPRINT3
    set_keyboard_input(["1", "10", "12"])
    Challenge_6.ImportantLinks()
    output = get_display_output()
    assert output == ["\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "\n"
                      "Copyright Notice\n"
                      "\nThis application and its content is copyright of InCollege. Any redistribution or \n"
                      "reproduction of part or all of the contents in any form is prohibited. You may not, \n"
                      "distribute or commercially exploit the content. Nor may you transmit or store it in any \n"
                      "other website or other form of electronic retrieval system.\n"
                      "\nIf you notice any of copyright infringement please notify us at copyright@InCollege.com\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_about_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.about()
    output = get_display_output()
    assert output == ["\nAbout InCollege\n\n"
                      "InCollege is an online application that has been designed exclusively for college \n"
                      "students. Searching for a first job can be challenging, but InCollege provides \n"
                      "tools that are needed in order to be successful. This service allows students at \n"
                      "various universities to network and exchange information about school, jobs, \n"
                      "salaries, offers, and projects.\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_accessibility_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.accessibility()
    output = get_display_output()
    assert output == ["\nAccessibility\n\n"
                      "InCollege is a place for college students to connect and find opportunities"
                      " in the workforce. \n\nWe’re here to help you succeed with any goals, ideas, or "
                      "ambitions that you want to carry out. "
                      "\n\nWith a diverse collection of InCollege members, accessibility is a major key \n"
                      "for establishing a great community. Our aim is to design products, services, \n"
                      "and environments for people for people who experience disabilities. We wish \n"
                      "to identify, remove, and prevent barriers that would make it difficult for students \n"
                      "to interact with the InCollege application.\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_copyrightpolicy_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.copyRightPolicy()
    output = get_display_output()
    assert output == ["\nCopyright Policy\n\n"
                      "InCollege respects the intellectual property rights of others and expects its \n"
                      "users to do the same. It is InCollege’s policy to remove or terminate any users \n"
                      "who repeatedly infringe or charged with infringing the copyrights or other intellectual \n"
                      "property rights of others. Information posted by members should be accurate, lawful, \n"
                      "and not in violation of any U.S copyright laws. Any complaints regarding copyright \n"
                      "infringement can be handled in copyright notice.\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_cookiepolicy_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.cookiePolicy()
    output = get_display_output()
    assert output == ["\nCookie Policy\n\n"
                      "By using InCollege, you consent to the use of cookies.\n\n"
                      "Cookies are small blocks of data sent from web browser by the website you are on. A \n"
                      "cookie file allows the InCollege or a third-party to recognize you and make your next \n"
                      "visit easier.\n\n"
                      "Cookies are used to enable certain functions of InCollege, provide analytics, store \n"
                      "preferences and enable advertisement delivery. Essential cookies authenticate users \n"
                      "and prevent fraudulent use of user accounts. \n\n"
                      "Third – party cookies are used to report usage statistics and deliver advertisement \n"
                      "for InCollege.\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_copyrightnotice_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.copyRightPolicy()
    output = get_display_output()
    assert output == ["\nCopyright Policy\n\n"
                      "InCollege respects the intellectual property rights of others and expects its \n"
                      "users to do the same. It is InCollege’s policy to remove or terminate any users \n"
                      "who repeatedly infringe or charged with infringing the copyrights or other intellectual \n"
                      "property rights of others. Information posted by members should be accurate, lawful, \n"
                      "and not in violation of any U.S copyright laws. Any complaints regarding copyright \n"
                      "infringement can be handled in copyright notice.\n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_brandpolicy_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.brandPolicy()
    output = get_display_output()
    assert output == ["\nBrand Policy\n\n"
                      "Any trademarks and brand features are protected by law. You’ll need InCollege’s \n"
                      "consent in order to use them. \n\n"
                      "InCollege does not permit its members, third party developers, partners and the media \n"
                      "to use its name, trademarks, logos, web pages, screenshots and other brand features. \n",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_importantLinks_notice():  # SPRINT3
    set_keyboard_input(["10", "12"])
    Challenge_6.ImportantLinks()
    output = get_display_output()
    assert output == ["\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
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
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "

                      ]


def test_privacypolicy_signedin_notice():  # SPRINT3
    set_keyboard_input(["allenda", "dsdas123A-", "8", "5", "4", "10", "12"])
    Challenge_6.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In\n",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: ",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "\nPrivacy Policy\n\n"
                      "Personal information is only processed with your consent, or on another legal basis. \n"
                      "In addition, privacy settings can be changed by any signed-in user to meet specific needs.\n",
                      "\nGuest Controls",
                      "[1] Toggle Email notifications",
                      "[2] Toggle SMS notifications",
                      "[3] Toggle Targeted Advertising features",
                      "[4] Return to previous",
                      "Choose an option: ",
                      "Returning...",
                      "\nImportant Links",
                      "[1] Copyright Notice",
                      "[2] About",
                      "[3] Accessibility",
                      "[4] User Agreement",
                      "[5] Privacy Policy",
                      "[6] Cookie Policy",
                      "[7] Copyright Policy",
                      "[8] Brand Policy",
                      "[9] Languages",
                      "[10] Return to previous",
                      "Choose an option: ",
                      "Returning...",
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]

