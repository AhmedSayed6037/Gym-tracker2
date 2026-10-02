from cs50 import SQL
from flask import Flask,redirect, render_template, request, session , flash
from flask_session import Session
from werkzeug.security import generate_password_hash,check_password_hash
import os

app = Flask(__name__)

if os.environ.get("DATABASE_URL"):
    db = SQL(os.environ["DATABASE_URL"])
else:
    db = SQL("sqlite:///gym.db")



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

task = [
    "Complete 20 push-ups",
    "Complete 30 bodyweight squats",
    "Hold a plank for 60 seconds",
    "Complete 20 walking lunges",
    "Complete 15 burpees",
    "Complete 30 jumping jacks",
    "Do a 10-minute brisk walk",
    "Complete 20 mountain climbers",
    "Hold a wall sit for 60 seconds",
    "Complete 15 diamond push-ups",
    "Complete 30 calf raises",
    "Complete 20 bicycle crunches",
    "Complete 15 jump squats",
    "Hold a plank for 90 seconds",
    "Complete 20 reverse lunges",
    "Complete 10 burpees followed by 20 squats",
    "Complete 40 jumping jacks",
    "Complete 20 sit-ups",
    "Complete 10 push-ups followed by 20 lunges",
    "Complete a 15-minute walk or jog"
]

images = [
    # 1 - Push-ups
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Push-up.jpg",

    # 2 - Squats
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Squatting.jpg",

    # 3 - Plank
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Plank.jpg",

    # 4 - Lunges
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Girl_doing_lunges.jpg",

    # 5 - Burpees
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Airborne_Burpee.jpg",

    # 6 - Jumping jacks
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Jumpingjacks.gif",

    # 7 - Walking
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Joggers.jpg",

    # 8 - Mountain climbers
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Performing_pushups.jpg",

    # 9 - Wall sit
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Squatting.jpg",

    # 10 - Diamond push-ups
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Personal_training_push-ups_instruction.jpg",

    # 11 - Calf raises
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Standing-calf-raises-1.gif",

    # 12 - Bicycle crunches
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Bicycle_crunch_with_back_support.jpg",

    # 13 - Jump squats
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Squatting.jpg",

    # 14 - 90-second plank
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Woman_performing_plank_exercise_at_home_gym.jpg",

    # 15 - Reverse lunges
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/TRX_lunge_Exercise.jpg",

    # 16 - Burpees + squats
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Airborne_Burpee.jpg",

    # 17 - 40 jumping jacks
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Jumpingjacks.gif",

    # 18 - Sit-ups
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Sit-ups_or_Crunch.gif",

    # 19 - Push-ups + lunges
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Push-up_session.jpg",

    # 20 - Walk/jog
    "https://commons.wikimedia.org/wiki/Special:Redirect/file/Early_morning_Jogging.jpg"
]

@app.route("/",methods=["GET","POST"])
def index():
         if "user_id" not in session:
              return redirect("/login")
         if request.method == "POST":
                 exercise_number = request.form.get("exercise_number")
                 exercise = request.form.get("exercise")
                 muscle = request.form.get("muscle")
                 sets = request.form.get("sets")
                 day = request.form.get("day")
                 reps = request.form.get("reps")
                 weight = request.form.get("weight")
                 db.execute("INSERT INTO workouts (user_id, day, exercise_number, exercise, muscle, sets, reps, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                                   session["user_id"],
                                                   day,
                                                   exercise_number,
                                                  exercise,
                                                  muscle,
                                                  sets,
                                                  reps,
                                                  weight
                                                         )
                 return redirect("/")
         else:
                             saturday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Saturday")

                             sunday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Sunday")

                             monday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Monday")

                             tuesday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Tuesday")

                             wednesday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Wednesday")

                             thursday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Thursday")

                             friday = db.execute("SELECT id, exercise_number, exercise, muscle, sets, reps, weight FROM workouts WHERE user_id = ? AND day = ?",
                             session["user_id"], "Friday")
                             return render_template(
                                                     "index.html",
                                                    saturday=saturday,
                                                    sunday=sunday,
                                                     monday=monday,
                                                     tuesday=tuesday,
                                                   wednesday=wednesday,
                                                   thursday=thursday,
                                                    friday=friday)



