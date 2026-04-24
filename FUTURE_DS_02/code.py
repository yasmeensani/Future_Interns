import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv", encoding='latin1')

# Fix column names (remove spaces/newlines)
df.columns = df.columns.str.strip()

# Fix TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Drop missing values
df = df.dropna()

# -------------------------------
# 📊 1. Churn Count
# -------------------------------
churn = df['Churn'].value_counts()
churn.plot(kind='bar')
plt.title("Churn Count")
plt.savefig("churn.png")
plt.show()

# -------------------------------
# 💰 2. Monthly Charges vs Churn
# -------------------------------
df.groupby('Churn')['MonthlyCharges'].mean().plot(kind='bar')
plt.title("Monthly Charges vs Churn")
plt.savefig("monthly_charges.png")
plt.show()

# -------------------------------
# 📄 3. Contract vs Churn
# -------------------------------
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar')
plt.title("Contract vs Churn")
plt.savefig("contract.png")
plt.show()

# -------------------------------
# ⏳ 4. Tenure vs Churn
# -------------------------------
df.groupby('Churn')['tenure'].mean().plot(kind='bar')
plt.title("Tenure vs Churn")
plt.savefig("tenure.png")
plt.show()