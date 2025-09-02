import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="3G UMTS Network Visualizer", layout="wide")

st.title("📡 3G / UMTS Radio Network Live Visualizer")

st.sidebar.header("Simulation Controls")
num_users = st.sidebar.slider("Number of Users", 1, 10, 3)
spreading_factor = st.sidebar.slider("Spreading Factor", 2, 16, 8)
distance = st.sidebar.slider("User Distance from Base Station (km)", 0.1, 5.0, 1.0, 0.1)
qos_class = st.sidebar.selectbox("QoS Class", ["Conversational", "Streaming", "Interactive", "Background"])

# -------------------
# CDMA Spreading Simulation
# -------------------
chips = np.random.choice([-1, 1], spreading_factor)
data_bits = np.random.choice([-1, 1], num_users)

spread_signals = [bit * np.tile(chips, 1) for bit in data_bits]
composite_signal = np.sum(spread_signals, axis=0)

st.subheader("🔑 CDMA Spreading & Despreading")
fig, ax = plt.subplots()
ax.plot(composite_signal, label="Composite Signal (Multiple Users)")
ax.plot(spread_signals[0], label="User 1 Spread Signal")
ax.legend()
st.pyplot(fig)

# -------------------
# Power Control Simulation
# -------------------
path_loss = 1 / (distance ** 2)
tx_power = np.linspace(0.1, 1.0, num_users)
received_power = tx_power * path_loss

st.subheader("⚡ Power Control")
fig, ax = plt.subplots()
ax.bar(range(num_users), received_power)
ax.set_xlabel("Users")
ax.set_ylabel("Received Power")
st.pyplot(fig)

# -------------------
# Handover Simulation
# -------------------
cell_a_power = np.random.uniform(0.4, 1.0) / (distance)
cell_b_power = np.random.uniform(0.4, 1.0) / (5 - distance)

handover = "Cell A" if cell_a_power > cell_b_power else "Cell B"

st.subheader("📶 Handover Decision")
st.write(f"At {distance:.1f} km, user connects to **{handover}**")

fig, ax = plt.subplots()
ax.bar(["Cell A", "Cell B"], [cell_a_power, cell_b_power])
ax.set_ylabel("Signal Strength")
st.pyplot(fig)

# -------------------
# QoS Classes
# -------------------
qos_mapping = {
    "Conversational": {"Latency": "Very Low", "Data Rate": "Medium"},
    "Streaming": {"Latency": "Low", "Data Rate": "High"},
    "Interactive": {"Latency": "Medium", "Data Rate": "Medium"},
    "Background": {"Latency": "High", "Data Rate": "Low"},
}

st.subheader("🎯 QoS Class Simulation")
st.write(f"**Selected QoS Class:** {qos_class}")
st.write(f"- Latency: {qos_mapping[qos_class]['Latency']}")
st.write(f"- Data Rate: {qos_mapping[qos_class]['Data Rate']}")
