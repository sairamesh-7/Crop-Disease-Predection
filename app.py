from flask import Flask, render_template, request, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.secret_key = "agripredicts"

# -----------------------------
# DATABASE CONFIG
# -----------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -----------------------------
# USER TABLE
# -----------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

with app.app_context():
    db.create_all()

# -----------------------------
# TRANSLATIONS
# -----------------------------
translations = {

"en":{
"title_upload":"Upload Image",
"title_result":"Prediction Result",
"solution":"Solution",
"feedback":"Your Feedback",
"submit":"Submit"
},

"te":{
"title_upload":"చిత్రాన్ని అప్‌లోడ్ చేయండి",
"title_result":"అంచనా ఫలితం",
"solution":"పరిష్కారం",
"feedback":"మీ అభిప్రాయం",
"submit":"సమర్పించండి"
},

"hi":{
"title_upload":"छवि अपलोड करें",
"title_result":"भविष्यवाणी परिणाम",
"solution":"समाधान",
"feedback":"आपकी प्रतिक्रिया",
"submit":"जमा करें"
}

}

# -----------------------------
# MULTILINGUAL SOLUTIONS
# -----------------------------
solutions = {

"en":{

"Bacterialblight":[
"Remove infected leaves immediately",
"Apply copper fungicide",
"Avoid overhead irrigation",
"Maintain proper plant spacing"
],

"Brownspot":[
"Use disease resistant seeds",
"Apply fungicide spray",
"Improve soil fertility",
"Ensure proper drainage"
],

"Leafsmut":[
"Remove infected plants immediately",
"Apply Carbendazim fungicide",
"Maintain proper crop rotation",
"Avoid high humidity conditions"
]

},

"te":{

"Bacterialblight":[
"సంఖ్యాబాధిత ఆకులను వెంటనే తొలగించండి",
"కాపర్ ఫంగిసైడ్ ఉపయోగించండి",
"పై నుండి నీరు పోయడం నివారించండి",
"మొక్కల మధ్య సరైన దూరం ఉంచండి"
],

"Brownspot":[
"రోగ నిరోధక విత్తనాలు ఉపయోగించండి",
"ఫంగిసైడ్ స్ప్రే చేయండి",
"నేల ఫలదీకరణ మెరుగుపరచండి",
"సరైన డ్రైనేజ్ కల్పించండి"
],

"Leafsmut":[
"సంఖ్యాబాధిత మొక్కలను వెంటనే తొలగించండి",
"కార్బెండాజిం ఫంగిసైడ్ ఉపయోగించండి",
"సరైన పంట మార్పిడి పాటించండి",
"అధిక తేమను నివారించండి"
]

},

"hi":{

"Bacterialblight":[
"संक्रमित पत्तियों को तुरंत हटा दें",
"कॉपर फंगीसाइड का प्रयोग करें",
"ऊपर से सिंचाई से बचें",
"पौधों के बीच उचित दूरी रखें"
],

"Brownspot":[
"रोग प्रतिरोधी बीजों का उपयोग करें",
"फंगीसाइड स्प्रे करें",
"मिट्टी की उर्वरता बढ़ाएं",
"उचित जल निकासी रखें"
],

"Leafsmut":[
"संक्रमित पौधों को तुरंत हटाएं",
"कार्बेन्डाजिम फंगीसाइड का प्रयोग करें",
"फसल चक्र बनाए रखें",
"अधिक नमी से बचें"
]

}

}

# -----------------------------
# UPLOAD FOLDER
# -----------------------------
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = load_model("model/crop_model.h5")

classes = ["Bacterialblight","Brownspot","Leafsmut"]

# -----------------------------
# IMAGE PREDICTION
# -----------------------------
def predict_image(path):

    img = Image.open(path)
    img = img.convert("RGB")
    img = img.resize((224,224))

    img = np.array(img)/255.0
    img = np.expand_dims(img,axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    disease = classes[index]
    confidence = float(np.max(prediction))*100

    return disease,round(confidence,2)

# -----------------------------
# ROUTES
# -----------------------------

@app.route("/")
def splash():
    return render_template("splash.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_user",methods=["POST"])
def login_user():

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email,password=password).first()

    if user:
        return redirect("/language")

    return "Invalid Login"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_user",methods=["POST"])
def register_user():

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = User(name=name,email=email,password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/login")

# -----------------------------
# LANGUAGE PAGE
# -----------------------------
@app.route("/language")
def language():
    return render_template("language.html")

# -----------------------------
# SET LANGUAGE
# -----------------------------
@app.route("/set_language/<lang>")
def set_language(lang):

    session["lang"] = lang

    return redirect("/upload")

# -----------------------------
# UPLOAD PAGE
# -----------------------------
@app.route("/upload")
def upload():

    lang = session.get("lang","en")
    text = translations[lang]

    return render_template("upload.html",text=text)

# -----------------------------
# PREDICTION
# -----------------------------
@app.route("/predict",methods=["POST"])
def predict():

    file = request.files["image"]

    path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)

    file.save(path)

    disease,confidence = predict_image(path)

    lang = session.get("lang","en")
    text = translations[lang]

    solution = solutions[lang].get(disease,[])

    return render_template(
        "result.html",
        disease=disease,
        confidence=confidence,
        image=file.filename,
        solution=solution,
        text=text
    )

# -----------------------------
# SHOW IMAGE
# -----------------------------
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# -----------------------------
# FEEDBACK
# -----------------------------
@app.route("/feedback")
def feedback():

    lang = session.get("lang","en")
    text = translations[lang]

    return render_template("feedback.html",text=text)

@app.route("/submit_feedback",methods=["POST"])
def submit_feedback():

    return """
    <h2>Thank You!</h2>
    <a href='/'>Home</a>
    """

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)