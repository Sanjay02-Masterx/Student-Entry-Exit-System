# Student Entry–Exit Management System
# Author: Sanjay Murugesan
# Description: Flask-based web application for hostel entry-exit logging


from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Add student
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student_id = request.form["student_id"]
        name = request.form["name"]
        department = request.form["department"]

        with open("data.txt", "a") as file:
            file.write(student_id + "," + name + "," + department + "\n")

        return "Student added successfully! <br><br><a href='/'>Go Home</a>"

    return render_template("add.html")

# Entry / Exit
@app.route("/entry", methods=["GET", "POST"])
def entry_exit():
    if request.method == "POST":
        student_id = request.form["student_id"]
        status = request.form["status"]
        time = datetime.datetime.now()

        with open("data.txt", "a") as file:
            file.write(student_id + "," + status + "," + str(time) + "\n")

        return "Entry/Exit recorded! <br><br><a href='/'>Go Home</a>"

    return render_template("entry.html")

# View records
@app.route("/view")
def view_records():
    records = []

    try:
        with open("data.txt", "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        records = []

    return render_template("view.html", records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

