# 📊 Customer Churn Prediction Project

## 🔍 Overview

This project predicts whether a customer is likely to churn (leave a service) based on their demographic and service usage data. It helps businesses take proactive actions to retain customers.

---

## 🎯 Business Problem

Customer churn leads to revenue loss. Acquiring new customers is more expensive than retaining existing ones.

### Goals:

* Identify customers likely to churn
* Understand key churn factors
* Improve customer retention strategies

---

## 🗂 Dataset

* Dataset: Telco Customer Churn
* Total Records: 7043
* Features Used:

  * tenure_yeo_trim
  * gender_Male
  * Partner_Yes
  * PhoneService_Yes
  * Contract_One year
  * Contract_Two year
  * PaperlessBilling_Yes
  * PaymentMethod_Credit card (automatic)
  * PaymentMethod_Electronic check
  * PaymentMethod_Mailed check

---

## ⚙️ Data Preprocessing

* Removed irrelevant columns
* Handled categorical variables using One-Hot Encoding
* Applied Yeo-Johnson transformation for normalization
* Outlier treatment using IQR method
* Feature selection using Variance Threshold
* Data balancing using SMOTE
* Feature scaling using StandardScaler

---

## 🤖 Model Building

Models tried:

* K-Nearest Neighbors
* Naive Bayes
* Logistic Regression ✅ (Best)
* Decision Tree
* Random Forest

### Final Model:

* Logistic Regression
* Accuracy: ~78%

---

## 🚀 Deployment

* Framework: Flask
* Frontend: HTML/CSS
* Backend: Python (Flask)

### How it Works:

1. User inputs customer details
2. Data is processed & scaled
3. Model predicts churn
4. Output displayed on UI

---

## 📁 Project Structure

```
customer_churn_project/
│
├── app.py
├── customer_churn.pkl
├── standard_scalar.pkl
├── templates/
│   └── index.html
├── notebook/
│   └── Customer_churn.ipynb
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install flask numpy pandas scikit-learn
   ```
3. Run the app:

   ```bash
   python app.py
   ```
4. Open browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📈 Results

* Logistic Regression performed best among all models
* Balanced dataset improved prediction performance
* Model successfully predicts churn vs non-churn

---

## 🧠 Future Improvements

* Use Pipeline for automation
* Add more features for better accuracy
* Deploy on cloud (AWS / Render / Heroku)
* Improve UI/UX

---

## 👨‍💻 Author

Gujjula Umamaheswara Reddy

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
