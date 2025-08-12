# Reflection Journal: Temperature Logger Project

**Student:** Alex Student
**Project:** Temperature and Humidity Logger

## Introduction

My project goal is to create a device that can log the temperature and humidity in my room over time. I want to see how the temperature changes throughout the day and night. The plan is to use a DHT11 sensor with a Raspberry Pi Pico, have a Python script read the data every 15 minutes, and save it to a CSV file on the Pico. This will help me learn about hardware interfacing, data logging, and working with files in MicroPython.

## Development Log & AI Interactions

### Day 1: Getting the Sensor to Work

**My Process:**
My first step was just to get a reading from the DHT11 sensor. I've never used one before. I wired it up according to a tutorial I found online. I connected the VCC to 3.3V, GND to GND, and the data pin to GP15.

I then asked the AI for help with the initial code.

**My Prompt to the AI:**
> "Hello! I'm a student learning Python and I'm using a Raspberry Pi Pico with the Thonny IDE. I have a DHT11 temperature sensor connected to GP15. I need to write a MicroPython script that reads the temperature and humidity from the sensor. Can you provide the basic code to do just that one thing? Please include comments explaining each part of the code."

**AI's Response & My Thoughts:**
The AI gave me a simple script that imported the `dht` and `machine` libraries, set up the sensor on pin 15, and then called `sensor.measure()` inside a loop. It was really helpful that the code was commented, as it explained *why* each line was there. I ran the code and it worked on the first try! I could see the temperature and humidity printing in the Thonny console. This was a great first step.

### Day 2: The Data Logging Problem

**My Process:**
Next, I wanted to save the data to a file. This was much harder than I expected. I tried to modify the script myself first. I knew I needed to use `open()`, `write()`, and `close()`, but I kept getting errors.

**My Prompt to the AI:**
> "Here is my current MicroPython code: `[...pasted my working code from day 1...]`. I want to write the temperature and humidity readings to a CSV file on the Pico called `data.csv`. The file should have three columns: `timestamp`, `temperature_C`, and `humidity`. Can you show me how to modify my main loop to open the file in 'append' mode, write a new line with the data, and then close it?"

**AI's Response & My Thoughts:**
The AI's suggestion was to use `with open('data.csv', 'a') as f:`. This was a great tip, because it automatically handles closing the file even if there's an error. It also showed me how to format the string with the current time using `utime.localtime()`. I had a `TypeError` at first because I was trying to add numbers and strings, but I remembered the debugging guide and asked the AI about that specific error. It told me to convert all my variables to strings using `str()` before joining them. That fixed it.

### Day 3: Final Touches & Reflection

**My Process:**
Today I cleaned up the code and added more comments for myself. I let the logger run for a few hours to collect data. I then used Thonny to download the `data.csv` file from my Pico to my computer and opened it in Excel. It worked! I could see all the data points and I made a simple chart showing the temperature changing over time.

## Final Reflective Essay

This project was a great learning experience. The most challenging part was figuring out the file I/O on the Pico. I spent about an hour getting errors before I asked the AI for help. The AI was most helpful when I gave it very specific questions, like when I pasted my exact error message. When I just said "it's broken," the AI gave me very generic advice. This taught me that being specific is key.

I learned a lot about how sensors work and how to handle their data in Python. I also learned that debugging is a process of elimination. The `print()` statement is still the most useful tool! Seeing my code actually interact with a physical sensor and create a real data file was much more satisfying than just doing a software-only project.

For next steps, I would like to add a small LCD screen to the project to display the current temperature in real-time, without needing to plug it into a computer. I could also add a button that, when pressed, triggers an immediate reading. This assignment has given me more confidence to try more complex hardware projects in the future.
