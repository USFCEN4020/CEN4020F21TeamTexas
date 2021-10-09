import Challenge_4
from tud_test_base import set_keyboard_input, get_display_output


def test_education_section():
    set_keyboard_input(["1", "6", "University Of South Florida", "Computer Science",
                        "5", "7", "3", "10"])
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
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
    Challenge_4.eduOptSchool = "School: None"
    Challenge_4.eduOptDegree = "Degree: None"
    Challenge_4.eduOptYears = "Years: None"
    Challenge_4.variable = 0

    Challenge_4.personalProfile()
    with open("login.txt") as f:
        firstline = f.readline().rstrip()
        if firstline[3] == "Spider11!":
            assert firstline == "John	Smith	JohnS11!	Spider11!	On	On	On	English	None	" \
                                "None	None	None	Title: None	Employer: None	Start Date: None	" \
                                "End Date: None	Description: None	Title: None	Employer: None	Start Date: None	" \
                                "End Date: None	Description: None	Title: None	Employer: None	Start Date: None	" \
                                "End Date: None	Description: None	School: University Of South Florida	" \
                                "Degree: Computer Science	Years: 5"


def test_create_and_view_profile():
    set_keyboard_input(["1", "1", "4th Year Computer Science Student",
                        "2", "Computer Science", "3", "South Florida",
                        "4", "I am currently a student at the University of South Florida. "
                             "Some programming languages that I am familiar with are Python "
                             "and Java. I have been involved in many projects for Disney. I "
                             "worked as a programmer to write functioning software.", "5",
                        "1", "Code Developer", "Disney", "11/16/19", "03/19/20", "Florida",
                        "Help Design And Develop Code", "4", "6", "University Of South Florida",
                        "Computer Science", "5", "7", "2", "3", "10"])
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
    Challenge_4.expOpt1Des = "Description: None"
    Challenge_4.expOpt2Title = "Title: None"
    Challenge_4.expOpt2Emp = "Employer: None"
    Challenge_4.expOpt2Start = "Start Date: None"
    Challenge_4.expOpt2End = "End Date: None"
    Challenge_4.expOpt2Des = "Description: None"
    Challenge_4.expOpt3Title = "Title: None"
    Challenge_4.expOpt3Emp = "Employer: None"
    Challenge_4.expOpt3Start = "Start Date: None"
    Challenge_4.expOpt3End = "End Date: None"
    Challenge_4.expOpt3Des = "Description: None"
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
                      "Title: 4th Year Computer Science Student",
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
                      "Description: Help Design And Develop Code",
                      "\nJob Experience2",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Description: None",
                      "\nJob Experience3",
                      "Title: None",
                      "Employer: None",
                      "Start Date: None",
                      "End Date: None",
                      "Description: None",
                      "\nEducation",
                      "School: University Of South Florida",
                      "Degree: Computer Science",
                      "Years: 5\n",
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