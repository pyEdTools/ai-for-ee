# Project Ideas

This document provides a comprehensive list of potential projects that can be assigned to students. Each project includes a tangible verification method, ensuring students connect their software with a real-world or demonstrable outcome. The complexity can be scaled to suit different student levels.

---

### Turn signals on a car
- **Description:** Animated sequential turn signals for cars using multiple LEDs. Ask the user their turn directions, then visualize an LED-based turn signal. Build a circuit with an LED and some switches for options of turn signals.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Traffic lights simulator
- **Description:** LED traffic light simulator that manages the lights for all four directions.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Circuit resistance calculator
- **Description:** Implement series and parallel circuits in Python. Provide series, parallel, and custom modes where the user can enter multiple resistors. Compute and output the effective resistance for each case.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Weather analysis
- **Description:** Collect temperature data (via sensor or web), plot graphs of temperature patterns over a week, highlight special events, and let the user choose which visualizations to see.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Electric vehicle batteries
- **Description:** Calculate EV energy consumption and cost (Wh/kWh). Collect battery specs into spreadsheets, analyze cost, efficiency, and power delivery in Python, and generate performance graphs per battery type.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Energy consumption vs solar panel analysis
- **Description:** Ask the user about their energy consumption, estimate costs, solar cell count and payoff time. Plot solar payback curves vs. usual energy costs.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### What’s the time?
- **Description:** Predict time of day from solar cell voltage-current data. Load multiple data files, predict their timestamps, and plot time vs. power alongside a battery-powered clock comparison.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Energy bill app
- **Description:** Python app to calculate and predict household appliance energy consumption. Users select appliances, view usage and cost graphs, and forecast next month’s energy bill.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Automated irrigation systems algorithm
- **Description:** Use soil moisture sensor data to generate PWM motor outputs that automate water pump flow for optimal moisture maintenance.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Logic gate detector
- **Description:** Load circuit I/O voltage data, analyze it in Python to identify whether the circuit functions as AND, OR, NOT, NAND, or NOR.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Brain tumor detection
- **Description:** Process brain MRI scans in Python to detect tumor patterns. Convert images to matrices, identify tumor regions algorithmically, and visualize results with marked regions.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Face detection analysis
- **Description:** Collect data from online face detectors, analyze dominant features, image categories, and accuracy in Python, then plot feature-usage statistics.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Predict circuit structure
- **Description:** Infer resistive circuit layouts (series, parallel, combination) from voltage-current measurements by solving circuit equations and presenting matching diagrams.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Color detector
- **Description:** Process color images in Python to find user-selected colors. Perform color-space conversions and matrix operations to highlight chosen colors in the image.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Algorithmic LED patterns
- **Description:** Generate LED patterns (blinking, fading, chasing) with Python that mirror a four-LED circuit. Include EV-LED pattern info in the app.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### RGB LED color mixing
- **Description:** Simulate RGB LED color mixing in Python. Users input a target color; compute resistor values for a real RGB LED, build the circuit, and verify model predictions.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Circuit analyzer
- **Description:** Let users build virtual circuits (resistors, capacitors) step by step in Python, calculate total resistance or capacitance, and save circuit data to a file.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Resistor color code decoder
- **Description:** GUI-based Python app to select resistor color bands and display the corresponding resistance value and tolerance.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Speaker noise filter design
- **Description:** Assist in designing speaker noise filters. Users input cutoff frequencies; Python computes resistor and capacitor values. Optionally validate with a real speaker circuit.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Low-pass filter design
- **Description:** Design a speaker low-pass filter using resistors and capacitors.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### High-pass filter design
- **Description:** Design a speaker high-pass filter using resistors and capacitors.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### IR sensor data cleanup
- **Description:** Stabilize IR sensor readings in Python via noise filters. Let users choose filter strength, then plot raw vs. filtered distance over time.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### I-V curve plotter
- **Description:** Plot and analyze current-voltage curves in Python. Input measured data, graph the I-V curve, and compute threshold voltage, max power point, and degradation rates.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Solar cell analysis
- **Description:** Analyze monthly solar cell voltage-current data to find max power points. Compute P=V×I, plot power vs. time, and correlate peaks with time or weather.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Temperature monitor
- **Description:** Use Arduino to log temperature data over multiple days, then read the CSV in Python to plot thresholds, max/min labels, and detect trends per user choice.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### PWM motor controller analyzer
- **Description:** Generate and simulate PWM signals in Python to control motor speed and torque, with options for home-automation use cases.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Py-scilloscope
- **Description:** Python signal generator and oscilloscope simulator. Generate sine, square, triangle waves, allow frequency/amplitude control, and simulate circuit I/O.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Automatic night light
- **Description:** Simulate a motion-activated night light in Python. Users input motion levels; the program adjusts brightness accordingly.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Automatic water filter
- **Description:** Control water dispensing via Python and sensor input. Detect bottle placement, dispense/stop based on sensor or timeout, and increment a dispense counter.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Bike movement analysis
- **Description:** Collect gyroscope data (roll, pitch, yaw) on a bike ride, analyze patterns and power-accuracy trade-offs in Python, and plot motion variables over time.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Nerf gun optimization
- **Description:** Predict PWM signals for nerf blaster motors to optimize power, velocity, and stability. Visualize signals in Python and validate on hardware.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Energy time-keeper app
- **Description:** Read activity logs (activity, start/end times) in Python, compute electrical energy per category over a week, and graph time vs. energy consumption.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Noise cancelling
- **Description:** Remove noise from recorded audio files in Python, graph frequency components, and highlight removed frequencies.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Sound amplification
- **Description:** Amplify specific frequencies in audio files with Python, graph frequency and intensity, and optionally build a transistor amplifier to match software results.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### EV braking analysis
- **Description:** Predict EV stopping distances under various braking conditions. Simulate braking with IR sensors and LEDs, then plot performance in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### RC car EV simulator
- **Description:** Analyze RC car voltage-efficiency data, compare to EVs, and plot efficiency comparisons using Python.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Battery performance comparison
- **Description:** Measure voltage over time for multiple batteries, analyze performance statistics in Python, and plot key markers.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Water turbine performance
- **Description:** Analyze water turbine motor data in Python.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Solar panel tracking simulation
- **Description:** Generate PWM signals to rotate a solar panel toward its max power angle in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### EE curriculum advisor
- **Description:** Use Python to survey user interests and recommend EE major tracks and technical courses.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Memory usage analyzer
- **Description:** Analyze memory usage across RAM, GPU, and cache for various file types in Python, reporting distributions and metrics.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Cybersecurity simulation
- **Description:** Simulate encryption, storage, and decryption flows in a cybersecurity stack with Python, offering scenario options and summaries.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Crop sustainability predictor
- **Description:** Collect soil moisture and plant growth data, analyze crop sustainability in Python, plot moisture vs. longevity, and optionally build a sensor circuit.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Laptop heat analysis
- **Description:** Record PC heat levels under various workloads, analyze and predict temperature profiles with Python, and graph power vs. heat over time.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Speaker recording analysis
- **Description:** Record audio via a speaker circuit, analyze loudness and frequency properties in Python, and provide interactive waveform visualizations.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Power outage simulation
- **Description:** Simulate a power outage circuit with LEDs and motor, log voltage/current data, and analyze regulator performance in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Self-driving radar simulation
- **Description:** Build a 360° IR sensor array to mimic vehicle radar, collect obstacle voltages/distances, and visualize readings in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Motion sensing light
- **Description:** Create a motion-sensing LED circuit, log performance data, and analyze circuit vs. commercial device outputs in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Phone rotation analysis
- **Description:** Log phone rotation angles and screen behavior, analyze triggers with Python, and graph rotation properties alongside gyroscope voltages.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Smart cruise control
- **Description:** Collect GPS and speed limit data to simulate cruise control logic in Python, plotting suggested speeds and restrictions.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### PC temperature profiling
- **Description:** Monitor PC component temperatures under varied tasks, analyze heating/cooling requirements in Python, and compare profiles.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Voice recognition analysis
- **Description:** Record multiple voices, analyze audio waveforms and frequencies with Python to study voice recognition systems, and plot distinguishing features.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Power monitoring system
- **Description:** Build a sensor-based power monitor, collect real-time voltage/current data, and visualize power usage in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Encrypted circuit communications
- **Description:** Implement encrypted messaging with Python and a SOS-LED demonstration, with optional GUI for key management.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Battery management system
- **Description:** Read battery cell voltage/temperature in Python, adjust parameters for efficiency, and present interactive graphs.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Self-driving path planner
- **Description:** Implement grid-based path planning algorithms in Python for autonomous vehicles with multiple map scenarios.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Phone battery analysis
- **Description:** Analyze phone battery performance data in Python, graph statistics, and provide user-driven visualizations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Self-driving braking system
- **Description:** Build a wheeled cart with IR sensors to measure braking response, log data, and analyze braking patterns in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Automotive warning system
- **Description:** Build an analog sensor warning circuit, log temperature data, and analyze warning performance in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Morse code translator
- **Description:** Create a Python Morse code translator with LED/buzzer circuit demonstration.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Voltage multiplier analysis
- **Description:** Design diode-capacitor voltage multipliers, collect voltage/current data, and analyze error/noise with Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Architectural power modeling
- **Description:** Model a 3D-printed structure’s power needs in Python, allow user component selection, and verify predictions with measurements.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Tic-Tac-Toe LED game
- **Description:** Light up LEDs on a tic-tac-toe board with Python logic and simulate gameplay via switch inputs.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Music note analyzer
- **Description:** Measure musical notes with a circuit and analyze soundwaves with Python for accuracy feedback.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### PID control simulation
- **Description:** Simulate PID motor speed control with encoder feedback in Python, optionally validate with hardware tests.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Wind impact on solar energy
- **Description:** Analyze solar cell performance under varying wind and temperature conditions in Python.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Sleep-synchronized lighting
- **Description:** Simulate lighting schedules based on user sleep preferences in Python and visualize on/off patterns.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Renewable energy data analysis
- **Description:** Collect and analyze data from three renewable sources in Python, visualize costs and performance metrics.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Car speed control
- **Description:** Use encoder feedback to simulate PWM-based DC motor speed control in Python and graph performance metrics.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Phone brightness modeling
- **Description:** Analyze phone ambient light sensor data in Python to study brightness adjustment behavior and battery impact.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### EV brand performance comparison
- **Description:** Compare Tesla vs. Toyota EV battery performance data in Python with query-driven visualizations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Power grid simulation
- **Description:** Simulate California’s power grid in Python, analyze distribution scenarios, and visualize system dynamics.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Comprehensive battery analysis
- **Description:** Calculate battery performance and cost in Python, analyze efficiency and power delivery, and build a verification circuit.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Voice assistant application
- **Description:** Design a Python voice assistant that processes voice inputs and summarizes audio properties.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Ultrasonic radar
- **Description:** Build an ultrasonic IR radar system, collect obstacle motion data, and analyze detection properties in Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Solar-powered clock simulator
- **Description:** Simulate a solar-charged clock in Python using I-V curves and optionally build a physical prototype.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Water flow efficiency analysis
- **Description:** Model and solve water flow equations for dispensers in Python, analyze efficiencies, and visualize results.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Automatic door analysis
- **Description:** Collect data on automatic door operation and analyze sensor range, accuracy, and performance with Python.
- **Hardware Components:** Microcontroller (Pico or Arduino) and relevant sensors/actuators (e.g., LEDs, motors, sensors).

