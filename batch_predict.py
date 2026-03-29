import pandas as pd
import joblib

# # Load model
# model = joblib.load("rf_model.pkl")

# # Load data
# df = pd.read_csv("azure_demand_feature_engineered.csv")

# # Drop SAME columns used during training
# X = df.drop(columns=["timestamp","usage_units"])

# # Predict
# df["forecast"] = model.predict(X)

# # Save output
# df.to_csv("forecast_output.csv", index=False)

# print("Forecast generated successfully!")


import pandas as pd

# Load your current forecast file
df = pd.read_csv("forecast_output.csv")

# Convert service_type numbers to labels (optional but recommended)
service_map = {
    0: "Storage",
    1: "Compute",
    2: "Networking"
}

df["service_type"] = df["service_type"].map(service_map).fillna(df["service_type"])

# Create proper region column from dummy variables
def get_region(row):
    if row["region_India-South"] == True or row["region_India-South"] == 1:
        return "India-South"
    elif row["region_US-East"] == True or row["region_US-East"] == 1:
        return "US-East"
    elif row["region_US-West"] == True or row["region_US-West"] == 1:
        return "US-West"
    else:
        return "Unknown"

df["region"] = df.apply(get_region, axis=1)

# Save cleaned dashboard file
df.to_csv("dashboard_final.csv", index=False)

print("dashboard_final.csv created successfully!")