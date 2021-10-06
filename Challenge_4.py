import os
from pathlib import Path

# global variable to see if user is signed-in
signedIn = False
# get the name of current user
current_Name = ""
firstName = ""
lastName = ""
userName = ""
password = ""
emailOpt = ""
smsOpt = ""
advOpt = ""
languageOpt = ""
titleOpt = "None"
majorOpt = "None"
UniOpt = "None"
aboutOpt = "None"
expOpt1Title = "Title: None"
expOpt1Emp = "Employer: None"
expOpt1Start = "Start Date: None"
expOpt1End = "End Date: None"
expOpt1Des = "Description: None"
expOpt2Title = "Title: None"
expOpt2Emp = "Employer: None"
expOpt2Start = "Start Date: None"
expOpt2End = "End Date: None"
expOpt2Des = "Description: None"
expOpt3Title = "Title: None"
expOpt3Emp = "Employer: None"
expOpt3Start = "Start Date: None"
expOpt3End = "End Date: None"
expOpt3Des = "Description: None"
eduOptSchool = "School: None"
eduOptDegree = "Degree: None"
eduOptYears = "Years: None"
variable = 0


# display menu that lets user select options
def menu():
    if not signedIn:
        print("\nWant to hear what students have to say about InCollege?")
        print("\nRead about how InCollege helped Ethan Timor:")
        print('\t "I was never able to land an interview or internship in college. ')
        print("\t Thankfully, I discovered InCollege and I couldn't be more thankful! ")
        print("\t Within days, I had interviews, and offers from companies like:")
        print("\t Tesla, Microsoft, Google, and Apple")
        print("\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.")
        print('\t It would not be possible without InCollege."')

    print("\nMenu")
    print("[1] Log In")
    print("[2] Create an Account")
    print("[3] Search for a Job")
    print("[4] Find Someone You Know")
    print("[5] Learn a New Skill")
    print("[6] Not Sure About InCollege? Watch this Video!")
    print("[7] Useful Links")
    print("[8] InCollege Important Links")
    print("[9] Personal Profile")
    print("[10] Exit the Program")

    option = int(input("Enter your option: "))

    if option == 1:
        login()
    elif option == 2:
        create(accountCount())
    elif option == 3:
        searchJob()
    elif option == 4:
        findSomeone()
    elif option == 5:
        learnSkill()
    elif option == 6:
        print("Video is now playing")
        menu()
    elif option == 7:
        usefulLinks()
    elif option == 8:
        ImportantLinks()
    elif option == 9:
        personalProfile()
    elif option == 10:
        return
    else:
        print("Invalid option.")
        menu()


# this function returns the number of accounts created in the system
def accountCount():
    file = open("Login.txt", "r")
    count = 0
    for line in file:
        if line != "\n":
            count += 1
    file.close()
    return count


