from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("rf_model.pkl")

@app.get("/")
def home():
    return {"message": "Azure Demand Forecasting API Running"}

@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        # ---------- FEATURE ENGINEERING ----------
        df["timestamp"] = pd.to_datetime(df.get("timestamp", pd.Timestamp.now()))

        df["day"] = df["timestamp"].dt.day
        df["hour"] = df["timestamp"].dt.hour
        df["day_of_week"] = df["timestamp"].dt.dayofweek

        # Dummy lag values (approximation for API inference)
        df["lag_1"] = df["provisioned_capacity"] * 0.9
        df["lag_7"] = df["provisioned_capacity"] * 0.85
        df["lag_14"] = df["provisioned_capacity"] * 0.8

        df["rolling_mean"] = df[["lag_1", "lag_7", "lag_14"]].mean(axis=1)

        df["demand_spike"] = (df["enterprise_demand_index"] > 1.2).astype(int)

        # ---------- ENCODING ----------
        df = pd.get_dummies(df, columns=["region", "service_type"], drop_first=True)

        # ---------- MATCH TRAINING FEATURES ----------
        model_features = model.feature_names_in_

        for col in model_features:
            if col not in df.columns:
                df[col] = 0

        df = df[model_features]

        # ---------- PREDICT ----------
        prediction = model.predict(df)

        return {"forecast": prediction.tolist()}

    except Exception as e:
        return {"error": str(e)}