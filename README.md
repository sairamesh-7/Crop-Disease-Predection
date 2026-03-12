🌿 Crop-Disease-Predection

Crop-Disease-Predection is a web-based application that uses Artificial Intelligence and Deep Learning to detect crop diseases from leaf images.
Farmers or users can upload crop leaf images and the system predicts the type of disease and provides suggested solutions.

The application also supports multiple languages (English, Telugu, Hindi) to make it easier for farmers to understand the results.

🚀 Features

👤 User Registration and Login

🌍 Multi-language support (English, Telugu, Hindi)

📷 Upload crop leaf images

🤖 AI-based disease detection using a trained model

📊 Prediction confidence score

💡 Suggested solutions for detected diseases

💬 Feedback system

🗄 SQLite database for storing users

# 🛠 Technologies Used

| Technology         | Purpose                 |
| ------------------ | ----------------------- |
| Python             | Backend programming     |
| Flask              | Web framework           |
| TensorFlow / Keras | Deep learning model     |
| HTML               | Frontend structure      |
| CSS                | User interface styling  |
| JavaScript         | Client-side interaction |
| SQLite             | Database                |
| NumPy              | Image processing        |
| Pillow (PIL)       | Image handling          |

---
# 📂 Project Structure

Crop-Disease-Predection/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── train_model.py             # Script to train the AI model
├── test.py                    # Script for testing the model
│
├── instance/
│   ├── database.db            # SQLite database
│   └── users.db               # User login database
│
├── model/
│   └── crop_model.h5          # Trained AI model
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── images/
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── splash.html
│   ├── login.html
│   ├── register.html
│   ├── language.html
│   ├── upload.html
│   ├── result.html
│   ├── feedback.html
│   └── thankyou.html
│
└── uploads/

📊 Dataset

The dataset used to train the crop disease detection model is available on Kaggle:

Rice Plant Diseases Dataset
https://www.kaggle.com/datasets/jay7080dev/rice-plant-diseases-dataset

The dataset contains images of rice plant leaves categorized into different disease classes used to train the deep learning model.

⚙️ Installation
Clone the repository
git clone https://github.com/sairamesh-7/Crop-Disease-Predection.git
Navigate to the project folder
cd Crop-Disease-Predection
Install dependencies
pip install -r requirements.txt
▶️ Run the Application

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000/
📸 How the System Works

User registers or logs into the system.

User selects preferred language.

User uploads a crop leaf image.

The AI model processes the image.

The system predicts the crop disease.

The system displays disease name, confidence score, and solutions.

User can submit feedback.

🧠 AI Model

The system uses a Convolutional Neural Network (CNN) trained on crop disease datasets.

Model file location:

model/crop_model.h5

Diseases currently supported:

Bacterial Blight

Brown Spot

Leaf Smut

🔮 Future Improvements

Add more crop disease datasets

Improve prediction accuracy

Add more language support

Mobile application version

Real-time camera disease detection

👨‍💻 Author

Pragada Sai Ramesh

GitHub Profile:
https://github.com/sairamesh-7

Project Repository:
https://github.com/sairamesh-7/Crop-Disease-Predection

📜 License

This project is developed for educational and research purposes.