# create an account and print a statement to let user it was done successfully
def create(accCount):
    global titleOpt
    global majorOpt
    global UniOpt
    global aboutOpt
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Des
    global eduOptSchool
    global eduOptDegree
    global eduOptYears
    filesize = os.path.getsize("Login.txt")  # check if there are any accounts already made or not
    print("\nCreate A Account")

    # if there are less than 5 accounts proceed
    if accCount < 5:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")

        # check if the password is valid, if not keep asking for account name and password
        while not passCheck(password):
            username = input("Please Input a UserName: ")
            password = input("Please Input a Password: ")

        if passCheck(password):
            # if password is valid and file is empty, then add user info to the system
            if filesize == 0:
                file = open("Login.txt", "a")
                file.write(firstName)
                # separate user info in file with space
                file.write("\t")
                file.write(lastName)
                file.write("\t")
                file.write(username)
                file.write("\t")
                file.write(password)
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("English")
                file.write("\t")
                file.write(titleOpt)
                file.write("\t")
                file.write(majorOpt)
                file.write("\t")
                file.write(UniOpt)
                file.write("\t")
                file.write(aboutOpt)
                file.write("\t")
                file.write(expOpt1Title)
                file.write("\t")
                file.write(expOpt1Emp)
                file.write("\t")
                file.write(expOpt1Start)
                file.write("\t")
                file.write(expOpt1End)
                file.write("\t")
                file.write(expOpt1Des)
                file.write("\t")
                file.write(expOpt2Title)
                file.write("\t")
                file.write(expOpt2Emp)
                file.write("\t")
                file.write(expOpt2Start)
                file.write("\t")
                file.write(expOpt2End)
                file.write("\t")
                file.write(expOpt2Des)
                file.write("\t")
                file.write(expOpt3Title)
                file.write("\t")
                file.write(expOpt3Emp)
                file.write("\t")
                file.write(expOpt3Start)
                file.write("\t")
                file.write(expOpt3End)
                file.write("\t")
                file.write(expOpt3Des)
                file.write("\t")
                file.write(eduOptSchool)
                file.write("\t")
                file.write(eduOptDegree)
                file.write("\t")
                file.write(eduOptYears)
                file.write("\n")
                file.close()
                print("\nAccount Created.\nNow You Can Log-In!")
                menu()
                return
            else:
                # if file has existing accounts, check to make sure user name is not already taken
                for line in open("Login.txt", "r").readlines():
                    userCheck = line.split("\t")
                    if not line.strip():
                        pass
                    elif username == userCheck[2]:
                        print("Username Already Exists, Please Try Again.")
                        create(accCount)
                        return

                file = open("Login.txt", "a")
                file.write(firstName)
                file.write("\t")
                file.write(lastName)
                file.write("\t")
                file.write(username)
                file.write("\t")
                file.write(password)
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("English")
                file.write("\t")
                file.write(titleOpt)
                file.write("\t")
                file.write(majorOpt)
                file.write("\t")
                file.write(UniOpt)
                file.write("\t")
                file.write(aboutOpt)
                file.write("\t")
                file.write(expOpt1Title)
                file.write("\t")
                file.write(expOpt1Emp)
                file.write("\t")
                file.write(expOpt1Start)
                file.write("\t")
                file.write(expOpt1End)
                file.write("\t")
                file.write(expOpt1Des)
                file.write("\t")
                file.write(expOpt2Title)
                file.write("\t")
                file.write(expOpt2Emp)
                file.write("\t")
                file.write(expOpt2Start)
                file.write("\t")
                file.write(expOpt2End)
                file.write("\t")
                file.write(expOpt2Des)
                file.write("\t")
                file.write(expOpt3Title)
                file.write("\t")
                file.write(expOpt3Emp)
                file.write("\t")
                file.write(expOpt3Start)
                file.write("\t")
                file.write(expOpt3End)
                file.write("\t")
                file.write(expOpt3Des)
                file.write("\t")
                file.write(eduOptSchool)
                file.write("\t")
                file.write(eduOptDegree)
                file.write("\t")
                file.write(eduOptYears)
                file.write("\n")
                file.close()
                print("\nAccount Created.\nNow You Can Log-In!")
                menu()
                return

    else:
        # if there are over 5 accounts return to menu
        print("\nAll permitted accounts have been created, please come back later.")
        menu()
        return


def passCheck(password):  # check if password is valid
    returnVal = True
    # all the non alpha characters
    Symbols = [' ', '~', '!', '@', '#', '$', '^', '&', '*', '(', ')', '_', '-', '+',
               '=', '{', '}', '[', ']', '|', ':', ';', '<', ',', '>', '.', '?', '/']
    if len(password) < 8:  # check if password has 8 or more characters
        print("The length of the password should be at least 8 characters.")
        returnVal = False
    if len(password) > 12:  # check if password is within 12 characters
        print("The length of the password should not be greater than 12 characters.")
        returnVal = False
    if not any(char.isdigit() for char in password):  # check if password has at least 1 digit
        print("The password should have at least one digit.")
        returnVal = False
    if not any(char.isupper() for char in password):  # check if password has at least 1 uppercase letter
        print("The password should have at least one uppercase letter.")
        returnVal = False
    if not any(char in Symbols for char in password):  # check if password has at least one non alpha character
        print("The password should have at least one non-alpha character.")
        returnVal = False
    return returnVal


