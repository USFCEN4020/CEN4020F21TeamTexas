import Challenge_7
from tud_test_base import set_keyboard_input, get_display_output


# Challenge 5
# Create an account must be ran first before attempting any of the test cases
def test_create_ten_accounts_5():
    set_keyboard_input(["James", "Johnson", "James11!", "Johnson11!", "S", "2",
                        "Daniel", "Jones", "Daniel11!", "Jones11!", "S", "2",
                        "Charles", "Smith", "Charles11!", "Smith11!", "S", "2",
                        "David", "Miller", "David11!", "Miller11!", "S", "2",
                        "Richard", "Jackson", "Richard11!", "Jackson11!", "S", "2",
                        "Mark", "Thomas", "Mark11!", "Thomas11!", "S", "2",
                        "Harry", "Lewis", "Harry11!", "Lewis11!", "S", "2",
                        "Matt", "Harris", "Matt11!", "Harris11!", "S", "2",
                        "Eddie", "Williams", "Eddie11!", "Williams11!", "S", "2",
                        "John", "Smith", "JohnS11!", "Spider11!", "S", "13"])
    Challenge_7.create(Challenge_7.accountCount())
    assert Challenge_7.accountCount() == 10


# Challenge 5
# Test to make sure up to 10 accounts can be created
def test_maximum_accounts_number_5():
    set_keyboard_input(["13"])
    Challenge_7.create(Challenge_7.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "\nAll permitted accounts have been created, please come back later.",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "
                      ]


# Challenge 5
# Every student will have a list of friends on InCollege that they
# have connected with. Initially this list will be empty.
def test_friends_list_for_each_account():
    count = 0
    with open("list_of_friends.txt") as a_file:
        for line in a_file:
            if line != "\n":
                count += 1

    assert count == 10


