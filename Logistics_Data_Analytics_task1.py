import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
df = pd.read_csv("logistics_shipments_demo.csv")
# Cleaning
df["weight_kg"] = df["weight_kg"].fillna(df["weight_kg"].median())
df["tracking_available"] = df["tracking_available"].fillna("Unknown")
# KPI features
df["delay_days"] = df["actual_days"] - df["planned_days"]
df["on_time"] = np.where(df["actual_days"] <= df["planned_days"], 1, 0)
df["cost_per_km"] = df["transport_cost_inr"] / df["distance_km"]
# Route-level summary
route_summary = df.groupby(["origin", "destination"]).agg(
shipments=("shipment_id", "count"),
avg_delivery_days=("actual_days", "mean"),
on_time_rate=("on_time", "mean"),
avg_cost=("transport_cost_inr", "mean")
).reset_index()
print(route_summary)
# Regression
X = df[["distance_km", "weight_kg"]]
y = df["transport_cost_inr"]
model = LinearRegression().fit(X, y)
# Clustering
features = df[["distance_km", "weight_kg",
"transport_cost_inr", "vehicle_utilization_pct"]]
df["cluster"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(features)