def login():  # login function
    global signedIn
    global current_Name
    global firstName
    global lastName
    global password
    global userName
    global emailOpt
    global advOpt
    global smsOpt
    global languageOpt
    global titleOpt
    global majorOpt
    global UniOpt
    global aboutOpt
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Des
    global eduOptSchool
    global eduOptDegree
    global eduOptYears

    print("\nLog In")
    # ask for user and password
    username = input("Please Enter Your UserName: ")
    password = input("Please Enter Your Password: ")

    # read in login text file to see if account exists
    for line in open("Login.txt", "r").readlines():
        # line split into list of strings
        # the 3rd and 4th elements in list will be user name and password
        info = line.split("\t")
        if not line.strip():  # if its an empty line skip
            pass
        # if the user and password input matches any of the ones stored proceed to log-in
        elif username == info[2] and password == info[3]:
            print("\nYou Have Successfully Logged In")
            signedIn = True
            current_Name = info[0] + " " + info[1]
            firstName = info[0]
            lastName = info[1]
            userName = info[2]
            password = info[3]
            emailOpt = info[4]
            smsOpt = info[5]
            advOpt = info[6]
            languageOpt = info[7]
            titleOpt = info[8]
            majorOpt = info[9]
            UniOpt = info[10]
            aboutOpt = info[11]

            expOpt1Title = info[12]
            expOpt1Emp = info[13]
            expOpt1Start = info[14]
            expOpt1End = info[15]
            expOpt1Des = info[16]

            expOpt2Title = info[17]
            expOpt2Emp = info[18]
            expOpt2Start = info[19]
            expOpt2End = info[20]
            expOpt2Des = info[21]

            expOpt3Title = info[22]
            expOpt3Emp = info[23]
            expOpt3Start = info[24]
            expOpt3End = info[25]
            expOpt3Des = info[26]

            eduOptSchool = info[27]
            eduOptDegree = info[28]
            eduOptYears = info[29]
            menu()
            return

    # if no matches in the system, allow user to try again
    print("Incorrect UserName/Password, Please Try Again")
    signedIn = False
    # repeat the log-in
    login()
    return


# find someone you know function
def findSomeone():
    global signedIn
    print("\nFind Someone You Know")
    firstName = input("Enter Their First Name: ")
    lastName = input("Enter Their Last Name: ")

    # read file and check if any user names match the user input
    for line in open("Login.txt", "r").readlines():
        # each line has a unique users info
        # info is a line from text file, that is split up into a list of strings
        info = line.split("\t")
        if not line.strip():
            pass
        # if user input matches a name in the system proceed
        elif firstName == info[0] and lastName == info[1]:
            print("They are a part of the InCollege system!")
            # if person is not signed-in allow them to log-in, sign-up, or return to menu
            if not signedIn:
                print("[1] Log In")
                print("[2] Sign Up to Join Friend")
                print("[3] Return to Options")
                choice = int(input("Please Select an Option: "))
                while choice != 3:
                    if choice == 1:
                        login()
                        return
                    elif choice == 2:
                        count = accountCount()
                        create(count)
                        return
            menu()
            return

    # person was not found in system
    print("They are not yet a part of the InCollege system yet!")
    menu()
    return


# search for a job function
def searchJob():
    print("\nSearch for a Job")
    global signedIn

    # if a person is signed-in they can post a job in the system
    if signedIn:
        print("[1] Post a Job")
        print("[2] Return to menu")
        choice = int(input("Enter Your Option: "))
        while choice != 2:
            if choice == 1:
                postJob()
                return
            else:
                print("Invalid Option")
                searchJob()
                return
        print("Returning to Menu")
        menu()
        return
    # if a person is not signed-in they can't really do anything
    else:
        print("[1] Return to Options")
        choice = int(input("Enter Your Option: "))
        while choice != 1:
            print("Invalid Option")
            searchJob()
            return

        print("Returning to Menu")
        menu()
        return


# post a job function for search for job page
def postJob():
    # count the number of job posts in the system
    file = open("Job_Posts.txt", "r")
    postCount = 0
    for line in file:
        if line != "\n":
            postCount += 1
    file.close()

    file = open("Job_Posts.txt", "a")
    print("\nPost a Job!")
    # if job posts in the system is not 5 or more proceed
    if postCount < 5:
        title = input("Enter a Title: ")
        description = input("Enter a Description: ")
        employer = input("Enter an Employer: ")
        location = input("Enter a Location: ")
        salary = input("Enter a Salary: ")

        # write user input to job posts text file
        # info will be separated on line with a tab
        file.write(title)
        file.write("\t")
        file.write(description)
        file.write("\t")
        file.write(employer)
        file.write("\t")
        file.write(location)
        file.write("\t")
        file.write(salary)
        file.write("\t")
        file.write(current_Name)
        file.write("\n")
        file.close()
        print("Job Posted!")
        searchJob()
        return
    # there are already 5 jobs posted, so user can't do anything
    else:
        print("There are already 5 jobs posted!")
        searchJob()
        return