---

### Weather analysis
- **Description:** Output highest and lowest temperatures recorded, average temperature, number of rainy days, and days forecast as dry but with rainfall. Visualize and report using real-world weather data.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Real estate analysis
- **Description:** Histogram of for-sale houses per state. Output the most expensive house overall, the most expensive in a user-selected state, and average prices by state.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Movie rating analysis
- **Description:** Compute average ratings for three movies by matching movie IDs across two CSV files, then visualize the results.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Employment analysis
- **Description:** Output top three majors by employment, average unemployment and employment rates for a specific job, and averages by major category.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Steak cook preference analysis
- **Description:** Determine average preferred steak doneness percentage from votes, and allow users to record their own preference.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Contact Book
- **Description:** Read, add, delete, and modify contact entries in a file, then save updates back to the file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Gradebook
- **Description:** Allow teachers to input student grades across subjects, calculate averages, and retrieve individual performance.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Password Manager
- **Description:** Store and retrieve passwords securely with encryption in a simple command-line tool.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Calculator
- **Description:** Perform addition, subtraction, multiplication, and division. Store the last three results in a file and display history on demand.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Flashcard quizzer
- **Description:** Create and manage a Q&A file. Users can add cards or take a quiz, then receive a score.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Rock Paper Scissors
- **Description:** Play rock-paper-scissors against the computer. Maintain win/loss score in a file, display and update before each game.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Birthdays Reminder
- **Description:** Store friends’ birthdays in a file sorted chronologically. Output the next and furthest upcoming birthdays and days until each, or a specific person’s birthday.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Work logger
- **Description:** Log daily work hours in a file. Calculate monthly earnings at minimum wage, add visual reports, multi-employee support, and a live timesheet.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Dictionary creator
- **Description:** Maintain a word dictionary. Users can look up definitions or list words starting with a given letter.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Hangman
- **Description:** Play hangman with random words loaded from a file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Tic Tac Toe
- **Description:** Play tic-tac-toe vs. computer. Store and display win/loss record in a file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Music Playlist Creator
- **Description:** Create, load, edit, and save music playlists. Track listening statistics and visualize listening history.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Address Book
- **Description:** Store, retrieve, add, edit, search, and delete personal contact details in a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Student Grade Management System
- **Description:** Command-line tool to manage and analyze student grades with add/view/average features, saving to and loading from JSON.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Movie Watchlist
- **Description:** Manage a watchlist of movies: add titles, mark as watched, rate/review entries.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Number guesser
- **Description:** Guess a random number with 'very cold' to 'very hot' hints. Record attempts per game in a file and show the last game’s attempt count.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Blackjack
- **Description:** Play Blackjack (21) vs. computer. Display and update win/loss record stored in a file at each game’s start and end.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Coin toss game
- **Description:** Simulate coin tosses vs. computer, display and update score in a text file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Recipe suggester
- **Description:** Suggest recipes based on user-provided ingredients. Provide an exploration menu and realistic recipes from a database.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### News Aggregator
- **Description:** Compile top news from real-world APIs by user preference. Navigate via menu and adapt recommendations based on stored user scores.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Currency Converter
- **Description:** Convert currencies using a public API. Visualize rate trends over time for selected currency pairs.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Trivia quiz game
- **Description:** Play trivia from a question database. Display score and optional end-game fact sheet based on answered questions.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Fitness tracker
- **Description:** Log daily activity and diet, show progress graphs, workout summaries, and dietary recommendations over multiple days.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### E-commerce platform
- **Description:** Display products, reviews, and orders. Implement shopping cart and order summaries, saving data to files with optional visualizations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Russian Roulette
- **Description:** Simulate Russian Roulette vs. computer.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Car sale finder
- **Description:** Recommend cars from a database/CSV based on cost, ratings, and user criteria.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Password manager
- **Description:** Generate, store, and retrieve passwords across websites. Securely write to and load from an encrypted file. Optionally visualize common passwords.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Adventure text game
- **Description:** Interactive story with puzzle items to solve challenges.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Baseball player analysis
- **Description:** Fetch and visualize baseball player stats from a dataset, highlighting interesting facts.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### SimSteam platform
- **Description:** Manage owned games file, record hours played, levels, achievements, and visualize consolidated data.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Task Scheduler
- **Description:** Add, edit, and delete tasks with deadlines. Display priority based on proximity to the current date.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Recipe Cookbook
- **Description:** Display, search, and add recipes from a CSV/TXT file via a menu interface.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Workout Generator
- **Description:** Recommend workouts by body part or full routines from a CSV database.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Car performance finder
- **Description:** Recommend cars based on performance criteria specified by the user.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Mortgage analyzer
- **Description:** Visualize historical mortgage rate trends. Analyze future payments based on user input and stored expense rates.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Activity Guide
- **Description:** Ask the user questions to recommend activities in a chosen city, reading activity options from a CSV file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Air Quality checker
- **Description:** Display historical and current air quality for your area by reading and updating a CSV of previous checks.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Electric vehicle charging cost calculator
- **Description:** Calculate EV charging costs at various stations based on battery capacity, target charge percentage, and travel distance.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Morse Code translator
- **Description:** Translate text to and from Morse code, save translation history to a file, and allow viewing past translations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Notepad
- **Description:** Read, append, find, replace, and delete words in a text or CSV file via a simple notepad interface.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### QR Generator
- **Description:** Manage a CSV of names and links, generate and display QR codes for a selected person and link using Matplotlib.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Palindrome checker
- **Description:** Read words from a CSV file and identify which entries are palindromes, then display the results.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Goldbach's conjecture
- **Description:** Given an even number >5, output pairs of primes that sum to it and record input and results to a file.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Song recommender
- **Description:** Ask the user questions to recommend three songs from a CSV/database, with options to add new songs and prevent duplicates.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Make your own dice for board games
- **Description:** Simulate dice of various types, allow custom dice creation, record rolls to a file, and visualize faces and probability distributions.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### CatCard interface
- **Description:** Duplicate CatCard functionalities in Python: add funds, check balance, report lost card, access resources, and chart expense distributions.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Pavilion menu generator
- **Description:** Automate UC Merced Pavilion dining menus (breakfast, lunch, dinner) ensuring nutritional balance, fun items, and write weekly tables to a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Gacha simulator
- **Description:** Simulate gacha game mechanics and rates.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Wordle game
- **Description:** Implement Wordle using a CSV of valid words.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Speedometer Calculator
- **Description:** Calculate required speed given start, destination, and time constraints using city-distance data from a CSV.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Video game recommender
- **Description:** Recommend video games by querying a CSV database based on user preferences.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Battleship game
- **Description:** Play Battleship with randomly placed ships; track and display scores between user and computer from a file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Bobcat Shuttle Tracker
- **Description:** Simulate Bobcat Shuttle locations, update positions via loops, read initial data from a file, and visualize routes.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Library Resource Locator
- **Description:** Help students find and reserve study rooms, computers, or books in Kolligian Library using dictionaries and file-based availability.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### UCM Event Calendar
- **Description:** Fetch and display UC Merced events from an .ics file, sort by category, and save organized calendars for offline use.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Course Schedule Optimizer
- **Description:** Optimize student course schedules based on preferences (free days, professors, requirements) and save viable combinations to a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Housing Roommate Matcher
- **Description:** Match roommates based on stored profiles and preferences, outputting compatible pairs saved for future reference.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Text adventure
- **Description:** Navigate a text-based world with puzzles, timed challenges, and file-driven random events based on player input.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Financial Aid Calculator
- **Description:** Estimate student costs and aid using conditional logic, output detailed breakdowns saved to a text file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### ProfRateUCM
- **Description:** Allow students to rate and comment on professors/courses, calculate averages, and save top-rated lists and visualizations to a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Merced Outdoors Trip Planner
- **Description:** Plan trips around Merced by selecting hiking trails, lakes, and campsites, generating itineraries saved to a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Alphabet game
- **Description:** Guess a random letter by indicating if the target is before or after the guess, with a timer and fastest-time logging.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### UCM Club Finder
- **Description:** Match student interests to campus clubs using dictionaries and save recommended lists for later.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Research Opportunity Finder
- **Description:** Compile and filter research positions by department or skills, outputting lists saved to a file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Cypher Decoder
- **Description:** Encode and decode messages with variable-letter shifts, generating and applying a shift key for each character.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Car building program
- **Description:** Select car models and parts, calculate total cost, and output a bill of materials.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Akinator implementation
- **Description:** Guess user-chosen characters via yes/no questions, logging history of correct and incorrect guesses.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Music tracker
- **Description:** Log per-user song plays with artist, title, and rating; rank songs by mean rating and plot histograms of artist rankings.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Poker probability
- **Description:** Compute win counts for poker hands from a dataset file and report per-player outcomes.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Gas trip requirement calculator
- **Description:** Calculate required gas for a trip given engine specs or car model and trip distance.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Wheel of Fortune
- **Description:** Emulate Wheel of Fortune using puzzles from a CSV/TXT file, store and display game results.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### DeskFinder
- **Description:** Reserve desks for time slots, display availability and future reservations, updating a CSV/TXT file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Jeopardy game
- **Description:** Play Jeopardy with questions loaded from a CSV/TXT file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### English to Spanish Translation
- **Description:** Translate English text to Spanish, caching past translations in a file and checking before translating.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Star catalog
- **Description:** Explore constellations, star sizes, colors, and distances via a prompt-driven interface.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Buzzfeed Quizzes
- **Description:** Run three multiple-choice quizzes (car, computer, phone) from TXT files, require all answers, and report correctness.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Turbos and Superchargers
- **Description:** Analyze turbocharger and supercharger operation modes and suggest improvements via code.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Geo Distance guesser
- **Description:** Game: guess distances between two random locations within 20% error or study mode to compute distances using geopy.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Weightlifting exercises recommender
- **Description:** Recommend exercises by muscle group from a CSV/TXT file of available routines.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Fruit tree success calculator
- **Description:** Determine fruit tree viability by USDA zone, rainfall, and temperature using city and plant data files.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Soccer statistics app
- **Description:** Provide player stats, reports, visualizations, and fun facts for soccer data.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Python linter
- **Description:** Implement a command-line Python linter to analyze code style and report issues.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Largest Prime Factor
- **Description:** Compute and cache largest prime factor for numbers <100, storing inputs and results in a CSV.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Estimate Pi
- **Description:** Use Monte Carlo sampling to estimate π, output the estimate, and plot sampled points.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Fibonacci Sequence Generator
- **Description:** Generate the Fibonacci sequence up to a given limit, explore performance of different methods, and report timings.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Newton's Method for Root Finding
- **Description:** Implement Newton’s method with adjustable guesses and tolerances, output roots, and plot the function.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Traveling Salesman Problem Solver
- **Description:** Solve the TSP using heuristic methods (e.g., nearest neighbor), output the shortest path and distance.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Random Walk Simulator
- **Description:** Simulate and visualize 2D or 3D random walks, exploring step size and dimensional effects.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Simple Encryption Algorithms
- **Description:** Encrypt and decrypt text using Caesar and Vigenère ciphers, and compare algorithm strengths and weaknesses.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Maze Solver
- **Description:** Solve mazes with DFS/BFS algorithms and visualize the solved path.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Choice game
- **Description:** Branching narrative game allowing player choices that lead to different endings.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Game Theory Simulations
- **Description:** Simulate game theory scenarios like Prisoner’s Dilemma, reporting strategy performance stats.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Simple Weather Simulator
- **Description:** Use mathematical models and historical data to simulate and predict weather patterns.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Loan Calculator
- **Description:** Calculate loan payments and generate amortization schedules, exploring rate and frequency impacts.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Statistics Calculator
- **Description:** Compute mean, median, mode, standard deviation, etc., visualize results, and save to CSV.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Enigma Machine
- **Description:** Replicate Enigma machine encryption by mapping alphabetic input through rotor configurations, allowing message scrambling and unscrambling using accurate rotor combinations.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Jumper.io
- **Description:** Manage event guest lines: add/remove people, view queue status, and verify payment.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Invisible map adventure
- **Description:** Navigate an unseen map similar to Oregon Trail, avoid traps, track deaths and completion time; levels read from CSV.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Loot collector game
- **Description:** Control a spaceship to collect loot using arrow keys; track and display current and high scores.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Ping Pong game
- **Description:** Play ping pong with score persistence: load scores at start and save results at end.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Color calculator
- **Description:** Combine two primary colors (red, yellow, blue) to produce secondary hues, with extended color mixing options.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Timer reminder
- **Description:** Set a message and time to trigger a reminder notification at the specified time.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Fish Bait Sorter
- **Description:** Select from a predefined list of bait types, manage a favorites list, ensuring no duplicates, and check bait categories (live/artificial).
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Fast Food Ordering Simulator
- **Description:** Select a restaurant, load menu from CSV, place orders, and calculate total cost.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Housing Campus converter
- **Description:** Calculate living expenses for on/off campus housing including commuting costs based on distance and gas price inputs.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Average technological output of college freshman
- **Description:** Analyze and visualize average time spent on academic vs. personal technology use using Matplotlib.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Age/Food Simulator
- **Description:** Recommend healthy or unhealthy food based on user age, height, gender, nationality, and weight statistics, with a follow-up health survey.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Cake ordering form
- **Description:** Capture contact details, calculate cake order price, and suggest premade flavors.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Fun/Personality quizzes
- **Description:** Offer multiple personality quizzes from CSV; update and store result tallies for each outcome.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Class progress visualizer
- **Description:** Input quiz scores for a class, then display a histogram of score distribution using Matplotlib.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Product analyzer
- **Description:** Plot sales history from CSV; allow users to select a product and view its sales trend line chart.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Attendance tracker
- **Description:** Manage attendance records for a class CSV, mark daily presence, and visualize attendance rates per student.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Pattern memorizing game
- **Description:** Show a letter pattern briefly, then prompt user recall; increase length each round, record highest score in CSV.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Spell Checker
- **Description:** Identify misspelled words in user text or file input, suggest corrections interactively.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### PR Weight Tracker
- **Description:** Track personal record lifts (bench, squat, deadlift) via CSV, update when broken, and generate reports and visualizations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Scientific calculator
- **Description:** Perform basic arithmetic and trigonometric functions (sin, cos, tan) and log calculation history to a text file.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### 7/11 Dice game
- **Description:** Simulate the 7-11 dice game with Pygame, maintain and display score history.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Crime rate calculator
- **Description:** Compute crimes per 100,000 population based on user-input crime counts and population.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Stress Analysis on Materials
- **Description:** Simulate stress-strain curves for materials under tensile, compressive, and shear loads, plot curves, and generate fatigue reports.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Solar Panel Efficiency Calculator
- **Description:** Calculate solar panel efficiency under varying conditions (angle, weather, time) and plot daily efficiency graphs with summary.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Electrical Circuit Solver
- **Description:** Use Kirchhoff’s laws to compute currents and voltages in circuits; explore effects of components and output distributions and CSV reports.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Energy Consumption Reporter
- **Description:** Model and optimize building energy usage based on insulation, HVAC, and weather; generate daily/monthly consumption charts.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Material Life Cycle Analysis
- **Description:** Assess environmental impact of materials from production to disposal, outputting impact scores and selection recommendations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Message encoder
- **Description:** Encrypt and decrypt text messages with a key; share encoded messages for recipients with the correct key.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Skateboard part recommender
- **Description:** Recommend skateboard components for custom builds based on user requirements.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Logo Guess quiz
- **Description:** Identify brand logos in a quiz format.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Text Adventure game
- **Description:** Collect tokens through mini-games (word, number, puzzle) in a text-based adventure.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Food recommender
- **Description:** Suggest food items based on user-specified qualities.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Housing Roommate Finder
- **Description:** Match roommates by comparing student profiles and preferences, output saved match lists.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Video game recommender
- **Description:** Recommend games by platform, genre, player count, and duration from user preferences.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Periodic Table lookup
- **Description:** Display element properties by name or symbol.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Bobcat Shuttle Tracker
- **Description:** Simulate and display Bobcat shuttle locations and routes, update positions dynamically.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Vehicle Service Tracker
- **Description:** Record vehicle service history (mileage, year, make, model) and output maintenance logs.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Go Fish card game
- **Description:** Play Go Fish vs. computer; track win/loss history.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Soccer Code
- **Description:** Analyze and generate soccer-related code patterns.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Russian Roulette
- **Description:** Simulate Russian Roulette game against the computer.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Higher and Lower Game
- **Description:** Guess a hidden number by higher/lower prompts; log guess time to file.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Blackjack
- **Description:** Play Blackjack with deck manipulation, Ace valuation rules, and persistent scoring.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### Trajectory Calculator
- **Description:** Compute 2D and 3D projectile trajectories from initial velocity vectors.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Shoe size comparer
- **Description:** Compare shoe size data for men and women and identify patterns.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Food Ordering simulator
- **Description:** Simulate restaurant ordering workflows.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Club Finder
- **Description:** Match student interests to campus clubs using stored club data.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Energy consumer
- **Description:** Analyze building energy consumption based on IVAC settings and weather inputs.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Personal Finance summary
- **Description:** Track user expenses and income, set savings goals, and recommend spending cuts.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Athlete Player stats
- **Description:** Self-rate athlete skills and compute overall ratings from input skill approximations.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Time Management App Project
- **Description:** Mobile app to organize tasks, schedules, and time usage.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Rock paper scissors game
- **Description:** Play rock-paper-scissors vs. computer with persistent scoring.
- **Verification Method:** Demonstrate a fully playable and functional game session, showing all core mechanics working as described.

---

### GI Character Analyzer
- **Description:** Analyze Genshin Impact team stats including characters, weapons, levels, and effects.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---

### Interactive Program
- **Description:** Handle directional movement and quaternion rotations via user input.
- **Verification Method:** Demonstrate the simulation running for multiple scenarios. The output should be clear, textual or visual, proving the core logic is implemented correctly.

---

### Workout Planner
- **Description:** Generate weekly workout plans by splitting days and targeting muscle groups with recovery schedules and dietary options.
- **Verification Method:** The program must generate a data visualization (e.g., a plot or chart using a library like Matplotlib) or a formatted data table that clearly presents the analysis results.

---
