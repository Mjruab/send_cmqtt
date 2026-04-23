import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.set_page_config(
    page_title="MQTT Control",
    page_icon="📡",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #fffde7; color: #333333; }
[data-testid="stSidebar"] { background-color: #fff9c4 !important; border-right: 1px solid #f9a825; }
h1 { color: #f57f17 !important; font-weight: 700 !important; }
h2, h3 { color: #e65100 !important; font-weight: 600 !important; }
.stButton > button {
    background: #f9a825 !important; color: #ffffff !important;
    border: none !important; border-radius: 6px !important;
    font-weight: 600 !important; width: 100% !important;
    transition: background 0.2s ease !important;
}
.stButton > button:hover { background: #f57f17 !important; }
[data-testid="metric-container"] {
    background: #fff8e1; border: 1px solid #ffe082;
    border-top: 3px solid #f9a825; border-radius: 8px; padding: 18px 22px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#fff8e1; border:1px solid #ffe082; border-left:5px solid #f9a825;
border-radius:8px; padding:28px 36px; margin-bottom:24px;">
    <h1 style="margin:0; font-size:1.9rem;">📡 MQTT Control</h1>
    <p style="margin:6px 0 0 0; color:#f57f17; font-size:0.97rem;">
        Control de LED y servo motor vía MQTT
    </p>
</div>
""", unsafe_allow_html=True)

st.write("Versión de Python:", platform.python_version())

broker = "157.230.214.127"
port = 1883
CLIENT_ID = "MARIA_JOSE_CLIENT"

def on_publish(client, userdata, result):
    print("Dato publicado\n")

def get_client():
    """Crea y conecta un cliente MQTT fresco."""
    c = paho.Client(CLIENT_ID)
    c.on_publish = on_publish
    c.connect(broker, port)
    return c

st.markdown("### 💡 Control del LED")
col1, col2 = st.columns(2)

with col1:
    if st.button("ON"):
        message = json.dumps({"Act1": "ON"})
        client = get_client()
        client.publish("mjruab1", message)
        client.disconnect()
        st.success("LED encendido ✅")

with col2:
    if st.button("OFF"):
        message = json.dumps({"Act1": "OFF"})
        client = get_client()
        client.publish("mjruab1", message)
        client.disconnect()
        st.success("LED apagado ⭕")

st.divider()
st.markdown("### 🔧 Control del Servo")
values = st.slider("Ángulo del servo (0 – 100)", 0.0, 100.0)
st.write("Valor seleccionado:", values)

if st.button("Enviar valor analógico"):
    message = json.dumps({"Analog": float(values)})
    client = get_client()
    client.publish("mjruab2", message)
    client.disconnect()
    st.success(f"Valor {values} enviado al servo ✅")