# learn a skill page
def learnSkill():
    print("\nLearn a New Skill")
    print("[1] Learn ...")
    print("[2] Learn ...")
    print("[3] Learn ...")
    print("[4] Learn ...")
    print("[5] Learn ...")
    print("[6] Return")
    learn = int(input("Choose What You Want to Learn: "))

    while learn != 6:
        if learn == 1:
            # when more functionality is needed, add the different skill functions to here for calling
            print("Under Construction.")
            return
        elif learn == 2:
            print("Under Construction.")
            return
        elif learn == 3:
            print("Under Construction.")
            return
        elif learn == 4:
            print("Under Construction.")
            return
        elif learn == 5:
            print("Under Construction.")
            return
        else:
            # if invalid choice ask for something else
            print("Invalid Option, Try Again!")
            learn = int(input("Choose What You Want to Learn: "))

    menu()  # return to option screen if 6 is chosen
    return


def usefulLinks():
    print("\nUseful Links")
    print("[1] General")
    print("[2] Browse InCollege")
    print("[3] Business Solutions")
    print("[4] Directories")
    print("[5] Return to previous")
    usefulOpt = int(input("Choose an option: "))
    while usefulOpt != 5:
        if usefulOpt == 1:
            general()
            return
        elif usefulOpt == 2:
            print("Under Construction")
            return
        elif usefulOpt == 3:
            print("Under Construction")
            return
        elif usefulOpt == 4:
            print("Under Construction")
            return
        else:
            print("Invalid Option, Try Again!")
            usefulOpt = int(input("Choose an option: "))
    print("Returning...")
    menu()
    return


def ImportantLinks():
    print("\nImportant Links")
    print("[1] Copyright Notice")
    print("[2] About")
    print("[3] Accessibility")
    print("[4] User Agreement")
    print("[5] Privacy Policy")
    print("[6] Cookie Policy")
    print("[7] Copyright Policy")
    print("[8] Brand Policy")
    print("[9] Languages")
    print("[10] Return to previous")
    imptOpt = int(input("Choose an option: "))
    while imptOpt != 10:
        if imptOpt == 1:
            copyRightNotice()
            return
        elif imptOpt == 2:
            about()
            return
        elif imptOpt == 3:
            accessibility()
            return
        elif imptOpt == 4:
            userAgreement()
            return
        elif imptOpt == 5:
            privacy()
            return
        elif imptOpt == 6:
            cookiePolicy()
            return
        elif imptOpt == 7:
            copyRightPolicy()
            return
        elif imptOpt == 8:
            brandPolicy()
            return
        elif imptOpt == 9:
            language()
            return
        else:
            print("Invalid Option, Try Again!")
            imptOpt = int(input("Choose an option: "))

    print("Returning...")
    menu()
    return


# about page for important links
def about():
    print("\nAbout InCollege\n\n"
          "InCollege is an online application that has been designed exclusively for college \n"
          "students. Searching for a first job can be challenging, but InCollege provides \n"
          "tools that are needed in order to be successful. This service allows students at \n"
          "various universities to network and exchange information about school, jobs, \n"
          "salaries, offers, and projects.\n")
    ImportantLinks()
    return


# accessibility page for important links
def accessibility():
    print("\nAccessibility\n\n"
          "InCollege is a place for college students to connect and find opportunities"
          " in the workforce. \n\nWe’re here to help you succeed with any goals, ideas, or "
          "ambitions that you want to carry out. "
          "\n\nWith a diverse collection of InCollege members, accessibility is a major key \n"
          "for establishing a great community. Our aim is to design products, services, \n"
          "and environments for people for people who experience disabilities. We wish \n"
          "to identify, remove, and prevent barriers that would make it difficult for students \n"
          "to interact with the InCollege application.\n")
    ImportantLinks()
    return


