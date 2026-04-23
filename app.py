import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.write("Versión de Python:", platform.python_version())

broker = "157.230.214.127"
port = 1883

def on_publish(client, userdata, result):
    print("el dato ha sido publicado \n")

def publish_message(topic, message):
    client = paho.Client(f"MJ-HUB-{int(time.time())}")
    client.on_publish = on_publish
    client.connect(broker, port)
    client.loop_start()                    # ✅ Inicia el loop de red
    ret = client.publish(topic, message)
    ret.wait_for_publish()                 # ✅ Espera a que se publique
    client.loop_stop()                     # ✅ Detiene el loop limpiamente
    client.disconnect()                    # ✅ Desconecta correctamente

st.title("MQTT Control")

if st.button('ON'):
    message = json.dumps({"Act1": "ON"})
    publish_message("MJmqtt_s", message)
    st.success("Enviado: ON")

if st.button('OFF'):
    message = json.dumps({"Act1": "OFF"})
    publish_message("MJmqtt_s", message)
    st.success("Enviado: OFF")

values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    message = json.dumps({"Analog": float(values)})
    publish_message("MJmqtt_a", message)
    st.success(f"Enviado: {values}")
