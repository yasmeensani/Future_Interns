import pandas as pd
import matplotlib.pyplot as plt

# =========================
# STEP 1: LOAD + FIX DATA
# =========================
df = pd.read_csv("bank-additional-full.csv", header=None)

# Split manually (fix your issue)
df = df[0].str.split(";", expand=True)

# Assign column names
df.columns = [
    'age','job','marital','education','default','housing','loan',
    'contact','month','day_of_week','duration','campaign','pdays',
    'previous','poutcome','emp_var_rate','cons_price_idx',
    'cons_conf_idx','euribor3m','nr_employed','y'
]

# Remove quotes
df = df.applymap(lambda x: str(x).replace('"', '').strip())

print("✅ Data Loaded Successfully")

# =========================
# STEP 2: FUNNEL ANALYSIS
# =========================
total = len(df)
converted = len(df[df['y'] == 'yes'])
not_converted = len(df[df['y'] == 'no'])

conversion_rate = (converted / total) * 100
drop_off = 100 - conversion_rate

print("\n--- 🔍 Funnel Analysis ---")
print("Total Leads:", total)
print("Converted:", converted)
print("Not Converted:", not_converted)
print("Conversion Rate: {:.2f}%".format(conversion_rate))
print("Drop-off Rate: {:.2f}%".format(drop_off))

# =========================
# STEP 3: CHANNEL ANALYSIS
# =========================
channel = df.groupby('contact')['y'].value_counts().unstack()
print("\n--- 📊 Channel Performance ---")
print(channel)

# =========================
# STEP 4: GRAPHS
# =========================

# 1. Conversion Bar Chart
plt.figure()
df['y'].value_counts().plot(kind='bar')
plt.title("Conversion vs Non-Conversion")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.savefig("conversion_bar.png")   
plt.show()


# 2. Pie Chart
plt.figure()
df['y'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Conversion Distribution")
plt.ylabel("")
plt.savefig("conversion_pie.png")   # ✅ SAVE
plt.show()

# 3. Channel Performance
plt.figure()
channel.plot(kind='bar')
plt.title("Conversion by Contact Channel")
plt.xlabel("Channel")
plt.ylabel("Count")
plt.savefig("channel_performance.png")   # ✅ SAVE
plt.show()

# 4. Age Distribution (Converted)
import matplotlib.pyplot as plt

# Clean column names
df.columns = df.columns.str.strip()

# Convert age to numeric (important!)
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Drop null values
df = df.dropna(subset=['age'])

# Plot
plt.figure()
df['age'].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.savefig("age_distribution.png")
plt.show()

# 5. Campaign Impact
plt.figure()
df.groupby('campaign')['y'].value_counts().unstack().head(10).plot(kind='bar')
plt.title("Campaign Impact on Conversion")
plt.xlabel("Number of Contacts")
plt.ylabel("Count")
plt.savefig("campaign_impact.png")   # ✅ SAVE
plt.show()