# copyright policy page for important links
def copyRightPolicy():
    print("\nCopyright Policy\n\n"
          "InCollege respects the intellectual property rights of others and expects its \n"
          "users to do the same. It is InCollege’s policy to remove or terminate any users \n"
          "who repeatedly infringe or charged with infringing the copyrights or other intellectual \n"
          "property rights of others. Information posted by members should be accurate, lawful, \n"
          "and not in violation of any U.S copyright laws. Any complaints regarding copyright \n"
          "infringement can be handled in copyright notice.\n")
    ImportantLinks()
    return


# cookie policy page for important links
def cookiePolicy():
    print("\nCookie Policy\n\n"
          "By using InCollege, you consent to the use of cookies.\n\n"
          "Cookies are small blocks of data sent from web browser by the website you are on. A \n"
          "cookie file allows the InCollege or a third-party to recognize you and make your next \n"
          "visit easier.\n\n"
          "Cookies are used to enable certain functions of InCollege, provide analytics, store \n"
          "preferences and enable advertisement delivery. Essential cookies authenticate users \n"
          "and prevent fraudulent use of user accounts. \n\n"
          "Third – party cookies are used to report usage statistics and deliver advertisement \n"
          "for InCollege.\n")
    ImportantLinks()
    return


# copyright notice page for important links
def copyRightNotice():
    print("\nCopyright Notice\n\n"
          "This application and its content is copyright of InCollege. Any redistribution or \n"
          "reproduction of part or all of the contents in any form is prohibited. You may not, \n"
          "distribute or commercially exploit the content. Nor may you transmit or store it in any \n"
          "other website or other form of electronic retrieval system.\n\n"
          "If you notice any of copyright infringement please notify us at copyright@InCollege.com\n")
    ImportantLinks()
    return


# brand policy page for important links
def brandPolicy():
    print("\nBrand Policy\n\n"
          "Any trademarks and brand features are protected by law. You’ll need InCollege’s \n"
          "consent in order to use them. \n\n"
          "InCollege does not permit its members, third party developers, partners and the media \n"
          "to use its name, trademarks, logos, web pages, screenshots and other brand features. \n")
    ImportantLinks()
    return


# user agreement page for important links
def userAgreement():
    print("\nUser Agreement \n\n"
          "Users are expected to follow all policies, provide accurate information, and use all "
          "services in a professional manner.")
    ImportantLinks()
    return


def privacy():
    print("\nPrivacy Policy\n\n"
          "Personal information is only processed with your consent, or on another legal basis. \n"
          "In addition, privacy settings can be changed by any signed-in user to meet specific needs.\n")
    global signedIn
    if signedIn:
        print("\nGuest Controls")
        print("[1] Toggle Email notifications")
        print("[2] Toggle SMS notifications")
        print("[3] Toggle Targeted Advertising features")
        print("[4] Return to previous")
        privacyOpt = int(input("Choose an option: "))
        while privacyOpt != 4:
            if privacyOpt == 1:
                email()
                return
            elif privacyOpt == 2:
                sms()
                return
            elif privacyOpt == 3:
                adv()
                return
            else:
                print("Invalid Option, Try Again!")
                privacyOpt = int(input("Choose an option: "))

        print("Returning...")
        ImportantLinks()
        return
    else:
        print("[1] Return to previous")
        privacyOpt = int(input("Choose an option: "))
        while privacyOpt != 1:
            print("Invalid Option, Try Again!")
            privacyOpt = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return


def email():
    global emailOpt
    count = 0
    if emailOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Email notifications turned off.")
        emailOpt = "Off"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    else:
        print("Email notifications turned on.")
        emailOpt = "On"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def sms():
    global smsOpt
    count = 0
    if smsOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("SMS notifications turned off.")
        smsOpt = "Off"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears

    else:
        print("SMS notifications turned on.")
        smsOpt = "On"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def adv():
    global advOpt
    count = 0
    if advOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Targeted Advertising notifications turned off.")
        advOpt = "Off"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    else:
        print("Targeted Advertising notifications turned on.")
        advOpt = "On"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def language():
    global languageOpt
    print("\nLanguage")
    if signedIn:
        if languageOpt == "English":
            print("[1] Change language to Spanish.")
            print("[2] Return to previous")
        else:
            print("[1] Change language to English.")
            print("[2] Return to previous")
        languageChoice = int(input("Choose an option: "))
        while languageChoice != 2:
            if languageChoice == 1:
                switchLanguage()
                return
            else:
                print("Invalid option, Try Again!")
                languageChoice = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return
    else:
        print("[1] Return to previous")
        languageChoice = int(input("Choose an option: "))
        while languageChoice != 1:
            print("Invalid option, Try Again!")
            languageChoice = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return