@app.route("/delete",methods = ["POST"])
def delete():
    remove = request.form.get("remove")
    db.execute("DELETE FROM workouts WHERE user_id = ? AND id = ?",session["user_id"],remove)
    return redirect("/")


@app.route("/register",methods = ["GET","POST"])
def register():
   if request.method == "POST":
       # take user,pass
       username = request.form.get("username")
       password = request.form.get("password")
       confirm = request.form.get("confirm")
       gender = request.form.get("gender")
       name = db.execute("SELECT username FROM users WHERE username = ?",username)
       # check
       if len(username) < 5:
           return render_template("register.html",message="not enough characters")
       if len(password) < 8:
           return render_template("register.html",message="not enough characters")
       if password != confirm:
            return render_template("register.html",message = "Passwords do not match")
       if not name:
            db.execute("INSERT INTO users (username,hash,gender) VALUES (?,?,?)",username,generate_password_hash(password),gender)
       else:
              return render_template("register.html",message="Username already exists!")
       return redirect("/login")
   else:
         return render_template("register.html")



@app.route("/login",methods=["GET","POST"])
def login():
     if request.method == "POST":
         username = request.form.get("username")
         password = request.form.get("password")
         name = db.execute("SELECT id,username,hash FROM users WHERE username = ?",username)
         if not name:
            if not name:
               return render_template("login.html", message="Username does not exist")
         if not check_password_hash(name[0]["hash"],password):
             return render_template("login.html",message="Wrong Password")
         session["user_id"] = name[0]["id"]
         return redirect("/")
     else:
         return render_template("login.html")


@app.route("/password",methods=["GET","POST"])
def change_password():
    if request.method == "POST":
        password = request.form.get("password")
        if len(password) < 8:
                return render_template("password.html",message="not enough characters")
        db.execute("UPDATE users SET hash = ? WHERE id = ?",generate_password_hash(password),session["user_id"])
        return redirect("/")
    else:
        return render_template("password.html")


@app.route("/username",methods=["GET","POST"])
def username_password():
    if request.method == "POST":
        username = request.form.get("username")
        db.execute("UPDATE users SET username = ? WHERE id = ?",username,session["user_id"])
        return redirect("/")
    else:
        return render_template("user.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/calories",methods=["GET","POST"])
def calories():
     if request.method == "POST":
          gender = request.form.get("gender")
          age = int(request.form.get("age"))
          height = float(request.form.get("height"))
          weight = float(request.form.get("weight"))
          level = request.form.get("level")
          if gender == "Male":
              BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
          else:
               BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
          if level == "Sedentary":
               main = BMR * 1.2
          elif level == "Lightly Active":
               main = BMR * 1.375
          elif level == "Moderatly Active":
                main = BMR * 1.55
          else:
               main = BMR * 1.725
          return render_template("calories.html",BMR = (BMR),main=round(main))
     else:
          return render_template("calories.html")


@app.route("/challenges",methods=["GET","POST"])
def challenges():
     if request.method == "POST":
          number = request.form.get("number")
          status = request.form.get("status")
          challenge = request.form.get("challenge")
          if status == "Done":
               db.execute("INSERT INTO challenges (user_id,challenge,status,time) VALUES (?,?,?,CURRENT_TIMESTAMP)",session["user_id"],challenge,"Done")
               return render_template("challenges.html", message="Well done! Challenge completed! 🔥",status="Done")
          elif status == "Failed":
               db.execute("INSERT INTO challenges (user_id,challenge,status,time) VALUES (?,?,?,CURRENT_TIMESTAMP)",session["user_id"],challenge,"Failed")
               return render_template("challenges.html", message="Good luck next time! 💪",status="Failed")
          if not number:
                return render_template("challenges.html",message="Please enter a number")
          if int(number) > 20 or int(number) < 1:
                return render_template("challenges.html",message="Enter a number From 1 to 20")
          if int(number):
             do = task[int(number) - 1]
             photo = images[int(number) - 1]
          return render_template("challenges.html",do=do,photo=photo)
     else:
          return render_template("challenges.html")

@app.route("/history")
def history():
     history = db.execute("SELECT challenge,status,time FROM challenges WHERE user_id = ?",session["user_id"])
     workouts = db.execute("SELECT day,exercise_number,exercise,muscle,sets,reps,weight FROM workouts WHERE user_id = ?",session["user_id"])
     return render_template("history.html",history=history,workouts=workouts)
