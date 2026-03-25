import pandas as pd
import joblib

# Load model
model = joblib.load("rf_model.pkl")

# Load data
df = pd.read_csv("azure_demand_feature_engineered.csv")

# Drop SAME columns used during training
X = df.drop(columns=["timestamp","usage_units"])

# Predict
df["forecast"] = model.predict(X)

# Save output
df.to_csv("forecast_output.csv", index=False)

print("Forecast generated successfully!")