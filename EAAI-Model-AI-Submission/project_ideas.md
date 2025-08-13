# Project Ideas

This document provides a list of potential projects that can be assigned to students. Each project includes a tangible hardware component for verification, ensuring students connect their software with real-world outcomes. The complexity can be scaled to suit different student levels.

---

### 1. Turn Signals on a Car
- **Description:** Create animated sequential turn signals for a car using multiple LEDs. The program can ask the user for their turn direction and then visualize the signal. The project involves building a circuit with LEDs and switches to demonstrate the different turn signal options.
- **Hardware Components:** LEDs, switches, resistors, microcontroller (Pico or Arduino).

---

### 2. Traffic Light Simulator
- **Description:** Develop an LED-based traffic light simulator that correctly manages the light patterns (red, yellow, green) for all four directions of an intersection.
- **Hardware Components:** Red, green, and yellow LEDs; resistors; microcontroller.

---

### 3. Automated Irrigation System
- **Description:** Use data from a soil moisture sensor to create a program that generates PWM motor outputs. This will automate the water pump flow to maintain optimal soil moisture.
- **Hardware Components:** Soil moisture sensor, small water pump (or an LED/motor as a stand-in), microcontroller.

---

### 4. Algorithmic LED Patterns
- **Description:** Generate various LED patterns like blinking, fading, and chasing with Python code that controls a circuit with four or more LEDs. The patterns can be inspired by real-world applications, like those on electric vehicles.
- **Hardware Components:** LEDs, resistors, microcontroller.

---

### 5. RGB LED Color Mixing
- **Description:** Write a program that simulates RGB LED color mixing. The user inputs a target color, and the program computes the necessary resistor values or PWM signals for a real RGB LED. The final step is to build the circuit and verify the color.
- **Hardware Components:** RGB LED, resistors or PWM-capable microcontroller.

---

### 6. Resistor Color Code Decoder
- **Description:** Build a GUI-based application that allows a user to select the color bands on a resistor and then displays the corresponding resistance value and tolerance. The result can be verified with a real resistor and a multimeter.
- **Hardware Components:** A selection of physical resistors, a multimeter.

---

### 7. Speaker Noise Filter Design
- **Description:** Create a tool that assists in designing a simple speaker noise filter (like a low-pass or high-pass filter). The user inputs a cutoff frequency, and the Python script calculates the required resistor and capacitor values. This can be optionally validated with a real speaker circuit.
- **Hardware Components:** Resistors, capacitors, speaker, function generator (optional), oscilloscope (optional).

---

### 8. Temperature Monitor and Logger
- **Description:** Use a microcontroller to log temperature data from a sensor over multiple days. The data is then read by a Python script to plot temperature thresholds, label maximum/minimum values, and detect trends.
- **Hardware Components:** Temperature sensor (e.g., DHT11, TMP36), microcontroller.

---

### 9. PWM Motor Controller
- **Description:** Generate and simulate Pulse-Width Modulation (PWM) signals in Python to control the speed and torque of a small DC motor. The project can be framed around home automation use cases.
- **Hardware Components:** DC motor, motor driver (e.g., L298N), microcontroller.

---

### 10. Automatic Night Light
- **Description:** Create a motion-activated or light-sensitive night light. The program should read from a PIR motion sensor or a photoresistor and turn an LED on or off based on the input.
- **Hardware Components:** PIR sensor or photoresistor, LED, resistors, microcontroller.

---

### 11. Sound Amplification
- **Description:** Write a program to amplify specific frequencies in an audio file. The results can be optionally matched and verified by building a simple transistor-based amplifier circuit.
- **Hardware Components:** Transistor, resistors, capacitors, microphone, speaker.

---

### 12. EV Braking Analysis Simulator
- **Description:** Simulate an EV's braking system using an IR distance sensor and LEDs. As an object gets closer, the "brake light" LED gets brighter. The performance and response can be plotted in Python.
- **Hardware Components:** IR distance sensor, LEDs, resistors, microcontroller.

---

### 13. Solar Panel Tracker
- **Description:** Write a program that generates PWM signals to control servo motors, allowing a small solar panel to rotate and track a light source to maximize its power angle.
- **Hardware Components:** Small solar panel, servo motors, photoresistors, microcontroller.

---

### 14. Self-Driving Radar Simulation
- **Description:** Build a 360° sensor array using IR or ultrasonic sensors to mimic a vehicle's radar system. The program should collect obstacle distance data and visualize the readings in Python.
- **Hardware Components:** IR or ultrasonic sensors, servo motor (for rotation), microcontroller.

---

### 15. Power Monitoring System
- **Description:** Build a sensor-based power monitor to collect real-time voltage and current data from a circuit. The Python script then visualizes the power usage over time.
- **Hardware Components:** Voltage sensor, current sensor (e.g., ACS712), microcontroller.

---

### 16. Battery Management System
- **Description:** Read the voltage and temperature of a battery cell using a microcontroller. The Python program can then analyze the data and present interactive graphs showing the battery's state.
- **Hardware Components:** Battery, voltage sensor, temperature sensor, microcontroller.

---

### 17. Morse Code Translator with Light/Sound
- **Description:** Create a Python program that translates text to and from Morse code. The output should be demonstrated physically using an LED for light signals or a buzzer for sound.
- **Hardware Components:** LED or buzzer, resistors, microcontroller.

---

### 18. Tic-Tac-Toe LED Game
- **Description:** Create a physical Tic-Tac-Toe game. The board is a 3x3 grid of LEDs, and players make their moves using physical buttons or switches. The Python program manages the game logic.
- **Hardware Components:** 9 LEDs, 9 buttons/switches, resistors, microcontroller.

---

### 19. Music Note Analyzer
- **Description:** Use a microphone to measure musical notes being played. The program will analyze the sound waves with Python to provide feedback on the accuracy of the note (e.g., "sharp," "flat," "in tune").
- **Hardware Components:** Microphone/sound sensor module, microcontroller.

---

### 20. Comprehensive Battery Analysis
- **Description:** Calculate battery performance and cost in Python by analyzing efficiency and power delivery. The theoretical results are then verified by building a circuit to measure a real battery's discharge curve.
- **Hardware Components:** Battery holder, various batteries (AA, 9V), multimeter or voltage/current sensors, microcontroller.
