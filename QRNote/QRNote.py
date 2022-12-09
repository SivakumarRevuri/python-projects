from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import secrets
import qrcode
import os
import json

# Set Flask secret key
app = Flask(__name__)
app.secret_key = secrets.token_bytes()

# Define stylesheet
@app.route("/stylesheet.css")
def css():
    return redirect(url_for('static', filename='stylesheet.css'))

# Define javascript
@app.route("/script.js")
def js():
    return redirect(url_for('static', filename='script.js'))

# Read the config file
with open("config.json") as config:
    config = json.load(config)

# Login page
@app.route("/", methods=["POST", "GET"])
def auth():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == config["USERNAME"] and password == config["PASSWORD"]:
            session["user"] = username
        return redirect(url_for("home"))
    else:
        return render_template("auth.html")

# Homepage
@app.route("/home", methods=["POST", "GET"])
def home():
    # Check session cookie
    if "user" not in session:
        return redirect(url_for("auth"))

    # To display note list
    notes = []
    notes_with_ext = os.listdir("static/img")
    for note in notes_with_ext:
        note = note[:len(note)-4]
        notes.append(note)

    # Viewing of notes
    qr = ""
    if request.method == "POST":
        qr = "img/" + request.form["qr"] + ".png"
    return render_template("home.html", qr=qr, len=len(notes), notes=notes)

# Note creation page
@app.route("/create", methods=["POST", "GET"])
def create():
    # Check session cookie
    if "user" not in session:
        return redirect(url_for("auth"))

    # To display note list
    notes = []
    notes_with_ext = os.listdir("static/img")
    for note in notes_with_ext:
        note = note[:len(note)-4]
        notes.append(note)

    # Creation of notes
    note_name = ""
    if request.method == "POST":
        note = request.form["note"]
        note_name = request.form["note_name"] + ".png"
        qrcode.make(note).save(f"static/img/{note_name}")
        return redirect(url_for("create"))
    return render_template("create.html", note_name=note_name, notes=notes, len=len(notes))

# Deletion page
@app.route("/delete", methods=["POST", "GET"])
def delete():
    # Check session cookie
    if "user" not in session:
        return redirect(url_for("auth"))

    # To display note list
    notes = []
    notes_with_ext = os.listdir("static/img")
    for note in notes_with_ext:
        note = note[:len(note)-4]
        notes.append(note)
    
    # Deletion of notes
    if request.method == "POST":
        note_to_delete = "static/img/" + request.form["note_to_delete"] + ".png"
        os.remove(note_to_delete)
        return redirect(url_for("delete"))
    return render_template("delete.html", notes=notes, len=len(notes))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1440)