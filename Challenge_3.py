import os
from pathlib import Path

# global variable to see if user is signed-in
signedIn = False
# get the name of current user
current_Name = ""
userName = ""
password = ""
emailOpt = ""
smsOpt = ""
advOpt = ""
languageOpt = ""


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
    print("[7] Resources/Links")
    print("[8] Exit the Program")

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
        links()
    elif option == 8:
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
                file.write(" ")
                file.write(lastName)
                file.write(" ")
                file.write(username)
                file.write(" ")
                file.write(password)
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("English")
                file.write("\n")
                file.close()
                print("\nAccount Created.\nNow You Can Log-In!")
                menu()
                return
            else:
                # if file has existing accounts, check to make sure user name is not already taken
                for line in open("Login.txt", "r").readlines():
                    userCheck = line.split()
                    if not line.strip():
                        pass
                    elif username == userCheck[2]:
                        print("Username Already Exists, Please Try Again.")
                        create(accCount)
                        return

                file = open("Login.txt", "a")
                file.write(firstName)
                file.write(" ")
                file.write(lastName)
                file.write(" ")
                file.write(username)
                file.write(" ")
                file.write(password)
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("On")
                file.write(" ")
                file.write("English")
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
    global password
    global userName
    global emailOpt
    global advOpt
    global smsOpt
    global languageOpt

    print("\nLog In")
    # ask for user and password
    username = input("Please Enter Your UserName: ")
    password = input("Please Enter Your Password: ")

    # read in login text file to see if account exists
    for line in open("Login.txt", "r").readlines():
        # line split into list of strings
        # the 3rd and 4th elements in list will be user name and password
        info = line.split()
        if not line.strip():  # if its an empty line skip
            pass
        # if the user and password input matches any of the ones stored proceed to log-in
        elif username == info[2] and password == info[3]:
            print("\nYou Have Successfully Logged In")
            signedIn = True
            current_Name = info[0] + " " + info[1]
            userName = info[2]
            password = info[3]
            emailOpt = info[4]
            smsOpt = info[5]
            advOpt = info[6]
            languageOpt = info[7]
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
        info = line.split()
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


def links():
    print("[1] Useful links")
    print("[2] InCollege Important Links")
    print("[3] Return to menu")
    linkOpt = int(input("Choose an option: "))
    while linkOpt != 3:
        if linkOpt == 1:
            usefulLinks()
            return
        elif linkOpt == 2:
            ImportantLinks()
            return
        else:
            print("Invalid Option, Try Again!")
            linkOpt = int(input("Choose an option: "))
    print("Returning to menu.")
    menu()
    return


def usefulLinks():
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
    links()
    return


def ImportantLinks():
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

            return
        elif imptOpt == 2:

            return
        elif imptOpt == 3:

            return
        elif imptOpt == 4:

            return
        elif imptOpt == 5:
            privacy()
            return
        elif imptOpt == 6:

            return
        elif imptOpt == 7:

            return
        elif imptOpt == 8:

            return
        elif imptOpt == 9:
            language()
            return
        else:
            print("Invalid Option, Try Again!")
            imptOpt = int(input("Choose an option: "))

    print("Returning...")
    links()
    return


def privacy():
    global signedIn
    if signedIn:
        print("Guest Controls")
        print("[1] Toggle Email notifications")
        print("[1] Toggle SMS notifications")
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
    count = -1
    for line in open("Login.txt", "r"):
        info = line.split()
        if userName != info[0]:
            count = count + 1
            pass
        if info[4] == "On":
            print("Email notifications turned off.")
            temp = 1
        else:
            print("Email notifications turned on.")
            temp = 0
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + "Off" + " " + smsOpt + " " + advOpt \
                             + " " + languageOpt + "\n"
    else:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + "On" + " " + smsOpt + " " + advOpt \
                             + " " + languageOpt + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    return


def sms():
    count = -1
    for line in open("Login.txt", "r"):
        info = line.split()
        if userName != info[0]:
            count = count + 1
            pass
        if info[5] == "On":
            print("SMS notifications turned off.")
            temp = 1
        else:
            print("SMS notifications turned on.")
            temp = 0
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + "Off" + " " \
                             + advOpt + " " + languageOpt + "\n"
    else:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + "On" + " " \
                             + advOpt + " " + languageOpt + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    return


def adv():
    count = -1
    for line in open("Login.txt", "r"):
        info = line.split()
        if userName != info[0]:
            count = count + 1
            pass
        if info[7] == "English":
            print("Targeted Advertising notifications turned off.")
            temp = 1
        else:
            print("Targeted Advertising notifications turned on.")
            temp = 0
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + smsOpt + " " \
                             + "Off" + " " + languageOpt + "\n"
    else:
        listOfLines[count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + smsOpt + " " \
                             + "On" + " " + languageOpt + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    return


def language():
    count = -1
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
                for line in open("Login.txt", "r"):
                    info = line.split()
                    if userName != info[0]:
                        count = count + 1
                        pass
                    if info[7] == "English":
                        print("Switched the language to Spanish.")
                        temp = 1
                    else:
                        print("Switched the language to English.")
                        temp = 0
                file = open("Login.txt", "r")
                listOfLines = file.readlines()
                if temp == 1:
                    listOfLines[
                        count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + smsOpt + " " \
                                 + advOpt + " " + "Spanish" + "\n"
                else:
                    listOfLines[
                        count] = current_Name + " " + userName + " " + password + " " + emailOpt + " " + smsOpt + " " \
                                 + advOpt + " " + "English" + "\n"
                file = open("Login.txt", "w")
                file.writelines(listOfLines)
                file.close()
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


def general():
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
