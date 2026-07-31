# 🚦 AI Smart Traffic Optimization Project

## 📌 Project Overview

The AI Smart Traffic Optimization Project is an intelligent traffic management system that uses Machine Learning, Time Series Forecasting, and Computer Vision (YOLOv8) to analyze traffic conditions, predict congestion levels, detect vehicles from traffic videos, and provide traffic management recommendations.

The project aims to improve urban traffic flow by leveraging AI-based techniques for congestion prediction and traffic optimization.

---

## 🎯 Objectives

- Analyze traffic datasets using Exploratory Data Analysis (EDA).
- Predict traffic congestion levels using Machine Learning algorithms.
- Forecast future traffic trends.
- Detect and count vehicles using YOLOv8.
- Estimate traffic density.
- Provide AI-based traffic recommendations.
- Build an interactive Streamlit web application.

---

## 🚀 Features

- 📊 Data Preprocessing
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning Models
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost
- 📉 Traffic Forecasting
- 🚗 YOLOv8 Vehicle Detection
- 🚦 Traffic Density Estimation
- 💡 AI Traffic Recommendations
- 🌐 Streamlit Dashboard

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- OpenCV
- Ultralytics YOLOv8
- Streamlit
- Joblib

---

## 📂 Project Structure

```
AI-Smart-Traffic-Optimization-Project/
│
├── app.py
├── Traffic_Project.ipynb
├── requirements.txt
├── traffic_cleaned.csv
├── traffic_forecast.csv
├── traffic_model.pkl
├── road.mp4
├── output_detection.mp4
├── AI_Report.txt
├── traffic_report.txt
├── Vehicle_Distribution.png
└── README.md
```

---

## 📊 Dataset

The project uses a traffic dataset containing:

- DateTime
- Junction
- Vehicles

Additional features such as:

- Year
- Month
- Day
- Hour
- DayOfWeek

were generated during preprocessing.

---

## 🤖 Machine Learning Models

The following classification models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 🚗 Vehicle Detection

YOLOv8 is used for:

- Car Detection
- Bus Detection
- Truck Detection
- Motorcycle Detection

The processed video includes:

- Bounding Boxes
- Vehicle Count
- Traffic Density Estimation

---

## 🌐 Streamlit Dashboard

The dashboard allows users to:

- Enter traffic parameters
- Predict traffic congestion
- View AI-generated traffic recommendations

Run the application using:

```bash
streamlit run app.py
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Rishika14104/AI-Smart-Traffic-Optimization-Project.git
```

Move into the project folder:

```bash
cd AI-Smart-Traffic-Optimization-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```
# Output :


---

## 📈 Future Enhancements

- Live CCTV traffic monitoring
- Real-time traffic prediction
- Google Maps integration
- Emergency vehicle prioritization
- Smart traffic signal control using Reinforcement Learning
- Cloud deployment

---

## 👩‍💻 Author

**Kosireddy Rishika**

B.Tech – Computer Science & Engineering

Visvesvaraya College of Engineering and Technology

Hyderabad, Telangana, India

---

## 📜 License

This project is developed for educational and academic purposes.
