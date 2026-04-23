from flask import Flask, render_template, request, redirect, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "agripredicts"

# ---------------- DATABASE ----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ---------------- MODELS ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100))
    disease = db.Column(db.String(100))
    confidence = db.Column(db.Float)
    image = db.Column(db.String(200))
    date = db.Column(db.String(100))

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100))
    comment = db.Column(db.Text)
    rating = db.Column(db.Integer)
    date = db.Column(db.String(100))

with app.app_context():
    db.create_all()

# ---------------- TRANSLATIONS ----------------
translations = {
    "en":{
        "title_upload":"Upload Image","predict":"Predict Disease","profile":"Profile","logout":"Logout",
        "dashboard":"Dashboard","drag_drop":"Drag & Drop Image Here","click_browse":"Click to Browse",
        "solution_title":"Solution","confidence":"Confidence","title_result":"Result",
        "feedback":"Your comments...","submit":"Submit","rating":"Rate your experience",
        "image":"Image","disease":"Disease","date":"Date"
    },
    "te":{
        "title_upload":"చిత్రాన్ని అప్‌లోడ్ చేయండి","predict":"వ్యాధిని గుర్తించండి","profile":"ప్రొఫైల్",
        "logout":"లాగ్ అవుట్","dashboard":"డాష్‌బోర్డ్","drag_drop":"చిత్రాన్ని డ్రాగ్ చేయండి",
        "click_browse":"బ్రౌజ్ చేయండి","solution_title":"పరిష్కారం","confidence":"నమ్మకం",
        "title_result":"ఫలితం","feedback":"మీ అభిప్రాయం","submit":"సబ్మిట్",
        "rating":"మీ అనుభవాన్ని రేట్ చేయండి","image":"చిత్రం","disease":"వ్యాధి","date":"తేదీ"
    },
    "hi":{
        "title_upload":"छवि अपलोड करें","predict":"रोग पहचानें","profile":"प्रोफ़ाइल",
        "logout":"लॉग आउट","dashboard":"डैशबोर्ड","drag_drop":"छवि ड्रैग करें",
        "click_browse":"ब्राउज़ करें","solution_title":"समाधान","confidence":"विश्वास",
        "title_result":"परिणाम","feedback":"अपनी प्रतिक्रिया","submit":"सबमिट",
        "rating":"अपने अनुभव को रेट करें","image":"छवि","disease":"रोग","date":"तारीख"
    }
}

# ---------------- DISEASE TRANSLATION ----------------
disease_translations = {
    "Leafsmut": {"en":"Leaf Smut","te":"ఆకు స్మట్","hi":"पत्ती स्मट"},
    "Bacterialblight": {"en":"Bacterial Blight","te":"బ్యాక్టీరియా బ్లైట్","hi":"बैक्टीरियल ब्लाइट"},
    "Brownspot": {"en":"Brown Spot","te":"బ్రౌన్ స్పాట్","hi":"ब्राउन स्पॉट"}
}

def get_text():
    return translations.get(session.get("lang","en"), translations["en"])

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect("/login")

# ---------------- LOGIN ----------------
@app.route("/login")
def login():
    if "user" in session:
        return redirect("/upload")
    return render_template("login.html")

@app.route("/login_user", methods=["POST"])
def login_user():
    user = User.query.filter_by(email=request.form.get("email")).first()

    if user and check_password_hash(user.password, request.form.get("password")):
        session["user"] = user.email
        session["lang"] = session.get("lang","en")
        return redirect("/upload")

    return render_template("error.html", message="Invalid Email or Password")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")

        if User.query.filter_by(email=email).first():
            return render_template("error.html", message="User already exists")

        db.session.add(User(
            name=request.form.get("name"),
            email=email,
            password=generate_password_hash(request.form.get("password"))
        ))
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/register_user", methods=["POST"])
def register_user():
    return register()

# ---------------- FORGOT PASSWORD ----------------
@app.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/reset_password", methods=["POST"])
def reset_password():
    email = request.form.get("email")
    new_password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return render_template("error.html", message="User not found")

    user.password = generate_password_hash(new_password)
    db.session.commit()

    return redirect("/login")

# ---------------- PROFILE ----------------
@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")

    user = User.query.filter_by(email=session["user"]).first()
    return render_template("profile.html", user=user)

@app.route("/update_profile", methods=["POST"])
def update_profile():
    if "user" not in session:
        return redirect("/login")

    user = User.query.filter_by(email=session["user"]).first()

    name = request.form.get("name")
    new_email = request.form.get("email")
    password = request.form.get("password")

    user.name = name

    if new_email != user.email:
        if User.query.filter_by(email=new_email).first():
            return render_template("error.html", message="Email already exists")
        user.email = new_email

    if password and password.strip():
        user.password = generate_password_hash(password)

    db.session.commit()
    session["user"] = user.email

    return redirect(url_for("profile"))

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------------- LANGUAGE ----------------
@app.route("/set_language/<lang>")
def set_language(lang):
    session["lang"] = lang
    return redirect(request.referrer or "/upload")

# ---------------- UPLOAD ----------------
@app.route("/upload")
def upload():
    if "user" not in session:
        return redirect("/login")
    return render_template("upload.html", text=get_text())

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect("/login")

    file = request.files.get("image")
    if not file or file.filename == "":
        return redirect("/upload")

    os.makedirs("uploads", exist_ok=True)
    file.save(os.path.join("uploads", file.filename))

    disease = "Leafsmut"
    confidence = 98.5

    db.session.add(Prediction(
        user_email=session["user"],
        disease=disease,
        confidence=confidence,
        image=file.filename,
        date=datetime.now().strftime("%d-%m-%Y %H:%M")
    ))
    db.session.commit()

    session["result"] = {"disease": disease, "confidence": confidence, "image": file.filename}

    return redirect("/result")

# ---------------- RESULT ----------------
@app.route("/result")
def result():
    data = session.get("result")
    if not data:
        return redirect("/upload")

    lang = session.get("lang","en")
    disease_name = disease_translations.get(data["disease"], {}).get(lang, data["disease"])

    return render_template("result.html",
        disease=data["disease"],
        disease_name=disease_name,
        confidence=data["confidence"],
        image=data["image"],
        text=get_text()
    )

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    lang = session.get("lang","en")
    predictions = Prediction.query.filter_by(user_email=session["user"]).all()

    for p in predictions:
        p.disease_name = disease_translations.get(p.disease, {}).get(lang, p.disease)

    return render_template("dashboard.html",
        data=predictions,
        feedbacks=Feedback.query.filter_by(user_email=session["user"]).all(),
        text=get_text()
    )

# ---------------- FEEDBACK ----------------
@app.route("/feedback")
def feedback():
    if "user" not in session:
        return redirect("/login")
    return render_template("feedback.html", text=get_text())

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    db.session.add(Feedback(
        user_email=session["user"],
        comment=request.form.get("comment"),
        rating=int(request.form.get("rating", 5)),
        date=datetime.now().strftime("%d-%m-%Y %H:%M")
    ))
    db.session.commit()

    return redirect("/dashboard")

# ---------------- FILE ----------------
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)