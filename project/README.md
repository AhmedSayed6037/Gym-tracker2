# Gym Tracker
Project Title: Gym Tracker
Name: Ahmed Sayed
GitHub Username: AhmedSayed6037
edX Username: Ahmed6037
City and Country: Cairo, Egypt
Date Recorded: September 29, 2026

#### Video Demo: https://youtu.be/QN3a-sj_wG4

#### Description:

Gym Tracker is a web application designed to help users organize their weekly workouts, track exercises, calculate daily calorie needs, complete fitness challenges, and review their workout and challenge history. I created this project as my final project for CS50x.

The main goal of Gym Tracker is to combine several useful fitness tools into one simple website. Instead of having a separate workout planner, calorie calculator, and challenge tracker, the user can access these features from one account.

The application was built primarily using Python and Flask for the backend, SQLite for the database, HTML and Jinja for the web pages, Bootstrap and CSS for styling, and a small amount of JavaScript for interactive elements.

## User Accounts

Users can create their own accounts through the registration page. Each account has a unique username and a hashed password. Passwords are not stored directly in the database. Instead, Werkzeug's password hashing functions are used to store and verify them more securely.

After registering, users can log in and access their personal Gym Tracker data. Flask sessions are used to keep track of the currently logged-in user.

Users can also change their username and password through the Settings menu and can log out when they are finished.

## Workout Tracker

The home page contains the main workout tracker. The week is divided into seven days from Saturday through Friday.

For each day, users can add exercises to their workout plan. An exercise contains information including the exercise name, muscle group, number of sets, number of repetitions, and weight.

Workout information is stored in the SQLite database and connected to the currently logged-in user through their user ID. This means different users can maintain their own workout plans independently.

Users can also remove exercises from their plan when they no longer need them. A tutorial link is available to help users find information about exercises and proper exercise technique.

## Calorie Calculator

Gym Tracker includes a calorie calculator that estimates a user's daily calorie requirements.

The calculator asks for information including age, gender, height, weight, and activity level. It first estimates the user's Basal Metabolic Rate (BMR), which represents approximately how much energy the body uses while at rest.

The BMR is then multiplied by an activity factor to estimate maintenance calories.

The results display four useful values:

- BMR
- Maintenance calories
- Fat-loss target
- Lean-bulk target

The fat-loss target is calculated by subtracting 500 calories from estimated maintenance, while the lean-bulk target adds 300 calories. These values are intended as simple starting estimates rather than medical or nutritional advice.

## Fitness Challenges

The Challenges page adds a more interactive part to the application.

The user chooses a number between 1 and 20. Each number corresponds to a fitness challenge, such as push-ups, squats, planks, lunges, or walking.

After receiving a challenge, the user can mark it as either "Done" or "Failed."

The result is stored in the database together with the challenge, the user's ID, the result, and the time it was attempted. Successful challenges are visually distinguished from failed challenges when displayed in the history.

This feature was designed to add variety and some fun to normal workout tracking.

## History

The History page allows users to review information stored by the application.

It displays workout information associated with the logged-in user as well as previous fitness challenge attempts. Challenge history includes the challenge, whether it was completed or failed, and the date and time of the attempt.

User IDs are used when querying the database so that users only see information associated with their own accounts.

## Project Files

`app.py` contains the main backend logic of the application. It initializes Flask and the SQLite database and contains the routes responsible for registration, login, workouts, calorie calculations, challenges, history, account settings, and logout.

`gym.db` is the SQLite database used by the application. It stores user accounts, workouts, and challenge history.

`requirements.txt` contains the Python packages required to run the project.

The `templates` directory contains the HTML templates used by Flask.

`layout.html` provides the base HTML structure and loads Bootstrap, the custom stylesheet, and JavaScript used by the website.

`index.html` contains the main weekly workout tracker.

`register.html` and `login.html` provide the account registration and authentication interfaces.

`calories.html` contains the calorie calculator form and displays the calculated BMR, maintenance, fat-loss, and lean-bulk values.

`challenges.html` contains the fitness challenge interface and displays the selected challenge and its result.

`history.html` displays workout and challenge information stored for the logged-in user.

The username and password templates provide interfaces for changing account information.

The `static` directory contains `styles.css` and `script.js`. `styles.css` provides the custom dark and blue visual design used throughout the application, while `script.js` contains the JavaScript used for interactive behavior such as displaying and hiding parts of the workout interface.

## Design Choices

One important design decision was to associate workouts and challenge attempts with a user ID. This allows multiple people to use the application while keeping their information separate.

I also decided to use a single SQLite database because it provides everything required for the scope of this project while keeping the application relatively simple.

Another design decision involved the workout tracker. I chose to organize workouts by days of the week because the application is intended primarily as a weekly workout planner. Each day can contain multiple exercises with their own sets, repetitions, weight, and muscle group.

For the challenge system, I chose a simple number-based challenge selection system instead of implementing a complicated animated wheel. This kept the feature simple while still providing an interactive element and allowed challenge results to be stored and displayed in the user's history.

For the visual design, I chose a dark background combined with a blue navigation bar and blue accents. I wanted the website to have a modern fitness-oriented appearance while maintaining readable tables, forms, and buttons.

## Future Improvements

There are several features that could be added in the future. One would be a secure "Forgot Password" system using email verification and time-limited password reset tokens.

The workout history system could also be expanded to store exact workout dates and provide progress graphs showing how a user's weights or repetitions change over time. Deleted workouts could potentially be archived instead of permanently removed, allowing users to restore them later.

Other possible improvements include more detailed exercise tutorials, additional calorie and nutrition tools, custom user-created challenges, and more advanced workout statistics.

Overall, Gym Tracker combines the major concepts I learned throughout CS50, including Python, SQL databases, Flask, HTML, CSS, JavaScript, user authentication, sessions, and dynamic web applications. Building the project helped me understand how these technologies can work together to create a complete application rather than functioning as separate programming concepts.
