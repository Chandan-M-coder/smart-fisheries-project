import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Smart Fisheries Dashboard", layout="wide")

# Title
st.title("🐟 Smart Fisheries Monitoring System")

st.markdown("### Real-time Water Quality & Feeding Recommendation")

# Sidebar inputs
st.sidebar.header("Enter Water Parameters")

temp = st.sidebar.slider("Temperature (°C)", 0, 40, 28)
ph = st.sidebar.slider("pH Level", 0.0, 14.0, 7.5)
turbidity = st.sidebar.slider("Turbidity", 0, 50, 10)
oxygen = st.sidebar.slider("Oxygen Level (mg/L)", 0.0, 10.0, 5.0)

# Display metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡 Temperature", f"{temp} °C")
col2.metric("💧 pH Level", ph)
col3.metric("🌊 Turbidity", turbidity)
col4.metric("🫧 Oxygen", oxygen)

# Prediction logic
if oxygen < 4:
    status = "❌ Unsafe"
    color = "red"
elif temp < 25:
    status = "⚠ Moderate"
    color = "orange"
else:
    status = "✅ Safe"
    color = "green"

st.markdown(f"## Water Status: :{color}[{status}]")

# Feeding recommendation
st.subheader("🐟 Feeding Recommendation")

if oxygen < 4:
    st.error("Do NOT feed fish (Low Oxygen)")
elif temp < 25:
    st.warning("Feed less (Low Temperature)")
elif temp > 32:
    st.info("Feed moderately")
else:
    st.success("Feed normally")

# Graph section
st.subheader("📊 Water Parameters Graph")

data = {
    "Parameter": ["Temperature", "pH", "Turbidity", "Oxygen"],
    "Value": [temp, ph, turbidity, oxygen]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.bar(df["Parameter"], df["Value"])
ax.set_title("Water Quality Parameters")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Developed by Chandan 🚀")
st.subheader("🐟 Smart Feeding System")

# Inputs
num_fish = st.number_input("Number of Fish", value=100)
avg_weight = st.number_input("Average Fish Weight (kg)", value=0.5)

# --- WHEN TO FEED (Decision) ---
if oxygen < 4:
    feed_status = "❌ Do NOT feed (Low Oxygen)"
    allow_feed = False
elif temp < 20:
    feed_status = "⚠ Feed very less (Too Cold)"
    allow_feed = True
elif temp > 32:
    feed_status = "⚠ Feed moderately (High Temp)"
    allow_feed = True
else:
    feed_status = "✅ Feed normally"
    allow_feed = True

st.markdown(f"### Feeding Decision: {feed_status}")

# --- HOW MUCH TO FEED (Quantity) ---
if temp < 20:
    feed_percent = 0.01
elif temp < 25:
    feed_percent = 0.02
elif temp <= 30:
    feed_percent = 0.03
else:
    feed_percent = 0.025

total_weight = num_fish * avg_weight
feed_amount = total_weight * feed_percent

# --- OUTPUT ---
st.subheader("📦 Feed Quantity")

st.write(f"Total Fish Biomass: {total_weight:.2f} kg")
st.write(f"Feeding Rate: {feed_percent*100}%")

if allow_feed:
    st.success(f"Feed {feed_amount:.2f} kg per day")
else:
    st.error("Feeding stopped due to unsafe conditions")
