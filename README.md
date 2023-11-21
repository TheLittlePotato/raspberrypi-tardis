# Tardis (Raspberry Pi Edition)
Do you have a car ? Are you a fan of Doctor Who? Do you ever wish you could escape reality in the Tardis?
Well you're in luck! I wanted to turn my Chevrolet Bolt EUV 2022 into a time machine but couldn't so instead I used a Raspberry Pi to simulate one in my car.

## What is this even supposed to be?
This is my attempt at simulating a Tardis environment in my car by using a Raspberry Pi connected to speakers in my trunk and powered by a power inverter plugged into the front cigarette lighter.

When starting the car, the Raspberry Pi powers on and takes about 30 seconds to launch the Tardis Python program. It starts by playing 1 of 3 Tardis takeoff sounds depending on their probabilities. After that and as long as it's powered, every 5 to 15 minutes it will play 1 of 4 ambiance sounds depending on their probabilities.

I used threads to play the sounds because it's easier to control when the different sounds should play and I plan to implement other features sometimes in the future. Please copy and modify this project to make your own awesome Tardis or custom machine!

## What's the recipe to make this work?
To replicate my setup, you'll need:
- A Raspberry Pi 3 B+ with Raspbian
- A car with a power source for your Raspberry Pi and speakers (like a 12V cigarette lighter & and power inverter or directly tap into a fuse box)
- A set of random computer speakers

You need to copy **tardis.py** and the **sounds** folder somewhere on your Raspberry Pi and make sure the paths for these files in **tardis.py** are correct.

To launch the Tardis Python program on startup, I configured the Raspberry Pi in headless CLI mode and added this at the end of **/home/pi/.bashrc**
```
# Location of the Tardis Python program
sudo python /home/pi/tardis/tardis.py
```
Obviously if you know even a little bit about electronics and coding you can deviate from these steps to make it work for your situation.

## List of stuff I'd like to add
- Use a 3-axis accelerometer to play sounds relative to my movement (materialization when stopping completely, weird sounds when turning abruptly, etc.)
- Add LEDs inside the car to match the current state of the Tardis
- Add buttons inside the car that do cool stuff
- Do some research on the possibility of using the OBD port to retrieve information such as speed, orientation or coordinates that would be more accurate than my own little sensors

Have fun!
