import Challenge_4
from tud_test_base import set_keyboard_input, get_display_output


# Create an account must be ran first before attempting any of the test cases
def test_create_good_unique_non_log_in():
    set_keyboard_input(["John", "Smith", "JohnS11!", "Spider11!", "10"])
    Challenge_4.create(Challenge_4.accountCount())
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
                      "[10] Exit the Program",
                      "Enter your option: "
                      ]


# In the experience section, students will be able to enter information on up to three past jobs.
# Previous experience will include a title, an employer, date started, date ended, location, and
# then a description of what they did.
def test_experience_profile():
    set_keyboard_input(["1", "5", "1", "Code Developer", "Disney", "11/16/19",
                        "03/19/20", "Florida", "Help Design And Develop Code", "2",
                        "Code Tester", "Intel", "04/20/20", "10/06/20", "Florida",
                        "Test Code For Big Projects", "3", "Data Scientist", "Amazon",
                        "12/14/20", "06/16/21", "Florida", "Analyze Data", "4",
                        "7", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
    set_keyboard_input(["1", "2", "computer science", "7", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
                             "worked as a programmer to write functioning software.", "7", "3", "10"])

    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
    set_keyboard_input(["1", "1", "3rd Year Computer Science Student", "7", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
    with open("login.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().split("\t")
            if stripped_line[3] == "Spider11!":
                assert stripped_line[8] == "3rd Year Computer Science Student"


# Students will be able to enter an education section that will include school name, degree, and years attended.
def test_education_section():
    set_keyboard_input(["1", "6", "University Of South Florida", "Computer Science",
                        "3", "7", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
                        "Computer Science", "3", "7", "2", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
                      "[10] Exit the Program",
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
                        "Computer Science", "3", "7", "2", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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
                        "Computer Engineering", "4", "7", "3", "10"])
    Challenge_4.signedIn = True
    Challenge_4.current_Name = "John Smith"
    Challenge_4.firstName = "John"
    Challenge_4.lastName = "Smith"
    Challenge_4.userName = "JohnS11!"
    Challenge_4.password = "Spider11!"
    Challenge_4.emailOpt = "On"
    Challenge_4.smsOpt = "On"
    Challenge_4.advOpt = "On"
    Challenge_4.languageOpt = "English"
    Challenge_4.titleOpt = "None"
    Challenge_4.majorOpt = "None"
    Challenge_4.UniOpt = "None"
    Challenge_4.aboutOpt = "None"
    Challenge_4.expOpt1Title = "Title: None"
    Challenge_4.expOpt1Emp = "Employer: None"
    Challenge_4.expOpt1Start = "Start Date: None"
    Challenge_4.expOpt1End = "End Date: None"
    Challenge_4.expOpt1Loc = "Job Location: None"
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Loc = "Job Location: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.expOpt3Loc = "Job Location: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
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