def switchLanguage():
    global languageOpt
    count = 0
    if languageOpt == "English":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Switched the language to Spanish.")
        languageOpt = "Spanish"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    else:
        print("Switched the language to English.")
        languageOpt = "English"
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                             + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                             + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                             + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                             + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                             + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    ImportantLinks()
    return


def general():
    print("\nGeneral")
    print("[1] Sign Up")
    print("[2] Help Center")
    print("[3] About")
    print("[4] Press")
    print("[5] Blogs")
    print("[6] Careers")
    print("[7] Developers")
    print("[8] Return to previous")
    generalOpt = int(input("Choose an option: "))
    while generalOpt != 8:
        if generalOpt == 1:
            create(accountCount())
            return
        elif generalOpt == 2:
            print("We're here to help.")
            return
        elif generalOpt == 3:
            print("In College: Welcome to In College, the world's largest college student network with many users")
            print("in many countries and territories worldwide.")
            return
        elif generalOpt == 4:
            print("In College Pressroom: Stay on top of the latest news, updates and reports.")
            return
        elif generalOpt == 5:
            print("Under Construction")
            return
        elif generalOpt == 6:
            print("Under Construction")
            return
        elif generalOpt == 7:
            print("Under Construction")
            return
        else:
            print("Invalid Option, Try Again!")
            generalOpt = int(input("Choose an option: "))
    usefulLinks()
    return


def personalProfile():
    global signedIn
    print("Profile")
    if signedIn:
        print("[1] Edit Profile")
        print("[2] View Profile")
        print("[3] Return to menu")
        profileOpt = int(input("Choose an option: "))
        while profileOpt != 3:
            if profileOpt == 1:
                editProfile()
                return
            elif profileOpt == 2:
                viewProfile()
                return
            else:
                print("Invalid option, Try Again!")
                profileOpt = int(input("Choose an option: "))
        print("Returning to menu...")
        menu()
        return
    else:
        print("[1] Return to menu")
        profileOpt = int(input("Choose an option: "))
        while profileOpt != 1:
            print("Invalid option, Try Again!")
        print("Returning to menu...")
        menu()
        return


def editProfile():
    print("[1] Title")
    print("[2] Major")
    print("[3] University Name")
    print("[4] About")
    print("[5] Work experience")
    print("[6] Education")
    print("[7] Return to previous")
    editOpt = int(input("Choose an option: "))
    while editOpt != 7:
        if editOpt == 1:
            profileTitle()
            return
        elif editOpt == 2:
            profileMajor()
            return
        elif editOpt == 3:
            profileUni()
            return
        elif editOpt == 4:
            profileAbout()
            return
        elif editOpt == 5:
            profileExp()
            return
        elif editOpt == 6:
            profileEdu()
            return
        else:
            print("Invalid option, Try Again!")
            editOpt = int(input("Choose an option: "))
    print("Returning...")
    personalProfile()
    return


def profileTitle():
    global titleOpt
    count = 0
    title = input("Enter a title: ")
    titleOpt = title
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    editProfile()
    return


def profileMajor():
    global majorOpt
    count = 0
    major = input("Enter a major: ")
    majorOpt = major
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    editProfile()
    return


def profileUni():
    global UniOpt
    count = 0
    Uni = input("Enter a University: ")
    UniOpt = Uni
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    editProfile()
    return


def profileAbout():
    global aboutOpt
    count = 0
    about = input("Enter an About: ")
    aboutOpt = about
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    editProfile()
    return


