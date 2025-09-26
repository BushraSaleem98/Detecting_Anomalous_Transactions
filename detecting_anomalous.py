# Import required libraries
import pandas as pd
from pyod.models.iforest import IForest
import matplotlib.pyplot as plt

# Load the dataset
transactions = pd.read_csv("transactions.csv")

# Select numerical features for anomaly detection
features = transactions[["TransactionAmount", "TransactionDuration", "AccountBalance"]]

# Train an IForest model with n_estimators parameter
model = IForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(features)

# Add the anomaly scores to the dataset
transactions["Anomaly_Score"] = model.decision_function(features)

# Flag transactions as anomalies based on the model's prediction
transactions["Anomaly"] = (model.predict(features) == 1).astype(int)  # Convert boolean to integer


# Create a summary of anomalous transactions
anomalies_summary = transactions.loc[transactions["Anomaly"] == 1, ["TransactionID", "TransactionAmount", "TransactionDuration", "AccountBalance"]]


# Plot the distribution of TransactionAmount for normal and anomalous transactions
plt.figure(figsize=(8, 6))
transactions[transactions["Anomaly"] == False]["TransactionAmount"].hist(bins=30, alpha=0.5, label="Normal", color="blue")
transactions[transactions["Anomaly"] == True]["TransactionAmount"].hist(bins=30, alpha=0.5, label="Anomalous", color="red")
plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("anomalies_histogram.png")