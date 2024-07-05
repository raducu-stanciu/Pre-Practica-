import json
import random
import paho.mqtt.client as mqtt
import time

# Function to generate simulated temperature and humidity data
def generate_data():
    temperature = random.uniform(5.0, 40.0)
    humidity = random.uniform(30.0, 60.0)
    return {"temperature": temperature, "humidity": humidity}

# Callback function when the MQTT client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Failed to connect, return code {rc}")

# MQTT setup
mqtt_broker = "mqtt.beia-telemetrie.ro"  # Replace with your MQTT broker address
mqtt_port = 1883
mqtt_topic = "training/device/Raducu-Stanciu"

client = mqtt.Client()

# Assign the on_connect callback function
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Loop to continuously generate and publish data
try:
    while True:
        data = generate_data()
        payload = json.dumps(data)
        client.publish(mqtt_topic, payload)
        print(f"Published data: {payload}")
        time.sleep(5)  # Wait for 5 seconds before publishing next data
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.disconnect()