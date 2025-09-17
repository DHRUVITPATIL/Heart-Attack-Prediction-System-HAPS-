# Heart-Attack-Prediction-System-HAPS-
Heart Attack Analysis is a machine learning project that predicts heart attack risk based on clinical data. It includes data preprocessing, feature engineering, model training, evaluation, and visualization of important health factors. The project demonstrates end-to-end predictive analytics in healthcare using Python.
# Heart Attack Prediction System (HAPS)

A modern web-based application built using **Django** and **Machine Learning** that predicts the risk of a heart attack based on user-provided health attributes.  
HAPS aims to provide an easy-to-use, reliable, and fast solution for early risk detection.

---

## 🚀 Features

- **User Authentication:** Secure signup and login functionality.
- **Prediction Form:** Users can input 13 health-related attributes for risk prediction.
- **Machine Learning Integration:** Pre-trained ML model (`heart_model.pkl`) integrated with Django backend.
- **Profile Management:** Users can view and update their profile data.
- **Prediction History:** Each user’s predictions are stored and viewable in their profile.
- **Contact & Feedback:** Users can send feedback or inquiries through a contact page.
- **Responsive Design:** Clean and mobile-friendly interface with consistent styling.

---

## 🛠️ Technologies Used

- **Backend:** Django (Python Web Framework)
- **Frontend:** HTML, CSS (with custom styles), Bootstrap (optional)
- **Machine Learning:** scikit-learn, pandas, joblib
- **Database:** SQLite (default), can be extended to PostgreSQL/MySQL
- **Authentication:** Django’s built-in User model
- **Others:** Django Admin for managing users and predictions

---

## ⚙️ How It Works

1. User registers and logs in.
2. User fills out a form with 13 health attributes.
3. Input is processed by the machine learning model (`heart_model.pkl`).
4. The system returns whether the user is at risk of heart attack.
5. Prediction is saved to the user’s **Prediction History**, accessible from their profile page.

---

## 📂 Project Structure


