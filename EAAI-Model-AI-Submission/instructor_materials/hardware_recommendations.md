# Hardware Recommendations

This document provides recommendations for hardware to be used in the "AI Pair Programming with Hardware Verification" assignment. The goal is to use low-cost, accessible, and well-documented components to ensure students can successfully build and verify their projects.

We recommend standardizing on one or both of the following microcontroller platforms.

---

## 1. Primary Microcontroller Platforms

### Raspberry Pi Pico / Pico W

The Pico is a low-cost, high-performance microcontroller from the Raspberry Pi Foundation. Its use of MicroPython makes it an excellent choice for courses where students are already learning or using Python, as they do not need to learn a new language.

- **Key Features:**
    - **Language:** MicroPython (a subset of Python 3).
    - **IDE:** Thonny IDE is recommended for beginners. It's simple and has built-in support for flashing MicroPython to the Pico.
    - **Cost:** ~$4 for the Pico, ~$7 for the Pico W (which includes WiFi).
    - **Strengths:** Python-native, strong documentation, large community, very low cost.
- **Official Website:** [https://www.raspberrypi.com/products/raspberry-pi-pico/](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- **Getting Started Guide:** [https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

### Arduino Uno R3 / R4

The Arduino Uno is arguably the most popular and well-known microcontroller for beginners and hobbyists. It has a massive ecosystem of shields, sensors, and tutorials. It is programmed in C++ using the Arduino framework, which simplifies many common tasks.

- **Key Features:**
    - **Language:** C++ (with the Arduino framework).
    - **IDE:** Arduino IDE (v2 is recommended).
    - **Cost:** ~$25-$30 for official boards, though cheaper clones are widely available.
    - **Strengths:** Extremely robust community support, vast number of tutorials and libraries, very easy to get started with the hardware.
- **Official Website:** [https://store.arduino.cc/products/uno-r4-minima](https://store.arduino.cc/products/uno-r4-minima)
- **Getting Started Guide:** [https://docs.arduino.cc/guides/uno-r4-minima/](https://docs.arduino.cc/guides/uno-r4-minima/)

---

## 2. Recommended Starter Kits

For simplicity, we recommend that students purchase a "starter kit" that includes one of the above microcontrollers along with a variety of common components. This is often cheaper and easier than buying individual parts.

- **Example Kits:**
    - **Elegoo Uno R3 Project Starter Kit:** A very popular and comprehensive kit for the Arduino Uno.
    - **Vilros Raspberry Pi Pico Starter Kit:** A good starting point for the Pico.
    - Many other kits are available on sites like Adafruit, SparkFun, or Amazon. A typical kit should cost between **$30 and $50**.

---

## 3. Common Components List

A good starter kit should include most of the following. These are the components most likely to be used in the suggested projects.

- **Core:**
    - Breadboard (solderless)
    - Jumper Wires (male-male, male-female, female-female)
- **Outputs:**
    - LEDs (various colors: red, green, yellow, blue, white)
    - RGB LED (common cathode or anode)
    - Buzzer (piezo)
    - Small DC Motor
    - Servo Motor
- **Inputs:**
    - Push Buttons / Switches
    - Potentiometers
    - Photoresistors (for light sensing)
- **Sensors:**
    - **Temperature/Humidity:** DHT11 or DHT22
    - **Distance:** HC-SR04 (Ultrasonic) or IR sensor
    - **Moisture:** Soil Moisture Sensor
    - **Motion:** PIR Motion Sensor
- **Passive Components:**
    - Resistors (a variety of values, e.g., 220Ω, 1kΩ, 10kΩ)
    - Capacitors
- **Measurement (Optional but Recommended):**
    - Basic Digital Multimeter (for verifying circuits)
