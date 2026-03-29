# Azure-based Demand Forecasting and Capacity Optimization System

## 📌 Overview

The **Azure-based Demand Forecasting and Capacity Optimization System** is an end-to-end data-driven solution designed to predict cloud resource demand and support intelligent infrastructure planning.

This project evolves from a **data analysis and machine learning prototype (Milestones 1–3)** into a **production-ready forecasting system (Milestone 4)** that includes:

* Machine Learning models for demand prediction
* Real-time prediction API deployment
* Automated forecasting pipeline
* Interactive Power BI dashboard for decision support

The system helps organizations:

* Predict future demand accurately
* Optimize resource allocation
* Reduce operational costs
* Enable proactive infrastructure scaling

---

## 🎯 Objectives

* Forecast cloud resource demand using historical data
* Compare multiple ML models (ARIMA, XGBoost, Random Forest)
* Deploy the best-performing model as an API
* Generate real-time and batch predictions
* Build a dashboard for capacity planning decisions
* Enable monitoring and scalability for production use

---

## 🧱 Project Architecture

```
Data Collection → Data Cleaning → Feature Engineering → Model Training
→ Model Evaluation → Model Deployment (FastAPI)
→ Forecast Generation → Power BI Dashboard → Decision Making
```

---

## 📊 Dataset

The dataset contains cloud usage and operational metrics such as:

* Timestamp (time-based usage)
* Service Type (Compute, Storage, Networking)
* Usage Units (actual demand)
* Provisioned Capacity
* Cost (USD)
* Availability %
* Cloud Spend Index
* Enterprise Demand Index
* Regional Data (US-East, US-West, India-South)

---

## ⚙️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Statsmodels (ARIMA)
* FastAPI (API Deployment)
* Uvicorn
* Power BI (Dashboard)
* Git & GitHub
* Render (Deployment)

---

## 🚀 Milestone-wise Implementation

---

### ✅ Milestone 1 – Data Collection & Understanding

* Collected Azure demand dataset
* Identified key variables affecting demand
* Performed exploratory data analysis

---

### ✅ Milestone 2 – Data Cleaning & Feature Engineering

* Handled missing values and duplicates
* Standardized formats
* Created time-based features:

  * hour, day, month, week
* Created lag features and rolling statistics

---

### ✅ Milestone 3 – Model Development & Evaluation

Trained and compared multiple models:

* ARIMA (Time Series Model)
* Random Forest
* XGBoost

Evaluation Metrics:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* Forecast Bias

✔ Final Model Selected: **Random Forest (Tuned)**

✔ Performed:

* Hyperparameter tuning (GridSearchCV)
* Backtesting
* Model comparison

---

### ✅ Milestone 4 – Deployment & Integration

#### 🔹 1. Model Deployment (API)

* Built API using FastAPI (`app.py`)
* Endpoint: `/predict`
* Accepts input data and returns forecast

Example:

```
POST /predict
```

✔ Deployed on Render:
👉 https://azure-based-demand-forecasting-and.onrender.com
👉 https://azure-based-demand-forecasting-and.onrender.com/docs

---

#### 🔹 2. Batch Prediction Pipeline

* Implemented `batch_predict.py`
* Generates predictions for dataset
* Output file:

```
forecast_output.csv
dashboard_final.csv
```

---

#### 🔹 3. Power BI Dashboard

Developed an interactive dashboard for:

* Forecast vs Actual Demand
* Capacity Utilization
* Region-wise Demand Analysis
* Service-wise Demand Analysis
* Capacity Gap Identification

Key Insights:

* Identify regions needing scaling
* Compare predicted vs actual demand
* Optimize infrastructure allocation

---

#### 🔹 4. Monitoring & Scalability

* Model performance can be monitored using prediction accuracy
* System supports retraining with new data
* Designed for scalable cloud deployment

---

## 📁 Project Structure

```
.
├── app.py                          # FastAPI deployment
├── batch_predict.py               # Batch prediction script
├── dashboard_final.csv            # Final dataset for dashboard
├── forecast_output.csv            # Prediction output
├── rf_model.pkl                   # Trained model
├── requirements.txt               # Dependencies
├── render.yaml                    # Deployment config
├── index.html                     # Optional UI
├── azure_demand_raw.csv
├── azure_demand_cleaned.csv
├── azure_demand_feature_engineered.csv
├── Milestone-2.ipynb
├── Milestone-3.ipynb
├── Updated Milestone-3.ipynb
└── README.md
```

---

## 📊 Dashboard Insights

The dashboard answers key business questions:

* Which region requires more infrastructure?
* Is current capacity sufficient?
* When should scaling be done?
* Which services drive demand?
* How accurate are predictions?

---

## 🎥 Demo Video

```
https://drive.google.com/file/d/1NvST483IIgcMYljqFl2P3dh9gQPWHh_Z/view?usp=sharing
```

---

## ⚡ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/Supraja-Potluri/Azure-based-Demand-Forecasting-and-Capacity-Optimization-System.git
cd Azure-based-Demand-Forecasting-and-Capacity-Optimization-System
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run API

```
uvicorn app:app --reload
```

### 4. Run Batch Prediction

```
python batch_predict.py
```

---

## 📈 Expected Outcomes

* Accurate demand forecasting
* Optimized resource allocation
* Reduced cloud operational costs
* Data-driven infrastructure decisions
* Scalable forecasting system

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.
