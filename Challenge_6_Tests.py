import Challenge_8
from tud_test_base import set_keyboard_input, get_display_output


# Create an account must be ran first before attempting any of the test cases
def test_create_ten_accounts_5():
    set_keyboard_input(["Allen", "Cheng", "Allenc", "Cheng123-", "S", "2",
                        "Ray", "Cheng", "Raym", "Cheng123-", "S", "2",
                        "Dylan", "Bradford", "DylanB", "Cheng123-", "S", "13"])
    Challenge_8.create(Challenge_8.accountCount())


#Login to attempt test cases
def test_login1():
    set_keyboard_input(["Allenc", "Cheng123-", "13"])
    Challenge_8.login()


def test_maximum_job_post():
    set_keyboard_input(["1", "Job1", "Des1", "Emp1", "Loc1", "Sal1",
                        "1", "Job2", "Des2", "Emp2", "Loc2", "Sal2",
                        "1", "Job3", "Des3", "Emp3", "Loc3", "Sal3",
                        "1", "Job4", "Des4", "Emp4", "Loc4", "Sal4",
                        "1", "Job5", "Des5", "Emp5", "Loc5", "Sal5",
                        "1", "Job6", "Des6", "Emp6", "Loc6", "Sal6",
                        "1", "Job7", "Des7", "Emp7", "Loc7", "Sal7",
                        "1", "Job8", "Des8", "Emp8", "Loc8", "Sal8",
                        "1", "Job9", "Des9", "Emp9", "Loc9", "Sal9",
                        "1", "Job10", "Des10", "Emp10", "Loc10", "Sal10", "1",
                        "5", "13"
                        ])
    Challenge_8.searchJob()
    count = 0
    with open("Job_Posts.txt") as a_file:
        for line in a_file:
            if line != "\n":
                count += 1
    assert count == 10


def test_apply_for_job_created_by_user():
    set_keyboard_input(["2", "1", "2", "13"])
    Challenge_8.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "Number of applied jobs: 0",
                      "[1] Post a Job",
                      "[2] Search for a job",
                      "[3] Generate saved jobs",
                      "[4] Generate unsaved jobs",
                      "[5] Return to menu",
                      "Enter Your Option: ",
                      "[1] Job1",
                      "[2] Job2",
                      "[3] Job3",
                      "[4] Job4",
                      "[5] Job5",
                      "[6] Job6",
                      "[7] Job7",
                      "[8] Job8",
                      "[9] Job9",
                      "[10] Job10",
                      "Enter your selection: ",
                      "Title: Job1",
                      "Job Description: Des1",
                      "Employer: Emp1",
                      "Location: Loc1",
                      "Salary: Sal1",
                      "Posted By: Allen Cheng",
                      "[1] Delete This Job Post",
                      "[2] Return to Menu",
                      "Enter your selection: ",
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


def test_login2():
    set_keyboard_input(["Raym", "Cheng123-", "13"])
    Challenge_8.login()


def test_apply_for_job():
    set_keyboard_input(["2", "1", "1", "May 2022", "May 2022", "I am good", "13"])
    Challenge_8.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "New posted job titled: Job1",
                      "New posted job titled: Job2",
                      "New posted job titled: Job3",
                      "New posted job titled: Job4",
                      "New posted job titled: Job5",
                      "New posted job titled: Job6",
                      "New posted job titled: Job7",
                      "New posted job titled: Job8",
                      "New posted job titled: Job9",
                      "New posted job titled: Job10\n",
                      "Number of applied jobs: 0",
                      "[1] Post a Job",
                      "[2] Search for a job",
                      "[3] Generate saved jobs",
                      "[4] Generate unsaved jobs",
                      "[5] Return to menu",
                      "Enter Your Option: ",
                      "[1] Job1",
                      "[2] Job2",
                      "[3] Job3",
                      "[4] Job4",
                      "[5] Job5",
                      "[6] Job6",
                      "[7] Job7",
                      "[8] Job8",
                      "[9] Job9",
                      "[10] Job10",
                      "Enter your selection: ",
                      "Title: Job1",
                      "Job Description: Des1",
                      "Employer: Emp1",
                      "Location: Loc1",
                      "Salary: Sal1",
                      "Posted By: Allen Cheng",
                      "[1] Apply For This Job",
                      "[2] Save/Unsave this Job",
                      "[3] Return to Menu",
                      "Enter your selection: ",
                      "Please enter a graduation date: ",
                      "Please enter the date you can start working: ",
                      "Please submit a paragraph stating why you would be good for this job: ",
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


