# User Authentication and Task Management System

This Python program is a simple user authentication and task management system. It allows users to log in, register new users (admin-only), add tasks, view all tasks, view their own tasks, and view data statistics.

## How to Use

1. **Log In**:
   - When you run the program, you will be prompted to enter your username and password.
   - If the provided credentials match those stored in the `user.txt` file, you will be logged in.

2. **Register New Users (Admin-Only)**:
   - To register a new user, you must log in as an admin (username: 'admin').
   - Admins can create new usernames and passwords for other users.

3. **Add Tasks**:
   - After logging in, you can add tasks to the system.
   - Provide the username of the person the task is assigned to, a title, description, due date, and the current date.
   - Task completion status is set to "No" by default.

4. **View All Tasks**:
   - You can view all tasks in the system.
   - The program displays tasks in a formatted manner, including task details such as title, assigned user, due date, and completion status.

5. **View Your Own Tasks**:
   - You can view tasks assigned to you by entering your username.
   - The program will display your tasks, including details like due date and completion status.

6. **Data Statistics**:
   - You can view data statistics, including the total number of tasks and users in the system.
   - This option provides an overview of the system's data.

7. **Exit**:
   - To exit the program, choose the 'e' option from the menu.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or would like to add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the original repository.


Feel free to use this program to manage tasks and users more efficiently. If you have any questions or suggestions, please don't hesitate to reach out.