def profileExp():
    global variable
    print("Enter information about your past jobs, up to three past jobs")
    print("[1] Job 1")
    print("[2] Job 2")
    print("[3] Job 3")
    print("[4] Return to previous")
    profileExpOpt = int(input("Choose an option: "))
    while profileExpOpt != 4:
        if profileExpOpt == 1:
            variable = 1
            jobExp(variable)
            return
        elif profileExpOpt == 2:
            variable = 2
            jobExp(variable)
            return
        elif profileExpOpt == 3:
            variable = 3
            jobExp(variable)
            return
        else:
            print("Invalid option, Try Again!")
            profileExpOpt = int(input("Choose an option: "))
    print("Returning...")
    editProfile()
    return


def profileEdu():
    global eduOptSchool
    global eduOptDegree
    global eduOptYears
    count = 0
    print("Enter information about your education here")
    school = input("Enter school name: ")
    degree = input("Enter your degree: ")
    years = (input("Enter how many years attended: "))
    eduOptSchool = "School: " + school
    eduOptDegree = "Degree: " + degree
    eduOptYears = "Years: " + years
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    editProfile()
    return


def jobExp(x):
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Des
    count = 0
    print("Enter information about your past jobs here")
    jobTitle = input("Enter the job title: ")
    jobEmployer = input("Enter the employer of the job: ")
    jobStart = input("Enter the start date of the job: ")
    jobEnd = input("Enter the end date of the job: ")
    jobLocation = input("Enter the location of the job: ")
    jobDes = input("Enter a description of the job: ")

    if x == 1:
        expOpt1Title = "Title: " + jobTitle
        expOpt1Emp = "Employer: " + jobEmployer
        expOpt1Start = "Start Date: " + jobStart
        expOpt1End = "End Date: " + jobEnd
        expOpt1Des = "Description: " + jobDes
    elif x == 2:
        expOpt2Title = "Title: " + jobTitle
        expOpt2Emp = "Employer: " + jobEmployer
        expOpt2Start = "Start Date: " + jobStart
        expOpt2End = "End Date: " + jobEnd
        expOpt2Des = "Description: " + jobDes
    elif x == 3:
        expOpt3Title = "Title: " + jobTitle
        expOpt3Emp = "Employer: " + jobEmployer
        expOpt3Start = "Start Date: " + jobStart
        expOpt3End = "End Date: " + jobEnd
        expOpt3Des = "Description: " + jobDes

    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + emailOpt + "\t" \
                         + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" + titleOpt + "\t" \
                         + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" + expOpt1Title + "\t" + expOpt1Emp \
                         + "\t" + expOpt1Start + "\t" + expOpt1End + "\t" + expOpt1Des + "\t" + expOpt2Title \
                         + "\t" + expOpt2Emp + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Des \
                         + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" \
                         + expOpt3End + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                         + "\t" + eduOptYears
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    profileExp()
    return


def viewProfile():
    global variable
    global current_Name
    print("\n" + current_Name)
    print("Title: " + titleOpt)
    result = majorOpt.title()
    print("Major: " + result)
    result = UniOpt.title()
    print("University: " + result)
    print("About: " + aboutOpt)
    print("\nJob Experience1")
    print(expOpt1Title)
    print(expOpt1Emp)
    print(expOpt1Start)
    print(expOpt1End)
    print(expOpt1Des)
    print("\nJob Experience2")
    print(expOpt2Title)
    print(expOpt2Emp)
    print(expOpt2Start)
    print(expOpt2End)
    print(expOpt2Des)
    print("\nJob Experience3")
    print(expOpt3Title)
    print(expOpt3Emp)
    print(expOpt3Start)
    print(expOpt3End)
    print(expOpt3Des)
    print("\nEducation")
    print(eduOptSchool)
    print(eduOptDegree)
    print(eduOptYears + "\n")
    personalProfile()
    return


# create log-in text file if it does not exist
loginFile = "Login.txt"
loginPath = Path(loginFile)
if loginPath.is_file():
    pass
else:
    CreateFile = open("Login.txt", "a")
    CreateFile.close()

# create job posts text file if it does not exist
jobFile = "Job_Posts.txt"
jobPath = Path(jobFile)
if jobPath.is_file():
    pass
else:
    createFile = open("Job_Posts.txt", "a")
    createFile.close()
# display menu
menu()