def test_save_a_job():
    set_keyboard_input(["2", "1", "2", "13"])
    Challenge_8.searchJob()
    with open("Job_Posts.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split("\t")
            if stripped_line[0] == "Job1":
                assert stripped_line[8] == "saved,Raym,"



def test_generate_list_of_saved_jobs():
    set_keyboard_input(["3", "1", "13"])
    Challenge_8.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "Number of applied jobs: 1",
                      "[1] Post a Job",
                      "[2] Search for a job",
                      "[3] Generate saved jobs",
                      "[4] Generate unsaved jobs",
                      "[5] Return to menu",
                      "Enter Your Option: ",
                      "Title: Job1",
                      "Job Description: Des1",
                      "Employer: Emp1",
                      "Location: Loc1",
                      "Salary: Sal1",
                      "Posted By: Allen Cheng",
                      "\n",
                      "Type anything to Return To Menu: ",
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


def test_unsave_a_job():
    set_keyboard_input(["2", "1", "2", "13"])
    Challenge_8.searchJob()
    with open("Job_Posts.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split("\t")
            if stripped_line[0] == "Job1":
                assert stripped_line[8] == "saved,"


def test_apply_for_job_already_applied():
    set_keyboard_input(["2", "1", "1", "13"])
    Challenge_8.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "Number of applied jobs: 1",
                              "[1] Post a Job",
                              "[2] Search for a job",
                              "[3] Generate saved jobs",
                              "[4] Generate unsaved jobs",
                              "[5] Return to menu",
                              "Enter Your Option: ",
                              "[1] Job1 - Applied For",
                              "[2] Job2",
                              "[3] Job3",
                              "[4] Job4",
                              "[5] Job5",
                              "[6] Job6",
                              "[7] Job7",
                              "[8] Job8",
                              "[9] Job9",
                              "[10] Job10",
                              "Enter your selection: ",
                              "Title: Job1",
                              "Job Description: Des1",
                              "Employer: Emp1",
                              "Location: Loc1",
                              "Salary: Sal1",
                              "Posted By: Allen Cheng",
                              "[1] Apply For This Job",
                              "[2] Save/Unsave this Job",
                              "[3] Return to Menu",
                              "Enter your selection: ",
                              "You've already applied for this job!",
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



def test_login3():
    set_keyboard_input(["Allenc", "Cheng123-", "13"])
    Challenge_8.login()


def test_delete_a_job():
    set_keyboard_input(["2", "1", "1", "13"])
    Challenge_8.searchJob()
    with open("Job_Posts.txt", "r") as a_file:
        lines = a_file.readlines()
        #only checking the first lines to see that the first job was deleted
        assert lines[0] == "Job2	Des2	Emp2	Loc2	Sal2	Allen Cheng	Allenc	applicants,	saved,	Placeholder\n"


def test_login4():
    set_keyboard_input(["Raym", "Cheng123-", "13"])
    Challenge_8.login()


def test_delete_notification():
    set_keyboard_input(["5", "13"])
    Challenge_8.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                      "Number of applied jobs: 0",
                      "You applied for 1 job but it has been deleted.\n",
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
                      "[12] Messages",
                      "[13] Exit the Program",
                      "Enter your option: "
                     ]