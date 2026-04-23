# 🌿 Crop Disease Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A web-based application that uses Artificial Intelligence and Deep Learning to detect crop diseases from leaf images.**

Farmers and users can upload crop leaf images, and the system predicts the type of disease along with suggested solutions.

> 🌍 Supports **English**, **Telugu**, and **Hindi** — making results accessible to farmers across regions.

</div>

---

## 🚀 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | 👤 User Authentication | Secure user registration and login system |
| 2 | 🌍 Multi-language Support | Interface available in English, Telugu, and Hindi |
| 3 | 📷 Image Upload | Upload crop leaf images for instant analysis |
| 4 | 🤖 AI Disease Detection | CNN-based disease classification from leaf images |
| 5 | 📊 Confidence Score | Prediction probability score displayed to the user |
| 6 | 💡 Suggested Solutions | Treatment and solution recommendations per disease |
| 7 | 💬 Feedback System | Users can submit feedback on predictions |
| 8 | 🗄️ Database Storage | SQLite database for user data and feedback |

---

## 🛠️ Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Backend programming language   |
| Flask              | Web framework                  |
| TensorFlow / Keras | Deep learning model (CNN)      |
| HTML               | Frontend structure             |
| CSS                | User interface styling         |
| JavaScript         | Client-side interaction        |
| SQLite             | User and feedback database     |
| NumPy              | Numerical and image processing |
| Pillow (PIL)       | Image loading and handling     |

---

## 📂 Project Structure

```
Crop-Disease-Prediction/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── train_model.py             # Script to train the AI model
├── test.py                    # Script for testing the model
│
├── instance/
│   ├── database.db            # SQLite database (feedback & data)
│   └── users.db               # User login database
│
├── model/
│   └── crop_model.h5          # Trained CNN model (Keras)
│
├── static/
│   ├── css/
│   │   └── style.css          # Application styles
│   ├── images/                # Static image assets
│   └── js/
│       └── script.js          # Frontend JavaScript
│
├── templates/
│   ├── splash.html            # Splash / landing screen
│   ├── login.html             # User login page
│   ├── register.html          # User registration page
│   ├── language.html          # Language selection page
│   ├── upload.html            # Image upload page
│   ├── result.html            # Prediction results page
│   ├── feedback.html          # Feedback submission page
│   └── thankyou.html          # Thank you confirmation page
│
└── uploads/                   # Uploaded leaf images (runtime)
```

---

## 📊 Dataset

The model was trained using the **Rice Plant Diseases Dataset** available on Kaggle:

🔗 [Rice Plant Diseases Dataset](https://www.kaggle.com/datasets/jay7080dev/rice-plant-diseases-dataset)

The dataset contains labeled images of rice plant leaves across multiple disease categories used to train the deep learning model.

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sairamesh-7/Crop-Disease-Predection.git
```

**2. Navigate to the project folder**
```bash
cd Crop-Disease-Predection
```

**3. Create a virtual environment** *(recommended)*
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 📸 How It Works

```
Step 1 → User registers or logs in to the system
Step 2 → User selects their preferred language (English / Telugu / Hindi)
Step 3 → User uploads a crop leaf image
Step 4 → The AI model preprocesses and analyzes the image
Step 5 → CNN predicts the crop disease class
Step 6 → Results display the disease name, confidence score & solutions
Step 7 → User can optionally submit feedback
```

---

## 🧠 AI Model

The system uses a **Convolutional Neural Network (CNN)** trained on the rice plant disease dataset.

- **Model file:** `model/crop_model.h5`
- **Framework:** TensorFlow / Keras
- **Input:** RGB crop leaf image
- **Output:** Disease class label + confidence score

### Diseases Currently Supported

| # | Disease          | Description                            |
|---|------------------|----------------------------------------|
| 1 | Bacterial Blight | Water-soaked lesions along leaf edges  |
| 2 | Brown Spot       | Oval brown spots scattered on leaves   |
| 3 | Leaf Smut        | Angular black or powdery leaf patches  |

---

## 🔮 Future Improvements

- [ ] Expand dataset to include more crop types (wheat, maize, potato)
- [ ] Improve CNN accuracy with transfer learning and data augmentation
- [ ] Support additional regional languages (Tamil, Kannada, Marathi)
- [ ] Build a mobile application (Android / iOS)
- [ ] Real-time camera-based disease detection
- [ ] Offline mode for areas with limited connectivity

---

## 👨‍💻 Author

**Pragada Sai Ramesh**

- 🐙 GitHub: [@sairamesh-7](https://github.com/sairamesh-7)
- 📁 Repository: [Crop-Disease-Predection](https://github.com/sairamesh-7/Crop-Disease-Predection)

---

## 📜 License

```
MIT License

Copyright (c) 2026 sairamesh-7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  Made with ❤️ for farmers across India 🌾
</div>
