from tkinter import Entry


def login():

    # Creating a boolean variable called 'entry' with the value False
    # Asking the user to input their username and their password.
    entry = False
    username = input("\nPlease enter your username: ").lower()
    password = input("Please enter your password: ").lower()

    # Opening the 'user.txt' file as 'users' in read-mode using the 'with open' function.
    with open("user.txt", "r", encoding='utf-8') as users:

        # Creating a for-loop to go through every line in the 'users' text-file.
        # If the username AND the password inputs are found on the same row within the text-file, then the user will be granted access.
        for line in users:

            if username in line and password in line:
                entry = True
                print("You have been logged in", username)
                break

    # Creating while-loop to repeatedly ask the user for their username and password until it is found in the text-file.
    while not entry:

        # Printing the error message to the user to inform them that their username or password is incorrect.
        # Asking the user to input their username and their password again.

        print("\nIncorrect Username or Password. Please ensure you are registered and that your spelling is correct.")
        username = input("\nPlease enter your username: ").lower()
        password = input("Please enter your password: ").lower()

        # Opening the 'user.txt' file as 'users' in read-mode using the 'open' function.
        with open("user.txt", "r") as users:

            # Creating a for-loop to go through every line in the 'users' text-file.
            # If the username AND the password inputs are found on the same row within the text-file, then the user will be granted access.
            for line in users:

                if username in line and password in line:
                    entry = True
                    print("You have been logged in", username)
                    break


login()

while True:

 # Adding two menu options: 'ao' for admin only to be able  to register new users and
 # 'ds' for data statistics for compulsary task part 2
    menu = input('''\nSelect one of the following Options below:
 r  - Registering a user
 a  - Adding a task
 va - View all tasks
 vm - view my task
 ao - admin only 
 ds - data statistics
 e  - Exit
 : ''').lower()

    # Registering a new user by inputing the username, a password and confirming the password.
    # Verifying if the passwords match. if matching write the user details to the files
    if menu == 'r':
        pass

        new_user = input("\nEnter a new username: ").lower()
        new_password = input("Enter a new password: ").lower()
        confirm_password = input("Confirm the password: ").lower()

        if new_password == confirm_password:
            user_details = "\n" + new_user + ", " + new_password

            with open("user.txt", "a") as f:
                f.write(user_details)

        elif new_password != confirm_password:
            print("wrong loggin details, please try again")

    # Adding a new task to task.txt file , start by opening the text file in append mode and write to the file every inputed data
    elif menu == 'a':
        pass

        with open("tasks.txt", "a") as task:

            new_task_user = input(
                "Enter the username of the person whom the task is assigned to: ")
            task.write("\n" + new_task_user)

            title = input("Enter the title of the task: ")
            task.write(", " + title)

            description = input("Enter the description of the task: ")
            task.write(", " + description)

            due_date = input("Enter the due date of the task: ")
            task.write(", " + due_date)

            current_date = input("Enter the current date: ")
            task.write(", " + current_date)

            task_completed = "No"
            task.write(", " + task_completed)

    # Viewing all tasks from task file and print to the console in the format of output 2 in L1T19 pdf file
    # Opening the file in read mode, read a line from the the file, split the line and print to the console.
    elif menu == 'va':
        pass

        task_file = open("tasks.txt", "r")
        read_file = task_file.readlines()
        task_split = read_file[1].strip().split(", ")

        print("\nTask:\t\t\t", task_split[1])
        print("Assigned to:\t\t", task_split[0])
        print("Date assigned:\t\t", task_split[3])
        print("Due date:\t\t", task_split[4])
        print("Task completed?\t\t", task_split[5])
        print("Task description:\n", task_split[2])

        task_file.close()

    # Viewing tasks assigned to the user logged in
    # Opening the file in read mode, read a line from the the file, split the line
    # Verify if the username of the person logged in is the same as the user we have, if yes print to the console
    elif menu == 'vm':
        pass
        task_file = open("tasks.txt", "r")
        read_file = task_file.readlines()
        task_split = read_file[1].strip().split(", ")
        
        username = input("Enter username: ").lower()

        if username == task_split[0]:
            print("\nTask:\t\t\t", task_split[1])
            print("Date assigned:\t\t", task_split[3])
            print("Due date:\t\t", task_split[4])
            print("Task completed?\t\t", task_split[5])
            print("Task description:\n", task_split[2])

        else:
            print("Sorry,Wrong username.")

        task_file.close()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # **********COMPULSORY PART 2***************
    # Creating a program where only the admin is allowed to register new users
    # Asking to enter admin as username to register a new user, if correctly inputed we proceed
    # or if not action will be denied
    elif menu == 'ao':
        username = input("Please enter 'admin' as your username: ").lower()

        if username == 'admin':
            new_user = input("\nEnter a new username: ").lower()
            new_password = input("Enter a new password: ").lower()
            confirm_password = input("Confirm the password: ").lower()

            if new_password == confirm_password:
                user_details = "\n" + new_user + ", " + new_password

                with open("user.txt", "a") as f:
                    f.write(user_details)

            elif new_password != confirm_password:
                print("Wrong password, please enter the same password to register.")

        else:
            print("Sorry, only 'admin' is allowed to add new users.")

    # Reading the data statistics
    # Open both files in read mode, read a line from the file text, creating two variables containing each the number
    # of tasks and users obtained by using the len() method.
    elif menu == 'ds':
        with open("tasks.txt", 'r') as task_file:
            task_number = len(task_file.readlines())
            print(task_number)

        with open("user.txt", "r") as users:
            users_number = len(users.readlines())

            print("\nThe total number of tasks is: ", task_number)
            print("The total number of users is: ", users_number)

    else:
        print("You have made a wrong choice, Please Try again")
