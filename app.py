import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.write("Versión de Python:", platform.python_version())
st.title("MQTT Control")

broker = "157.230.214.127"
port = 1883

# ✅ CAMBIA "NOMBRE_TUYO" por algo único (tu nombre, carné, etc.)
# Esto evita conflictos si alguien más tiene el mismo código corriendo
CLIENT_ID = "MARIA_JOSE_CLIENT"

def on_publish(client, userdata, result):
    print("Dato publicado\n")

def get_client():
    """Crea y conecta un cliente MQTT fresco."""
    c = paho.Client(CLIENT_ID)
    c.on_publish = on_publish
    c.connect(broker, port)
    return c

# --- Botones ON / OFF ---
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

# --- Control del servo ---
st.divider()
values = st.slider("Ángulo del servo (0 – 100)", 0.0, 100.0)
st.write("Valor seleccionado:", values)

if st.button("Enviar valor analógico"):
    message = json.dumps({"Analog": float(values)})
    client = get_client()
    client.publish("mjruab2", message)
    client.disconnect()
    st.success(f"Valor {values} enviado al servo ✅")