# Challenge 5
# Students will be able to search for students in the system by last name.
# When results of these searches are displayed, the student will have the option
# of sending that student a request to connect.
def test_search_name_and_add_friend_5():
    set_keyboard_input(["Daniel11!", "Jones11!", "10", "1", "1",
                        "Lewis", "1", "13"])
    Challenge_7.login()
    with open("friend_requests.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "Harry11!":
                assert stripped_line[1] == "Daniel11!:s"


# In the experience section, students will be able to enter information on up to three past jobs.
# Previous experience will include a title, an employer, date started, date ended, location, and
# then a description of what they did.
def test_experience_profile():
    set_keyboard_input(["1", "5", "1", "Code Developer", "Disney", "11/16/19",
                        "03/19/20", "Florida", "Help Design And Develop Code", "2",
                        "Code Tester", "Intel", "04/20/20", "10/06/20", "Florida",
                        "Test Code For Big Projects", "3", "Data Scientist", "Amazon",
                        "12/14/20", "06/16/21", "Florida", "Analyze Data", "4",
                        "7", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[12] == "Title: Code Developer"
                assert stripped_line[13] == "Employer: Disney"
                assert stripped_line[14] == "Start Date: 11/16/19"
                assert stripped_line[15] == "End Date: 03/19/20"
                assert stripped_line[16] == "Job Location: Florida"
                assert stripped_line[17] == "Description: Help Design And Develop Code"
                assert stripped_line[18] == "Title: Code Tester"
                assert stripped_line[19] == "Employer: Intel"
                assert stripped_line[20] == "Start Date: 04/20/20"
                assert stripped_line[21] == "End Date: 10/06/20"
                assert stripped_line[22] == "Job Location: Florida"
                assert stripped_line[23] == "Description: Test Code For Big Projects"
                assert stripped_line[24] == "Title: Data Scientist"
                assert stripped_line[25] == "Employer: Amazon"
                assert stripped_line[26] == "Start Date: 12/14/20"
                assert stripped_line[27] == "End Date: 06/16/21"
                assert stripped_line[28] == "Job Location: Florida"
                assert stripped_line[29] == "Description: Analyze Data"


# User will be able to enter a major. The major will be converted to a word that starts with an
# uppercase letter and the rest is lower case. Multiple words in the major will all start with
# an upper case letter no matter how the student entered it. The same formatting will be used
# for the names of universities.
def test_major_profile():
    set_keyboard_input(["1", "2", "computer science", "7", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[9] == "Computer Science"


# Students will be able to enter a paragraph of text for their About section.
def test_about_profile():
    set_keyboard_input(["1", "4", "I am currently a student at the University of South Florida. "
                             "Some programming languages that I am familiar with are Python "
                             "and Java. I have been involved in many projects for Disney. I "
                             "worked as a programmer to write functioning software.", "7", "3", "13"])

    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[11] == "I am currently a student at the University of South Florida. " \
                                            "Some programming languages that I am familiar with are Python " \
                                            "and Java. I have been involved in many projects for Disney. I " \
                                            "worked as a programmer to write functioning software."


# When the student is creating their profile they will be able to enter a title (line of text) for
# the profile (e.g. "3rd year Computer Science student")
def test_title_profile():
    set_keyboard_input(["1", "1", "3rd Year Computer Science Student", "7", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[8] == "3rd Year Computer Science Student"


# Students will be able to enter an education section that will include school name, degree, and years attended.
def test_education_section():
    set_keyboard_input(["1", "6", "University Of South Florida", "Computer Science",
                        "3", "7", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[30] == "School: University Of South Florida"
                assert stripped_line[31] == "Degree: Computer Science"
                assert stripped_line[32] == "Years: 3"


# Profiles can be created for a user, consisting of a title, a major, a university name, a paragraph with
# information regarding the student, zero or more lines about their experience, and 1 or more lines about
# their education. After entering their profile information, the student will be able to view their profile.
# When their profile is displayed, their name will be automatically be displayed at the top of the profile
# information.
def test_create_and_view_profile():
    set_keyboard_input(["1", "1", "3rd Year Computer Science Student",
                        "2", "Computer Science", "3", "South Florida",
                        "4", "I am currently a student at the University of South Florida. "
                             "Some programming languages that I am familiar with are Python "
                             "and Java. I have been involved in many projects for Disney. I "
                             "worked as a programmer to write functioning software.", "5",
                        "1", "Code Developer", "Disney", "11/16/19", "03/19/20", "Florida",
                        "Help Design And Develop Code", "4", "6", "University Of South Florida",
                        "Computer Science", "3", "7", "2", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    output = get_display_output()
    assert output == ["Profile",
                      "[1] Edit Profile",
                      "[2] View Profile",
                      "[3] Return to menu",
                      "Choose an option: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter a title: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter a major: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter a University: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter an About: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter information about your past jobs, up to three past jobs",
                      "[1] Job 1",
                      "[2] Job 2",
                      "[3] Job 3",
                      "[4] Return to previous",
                      "Choose an option: ",
                      "Enter information about your past jobs here",
                      "Enter the job title: ",
                      "Enter the employer of the job: ",
                      "Enter the start date of the job: ",
                      "Enter the end date of the job: ",
                      "Enter the location of the job: ",
                      "Enter a description of the job: ",
                      "Enter information about your past jobs, up to three past jobs",
                      "[1] Job 1",
                      "[2] Job 2",
                      "[3] Job 3",
                      "[4] Return to previous",
                      "Choose an option: ",
                      "Returning...",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Enter information about your education here",
                      "Enter school name: ",
                      "Enter your degree: ",
                      "Enter how many years attended: ",
                      "[1] Title",
                      "[2] Major",
                      "[3] University Name",
                      "[4] About",
                      "[5] Work experience",
                      "[6] Education",
                      "[7] Return to previous",
                      "Choose an option: ",
                      "Returning...",
                      "Profile",
                      "[1] Edit Profile",
                      "[2] View Profile",
                      "[3] Return to menu",
                      "Choose an option: ",
                      # ----------------------------- View profile
                      "\nJohn Smith",
                      "Title: 3rd Year Computer Science Student",
                      "Major: Computer Science",
                      "University: South Florida",
                      "About: I am currently a student at the University of South Florida. "
                      "Some programming languages that I am familiar with are Python "
                      "and Java. I have been involved in many projects for Disney. I "
                      "worked as a programmer to write functioning software.",
                      "\nJob Experience1",
                      "Title: Code Developer",
                      "Employer: Disney",
                      "Start Date: 11/16/19",
                      "End Date: 03/19/20",
                      "Job Location: Florida",
                      "Description: Help Design And Develop Code",
                      "\nJob Experience2",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Job Location: None",
                      "Description: None",
                      "\nJob Experience3",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Job Location: None",
                      "Description: None",
                      "\nEducation",
                      "School: University Of South Florida",
                      "Degree: Computer Science",
                      "Years: 3\n",
                      "Profile",
                      "[1] Edit Profile",
                      "[2] View Profile",
                      "[3] Return to menu",
                      "Choose an option: ",
                      "Returning to menu...",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]


# Students will be able to enter just part of a profile and then quit, then be allowed can come back
# and complete the entering of the rest of their profile.
def test_create_profile_in_increments():
    set_keyboard_input(["1", "1", "3rd Year Computer Science Student", "7", "3", "9", "1",
                        "2", "Computer Science", "7", "3", "9", "1", "3", "South Florida",
                        "7", "3", "9", "1", "4", "I am currently a student at the University of South Florida. "
                             "Some programming languages that I am familiar with are Python "
                             "and Java. I have been involved in many projects for Disney. I "
                             "worked as a programmer to write functioning software.", "7", "3", "9", "1", "5",
                        "1", "Code Developer", "Disney", "11/16/19", "03/19/20", "Florida",
                        "Help Design And Develop Code", "4", "7", "3", "9", "1", "6", "University Of South Florida",
                        "Computer Science", "3", "7", "2", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            temp = stripped_line.split("\t")
            if temp[3] == "Spider11!":
                assert stripped_line == "John	Smith	JohnS11!	Spider11!	On	On	On	" \
                                        "English	3rd Year Computer Science Student	Computer Science	" \
                                        "South Florida	I am currently a student at the University of South Florida. " \
                                        "Some programming languages that I am familiar with are Python and Java. " \
                                        "I have been involved in many projects for Disney. I worked as a programmer " \
                                        "to write functioning software.	Title: Code Developer	" \
                                        "Employer: Disney	Start Date: 11/16/19	End Date: 03/19/20	" \
                                        "Job Location: Florida	Description: Help Design And Develop Code	" \
                                        "Title: None	Employer: None	Start Date: None	End Date: None	" \
                                        "Job Location: None	Description: None	Title: None	Employer: None	" \
                                        "Start Date: None	End Date: None	Job Location: None	Description: None	" \
                                        "School: University Of South Florida	Degree: Computer Science	Years: 3"


# Students can come back and replace a part of the profile with new information if they so choose to do so.
def test_edit_profile():
    set_keyboard_input(["1", "1", "3rd Year Computer Science Student",
                        "2", "Computer Science", "3", "South Florida",
                        "4", "I am currently a student at the University of South Florida. "
                             "Some programming languages that I am familiar with are Python "
                             "and Java. I have been involved in many projects for Disney. I "
                             "worked as a programmer to write functioning software.", "5",
                        "1", "Code Developer", "Disney", "11/16/19", "03/19/20", "Florida",
                        "Help Design And Develop Code", "4", "6", "University Of South Florida",
                        "Computer Science", "3", "7", "3", "9", "1", "1",
                        "4th Year Computer Engineering Student", "2", "Computer Engineering",
                        "3", "Florida State", "4", "I am currently a student at Florida State University. "
                        "Some programming languages that I am familiar with are Python "
                        "and Java. I have been involved in many projects for Intel. I "
                        "worked as a tester for testing functioning software.", "5",
                        "1", "Code Tester", "Intel", "04/20/20", "10/06/20", "Florida",
                        "Test Code For Big Projects", "4", "6", "Florida State University",
                        "Computer Engineering", "4", "7", "3", "13"])
    Challenge_7.signedIn = True
    Challenge_7.current_Name = "John Smith"
    Challenge_7.firstName = "John"
    Challenge_7.lastName = "Smith"
    Challenge_7.userName = "JohnS11!"
    Challenge_7.password = "Spider11!"
    Challenge_7.emailOpt = "On"
    Challenge_7.smsOpt = "On"
    Challenge_7.advOpt = "On"
    Challenge_7.languageOpt = "English"
    Challenge_7.titleOpt = "None"
    Challenge_7.majorOpt = "None"
    Challenge_7.UniOpt = "None"
    Challenge_7.aboutOpt = "None"
    Challenge_7.expOpt1Title = "Title: None"
    Challenge_7.expOpt1Emp = "Employer: None"
    Challenge_7.expOpt1Start = "Start Date: None"
    Challenge_7.expOpt1End = "End Date: None"
    Challenge_7.expOpt1Loc = "Job Location: None"
    Challenge_7.expOpt1Des = "Description: None"
    Challenge_7.expOpt2Title = "Title: None"
    Challenge_7.expOpt2Emp = "Employer: None"
    Challenge_7.expOpt2Start = "Start Date: None"
    Challenge_7.expOpt2End = "End Date: None"
    Challenge_7.expOpt2Loc = "Job Location: None"
    Challenge_7.expOpt2Des = "Description: None"
    Challenge_7.expOpt3Title = "Title: None"
    Challenge_7.expOpt3Emp = "Employer: None"
    Challenge_7.expOpt3Start = "Start Date: None"
    Challenge_7.expOpt3End = "End Date: None"
    Challenge_7.expOpt3Des = "Description: None"
    Challenge_7.expOpt3Loc = "Job Location: None"
    Challenge_7.eduOptSchool = "School: None"
    Challenge_7.eduOptDegree = "Degree: None"
    Challenge_7.eduOptYears = "Years: None"
    Challenge_7.variable = 0

    Challenge_7.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            temp = stripped_line.split("\t")
            if temp[3] == "Spider11!":
                assert stripped_line == "John\tSmith\tJohnS11!\tSpider11!\tOn\tOn\tOn\tEnglish	" \
                                        "4th Year Computer Engineering Student	Computer Engineering	" \
                                        "Florida State	I am currently a student at Florida State University. " \
                                        "Some programming languages that I am familiar with are Python and Java. " \
                                        "I have been involved in many projects for Intel. I worked as a tester " \
                                        "for testing functioning software.	" \
                                        "Title: Code Tester	Employer: Intel	Start Date: 04/20/20	End Date: 10/06/20	" \
                                        "Job Location: Florida	Description: Test Code For Big Projects	" \
                                        "Title: None	Employer: None	Start Date: None	End Date: None	" \
                                        "Job Location: None	Description: None	Title: None	Employer: None	" \
                                        "Start Date: None	End Date: None	Job Location: None	Description: None	" \
                                        "School: Florida State University	Degree: Computer Engineering	Years: 4"


# Challenge 5
# Students will be able to search for students in the system by university.
# When results of these searches are displayed, the student will have the option of
# sending that student a request to connect.
def test_search_university_and_add_friend_5():
    set_keyboard_input(["Daniel11!", "Jones11!", "10", "1", "2",
                        "Florida State University", "1", "13"])
    Challenge_7.login()
    with open("friend_requests.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "JohnS11!":
                assert stripped_line[1] == "Daniel11!:s"


# Challenge 5
# Students will be able to search for students in the system by major.
# When results of these searches are displayed, the student will have the option of
# sending that student a request to connect.
def test_search_major_and_add_friend_5():
    set_keyboard_input(["Mark11!", "Thomas11!", "10", "1", "3",
                        "Computer Engineering", "1", "13"])
    Challenge_7.login()
    with open("friend_requests.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "JohnS11!":
                assert stripped_line[2] == "Mark11!:s"


# Challenge 5
# The next time that that student logs in, they will be informed
# that they have a pending friend request. They can accept the friend request.
def test_login_and_accept_request():
    set_keyboard_input(["Harry11!", "Lewis11!", "11", "1", "13"])
    Challenge_7.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In\n",
                      "You have 1 pending friend request!\n",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThese are your friend requests!\n",
                      "You have a friend request from Daniel11!\n",
                      "What do you want to do?\n",
                      "[1] Accept",
                      "[2] Reject",
                      "[3] Ignore\n",
                      "Enter Your Option: ",
                      "Daniel11! is now your new friend!\n",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]

    with open("list_of_friends.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "Daniel11!":
                assert stripped_line[1] == "Harry11!"
            elif stripped_line[0] == "Harry11!":
                assert stripped_line[1] == "Daniel11!"


# Challenge 5
# The next time that that student logs in, they will be informed
# that they have a pending friend request. They can reject the friend request.
# Each student will be able to generate a list of their pending friend requests.
def test_login_and_reject_friends():
    set_keyboard_input(["JohnS11!", "Spider11!", "11", "2", "2", "13"])
    Challenge_7.login()
    output = get_display_output()
    assert output == ["\nLog In",
                      "Please Enter Your UserName: ",
                      "Please Enter Your Password: ",
                      "\nYou Have Successfully Logged In\n",
                      "You have 2 pending friends requests!",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThese are your friend requests!\n",
                      "You have a friend request from Daniel11!\n",
                      "What do you want to do?\n",
                      "[1] Accept",
                      "[2] Reject",
                      "[3] Ignore\n",
                      "Enter Your Option: ",
                      "You have a friend request from Mark11!\n",
                      "What do you want to do?\n",
                      "[1] Accept",
                      "[2] Reject",
                      "[3] Ignore\n",
                      "Enter Your Option: ",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]

    with open("friend_requests.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "JohnS11!":
                assert stripped_line[1] == "Daniel11!:r"
                assert stripped_line[2] == "Mark11!:r"


# Challenge 5
# A new "show my network"option will be added that will present the user with a
# list of the people that they have connected with (including none).
def test_view_friend_list():
    set_keyboard_input(["Daniel11!", "Jones11!", "10", "4", "13"])
    Challenge_7.login()
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThis is your list of friends!\n",
                      "- Harry11!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]


# Challenge 5
# The next time that that student logs in, they will be informed
# that they have a pending friend request. They can accept the friend request.
# If they accept it, then the person who sent it will be added to their list of friends.
# The person who sent the request will also have this student added to their list of friends.
def test_send_accept_friend_request():
    set_keyboard_input(["Daniel11!", "Jones11!", "10", "1", "2",
                        "Florida State University", "1", "1", "JohnS11!",
                        "Spider11!", "11", "1", "13"])
    Challenge_7.login()

    with open("list_of_friends.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(",")
            if stripped_line[0] == "JohnS11!":
                assert stripped_line[1] == "Daniel11!"
            elif stripped_line[0] == "Daniel11!":
                assert stripped_line[2] == "JohnS11!"


# Challenge 5
# Students will be able to display the profile of any student that they have a friend relationship with.
# They will be able to do this by displaying a list of people that
# they are friends with and then selecting the "profile" option that is by a
# friend's name. When they do this, the friend's profile will be displayed.
def test_view_friend_profile():
    set_keyboard_input(["Daniel11!", "Jones11!", "10", "3", "JohnS11!", "4", "13"])
    Challenge_7.login()
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThis is your list of friends!\n",
                      "- Harry11!",
                      "- JohnS11!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
                      "Type the user you want to see the profile: ",
                      "\n John Smith",
                      "Title: 4th Year Computer Engineering Student",
                      "Major: Computer Engineering",
                      "University: Florida State",
                      "About: I am currently a student at Florida State University. Some "
                      "programming languages that I am familiar with are Python and Java. I have "
                      "been involved in many projects for Intel. I worked as a tester for testing "
                      "functioning software.",
                      "\nJob Experience1",
                      "Title: Code Tester",
                      "Employer: Intel",
                      "Start Date: 04/20/20",
                      "End Date: 10/06/20",
                      "Job Location: Florida",
                      "Description: Test Code For Big Projects",
                      "\nJob Experience2",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Job Location: None",
                      "Description: None",
                      "\nJob Experience3",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Job Location: None",
                      "Description: None",
                      "\nEducation",
                      "School: Florida State University",
                      "Degree: Computer Engineering",
                      "Years: 4\n",
                      "\nThis is your list of friends!\n",
                      "- Harry11!",
                      "- JohnS11!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]


# Challenge 5
# If the friend does not currently have a profile created,
# then the profile option will not be displayed by that friend's name.
def test_view_friend_with_no_profile():
    set_keyboard_input(["Harry11!", "Lewis11!", "10", "3", "Daniel11!", "4", "13"])
    Challenge_7.login()
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThis is your list of friends!\n",
                      "- Daniel11!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
                      "Type the user you want to see the profile: ",
                      "You can not see this profile because Daniel11! has not created a profile yet!",
                      "\nThis is your list of friends!\n",
                      "- Daniel11!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]


# Challenge 5
# The number of friends that that friend has will not be displayed.
# If they don't have a friend relationship with someone, they won't be able
# to see that person's profile information.
def test_view_profile_of_not_friend():
    set_keyboard_input(["Matt11!", "Harris11!", "10", "3", "Eddie11!", "4", "13"])
    Challenge_7.login()
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: ",
                      "\nThis is your list of friends!\n",
                      "\n What do you want to do now?",
                      "   [1] Add a friend!",
                      "   [2] Disconnect with a friend",
                      "   [3] See profile of a friend",
                      "   [4] Go back to menu\n",
                      "Enter Your Option: ",
                      "Type the user you want to see the profile: ",
                      "This user is not in your network or does not exist!\n"
                      "You can not see this profile.",
                      "Enter Your Option: ",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "]


# Challenge 5
# They will have the option of disconnecting from any of the listed people. 
# If they disconnect from someone, the person will be removed from their 
# list of friends and they will be removed from the other person's list of friends.
def test_disconnect():
    set_keyboard_input(["Harry11!", "Lewis11!", "10", "2", "Daniel11!",
                        "4", "13"])
    Challenge_7.login()
    with open("list_of_friends.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if stripped_line == "Harry11!":
                assert stripped_line == "Harry11!"  # Their friend line will only have themself
            if stripped_line == "Daniel11!,JohnS11!":
                assert stripped_line == "Daniel11!,JohnS11!"
