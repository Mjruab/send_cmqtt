import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.write("Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")

# ✅ Restaurado: on_message que tenías originalmente
def on_message(client, userdata, message):
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "157.230.214.127"
port = 1883

def publish_message(topic, message_dict):
    client = paho.Client(f"MJ-HUB-{int(time.time())}")  # ✅ ID único
    client.on_publish = on_publish
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_start()
    message = json.dumps(message_dict)
    ret = client.publish(topic, message)
    ret.wait_for_publish()
    client.loop_stop()
    client.disconnect()

st.title("MQTT Control")

if st.button('ON'):
    publish_message("MJmqtt_s", {"Act1": "ON"})  # ✅ topic corregido
    st.success("Enviado: ON")

if st.button('OFF'):
    publish_message("MJmqtt_s", {"Act1": "OFF"})
    st.success("Enviado: OFF")

values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    publish_message("MJmqtt_a", {"Analog": float(values)})
    st.success(f"Enviado: {values}")
