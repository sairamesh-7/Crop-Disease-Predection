# 🌿 Crop Disease Prediction

A web-based application that uses **Artificial Intelligence** and **Deep Learning** to detect crop diseases from leaf images. Farmers and users can upload crop leaf images, and the system predicts the type of disease along with suggested solutions.

> Supports multiple languages — **English**, **Telugu**, and **Hindi** — to make results accessible to farmers across regions.

---

## 🚀 Features

- 👤 User Registration and Login
- 🌍 Multi-language support (English, Telugu, Hindi)
- 📷 Upload crop leaf images
- 🤖 AI-based disease detection using a trained CNN model
- 📊 Prediction confidence score
- 💡 Suggested solutions for detected diseases
- 💬 Feedback system
- 🗄️ SQLite database for storing user data

---

## 🛠️ Technologies Used

| Technology          | Purpose                  |
| ------------------- | ------------------------ |
| Python              | Backend programming      |
| Flask               | Web framework            |
| TensorFlow / Keras  | Deep learning model      |
| HTML                | Frontend structure       |
| CSS                 | User interface styling   |
| JavaScript          | Client-side interaction  |
| SQLite              | Database                 |
| NumPy               | Image processing         |
| Pillow (PIL)        | Image handling           |

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
│   ├── database.db            # SQLite database
│   └── users.db               # User login database
│
├── model/
│   └── crop_model.h5          # Trained AI model
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
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
```

---

## 📊 Dataset

The model was trained using the **Rice Plant Diseases Dataset** available on Kaggle:

🔗 [Rice Plant Diseases Dataset](https://www.kaggle.com/datasets/jay7080dev/rice-plant-diseases-dataset)

The dataset contains labeled images of rice plant leaves across multiple disease categories.

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/sairamesh-7/Crop-Disease-Predection.git
```

**2. Navigate to the project folder**
```bash
cd Crop-Disease-Predection
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📸 How It Works

1. User **registers** or **logs in** to the system
2. User selects their **preferred language**
3. User **uploads** a crop leaf image
4. The **AI model** processes the image
5. The system **predicts** the crop disease
6. Results display the **disease name**, **confidence score**, and **suggested solutions**
7. User can optionally **submit feedback**

---

## 🧠 AI Model

The system uses a **Convolutional Neural Network (CNN)** trained on the rice plant disease dataset.

**Model file:** `model/crop_model.h5`

**Diseases currently supported:**

| Disease          |
| ---------------- |
| Bacterial Blight |
| Brown Spot       |
| Leaf Smut        |

---

## 🔮 Future Improvements

- [ ] Add more crop disease datasets
- [ ] Improve prediction accuracy
- [ ] Support additional languages
- [ ] Mobile application version
- [ ] Real-time camera-based disease detection

---

## 👨‍💻 Author

**Pragada Sai Ramesh**

- 🐙 GitHub: [@sairamesh-7](https://github.com/sairamesh-7)
- 📁 Repository: [Crop-Disease-Predection](https://github.com/sairamesh-7/Crop-Disease-Predection)

---

## 📜 License

This project is developed for **educational and research purposes**.
