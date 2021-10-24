import Challenge_6
from tud_test_base import set_keyboard_input, get_display_output


# This set of tests requires the entry John	Smith	allenda	dsdas123A-	On	On	On	English	None	None	None	None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	School: None	Degree: None	Years: None
def test_turning_guest_controls_off():
    set_keyboard_input(["1", "2", "3", "4", "10", "12"])
    Challenge_6.signedIn = True
    Challenge_6.firstName = "John"
    Challenge_6.lastName = "Smith"
    Challenge_6.password = "dsdas123A-"
    Challenge_6.userName = "allenda"
    Challenge_6.emailOpt = "On"
    Challenge_6.advOpt = "On"
    Challenge_6.smsOpt = "On"
    Challenge_6.languageOpt = "English"
    Challenge_6.privacy()
    with open("login.txt") as f:
        firstline = f.readline().rstrip()
        assert firstline == "John	Smith	allenda	dsdas123A-	Off	Off	Off	English	None	None	None	None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	School: None	Degree: None	Years: None"


def test_turning_guest_controls_on():
    set_keyboard_input(["1", "2", "3", "4", "10", "12"])
    Challenge_6.signedIn = True
    Challenge_6.firstName = "John"
    Challenge_6.lastName = "Smith"
    Challenge_6.password = "dsdas123A-"
    Challenge_6.userName = "allenda"
    Challenge_6.emailOpt = "Off"
    Challenge_6.advOpt = "Off"
    Challenge_6.smsOpt = "Off"
    Challenge_6.languageOpt = "English"
    Challenge_6.privacy()
    with open("login.txt") as f:
        firstline = f.readline().rstrip()
        assert firstline == "John	Smith	allenda	dsdas123A-	On	On	On	English	None	None	None	None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	School: None	Degree: None	Years: None"

def test_turning_language_controls_Spanish():
    set_keyboard_input(["1", "2", "10", "12"])
    Challenge_6.signedIn = True
    Challenge_6.firstName = "John"
    Challenge_6.lastName = "Smith"
    Challenge_6.password = "dsdas123A-"
    Challenge_6.userName = "allenda"
    Challenge_6.emailOpt = "On"
    Challenge_6.advOpt = "On"
    Challenge_6.smsOpt = "On"
    Challenge_6.languageOpt = "English"
    Challenge_6.language()
    with open("login.txt") as f:
        firstline = f.readline().rstrip()
        assert firstline == "John	Smith	allenda	dsdas123A-	On	On	On	Spanish	None	None	None	None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	School: None	Degree: None	Years: None"

def test_turning_language_controls_English():
    set_keyboard_input(["1", "2", "10", "12"])
    Challenge_6.signedIn = True
    Challenge_6.firstName = "John"
    Challenge_6.lastName = "Smith"
    Challenge_6.password = "dsdas123A-"
    Challenge_6.userName = "allenda"
    Challenge_6.emailOpt = "On"
    Challenge_6.advOpt = "On"
    Challenge_6.smsOpt = "On"
    Challenge_6.languageOpt = "Spanish"
    Challenge_6.language()
    with open("login.txt") as f:
        firstline = f.readline().rstrip()
        assert firstline == "John	Smith	allenda	dsdas123A-	On	On	On	English	None	None	None	None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	Title: None	Employer: None	Start Date: None	End Date: None	Job Location: None	Description: None	School: None	Degree: None	Years: None"

def test_General_Sign_Up():
    set_keyboard_input(["1", "1", "John", "Smith", "allendu", "dsdas123A-", "12"])
    Challenge_6.signedIn = True
    Challenge_6.usefulLinks()
    output = get_display_output()
    assert output == ["\nUseful Links",
                      "[1] General",
                      "[2] Browse InCollege",
                      "[3] Business Solutions",
                      "[4] Directories",
                      "[5] Return to previous",
                      "Choose an option: ",
                      "\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
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


def test_Useful_Links_Browse_InCollege():
    set_keyboard_input(["2"])
    Challenge_6.signedIn = True
    Challenge_6.usefulLinks()
    output = get_display_output()
    assert output == ["\nUseful Links",
                      "[1] General",
                      "[2] Browse InCollege",
                      "[3] Business Solutions",
                      "[4] Directories",
                      "[5] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]


def test_Useful_Links_Business_Solutions():
    set_keyboard_input(["3"])
    Challenge_6.signedIn = True
    Challenge_6.usefulLinks()
    output = get_display_output()
    assert output == ["\nUseful Links",
                      "[1] General",
                      "[2] Browse InCollege",
                      "[3] Business Solutions",
                      "[4] Directories",
                      "[5] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]


def test_Useful_Links_Directories():
    set_keyboard_input(["4"])
    Challenge_6.signedIn = True
    Challenge_6.usefulLinks()
    output = get_display_output()
    assert output == ["\nUseful Links",
                      "[1] General",
                      "[2] Browse InCollege",
                      "[3] Business Solutions",
                      "[4] Directories",
                      "[5] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]


def test_General_Help_Center():
    set_keyboard_input(["2"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "We're here to help."
                      ]

def test_General_Help_Center():
    set_keyboard_input(["2"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "We're here to help."
                      ]


def test_General_About():
    set_keyboard_input(["3"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "In College: Welcome to In College, the world's largest college student network with many users",
                      "in many countries and territories worldwide."
                      ]


def test_General_Press():
    set_keyboard_input(["4"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "In College Pressroom: Stay on top of the latest news, updates and reports."
                      ]


def test_General_Blogs():
    set_keyboard_input(["5"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]


def test_General_Careers():
    set_keyboard_input(["6"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]


def test_General_Careers():
    set_keyboard_input(["7"])
    Challenge_6.signedIn = True
    Challenge_6.general()
    output = get_display_output()
    assert output == ["\nGeneral",
                      "[1] Sign Up",
                      "[2] Help Center",
                      "[3] About",
                      "[4] Press",
                      "[5] Blogs",
                      "[6] Careers",
                      "[7] Developers",
                      "[8] Return to previous",
                      "Choose an option: ",
                      "Under Construction"
                      ]
