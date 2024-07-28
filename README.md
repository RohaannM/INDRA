# TEAM INDRA
Intelligent Network for Detection of Street Lights and Remote Assistance

# Smart Streetlight Monitoring System

The Smart Streetlight Monitoring System provides an efficient solution for monitoring and managing streetlights. It leverages ESP32 microcontrollers to collect and transmit data on light levels and current consumption, ensuring timely maintenance and optimal energy usage.

## Features
- **Real-time Monitoring**: Continuous data collection on light levels and current consumption.
- **Wireless Communication**: Uses ESP-NOW protocol for efficient and low-power wireless data transmission.
- **Centralized Processing**: Data from multiple streetlight poles is aggregated and processed centrally.
- **Threshold-based Alerts**: Generates alerts based on predefined light and current thresholds to identify faults.
- **Proactive Maintenance**: Enables timely identification and repair of faulty streetlights, reducing downtime and maintenance costs.

## Components
- **ESP32 Microcontrollers**: Used in each streetlight pole for data collection and transmission.
- **LDR Sensors**: Measure the light levels.
- **Current Sensors**: Measure the current consumption.
- **Central ESP32 (Pole 3)**: Aggregates data from other poles and processes it against thresholds.

## How It Works
1. **Data Collection**: Each pole (ESP32) collects LDR and current values.
2. **Data Transmission**: Data is transmitted wirelessly using the ESP-NOW protocol.
3. **Central Processing**: The central ESP32 (Pole 3) receives data from other poles, checks against thresholds, and sends alerts to the server if any anomalies are detected.
4. **Server Reporting**: The central ESP32 sends the processed data to a server for logging and further analysis.

## Project Setup

### Hardware
1. ESP32 microcontrollers (3 units)
2. LDR sensors (3 units)
3. Current sensors (3 units)
4. Necessary wiring and power supplies

### Software
1. Arduino IDE
2. ESP32 board libraries
3. HTTPClient library

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/smart-streetlight-monitoring.git
   cd smart-streetlight-monitoring
