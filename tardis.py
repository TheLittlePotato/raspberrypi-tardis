#############################################################################
#   This program tries to simulate Tardis noises to make you feel awesome   #
#                                                                           #
#   At launch, it will play the takeoff sound, then randomly play a noise   #
#   every 5 to 15 minutes. This is far from perfect, so please copy and do  #
#   whatever the Hell you want with this code and do cool things :)         #
#                                                                           #
#   This code was tested on a Raspberry Pi 3 B+ with Raspberry Pi OS. The   #
#   sounds are included in the repo, dont forget to change the paths.       #
#                                                                           #
#   Mélodie Vibert                                                          #
#   November 20th 2023                                                      #
#############################################################################


import pygame
import random
import threading
import time

#Init pygame
pygame.init()
pygame.mixer.init()

#Setup audio channels
pygame.mixer.set_num_channels(8)
takeoffLandingSound = pygame.mixer.Channel(1)
ambientSound = pygame.mixer.Channel(2)
clock = pygame.time.Clock()

#Setup sounds
tardis_takeoff1 = pygame.mixer.Sound('/home/pi/sounds/tardis_take_off1.wav')
tardis_takeoff2 = pygame.mixer.Sound('/home/pi/sounds/tardis_take_off2.wav')
tardis_landing = pygame.mixer.Sound('/home/pi/sounds/tadis_landing_short.wav')
tardis_cloister_bell = pygame.mixer.Sound('/home/pi/sounds/tardis_cloister_bell.wav')
tardis_denied = pygame.mixer.Sound('/home/pi/sounds/tardis_denied.wav')
tardis_malfunctioning = pygame.mixer.Sound('/home/pi/sounds/tardis_malfunctioning.wav')
silence = pygame.mixer.Sound('/home/pi/sounds/silence.wav')
dalek_control_room = pygame.mixer.Sound('/home/pi/sounds/dalek_control_room.wav')

#Sound lists
takeoffList = [tardis_takeoff2, tardis_takeoff1, tardis_malfunctioning]
noisesList = [tardis_cloister_bell, tardis_denied, dalek_control_room, silence]

#Takeoff function
def takeoff(event):
    takeoffLandingSound.play(random.choices(takeoffList, weights = [85, 10, 5], k = 1)[0])
    #Wait for takeoff before anything else
    while pygame.mixer.Channel(1).get_busy():
        pygame.event.poll()
        clock.tick(10)
    event.set()

#Random noise function
def randomNoise():
    ambientSound.play(random.choices(noisesList, weights = [88, 7, 4, 1], k = 1)[0])

#Create Event to check if takeoff is finished
takeoffEvent = threading.Event()
#Initial takeoff thread
initialThread = threading.Thread(target=takeoff, args=(takeoffEvent,), daemon=True)
initialThread.start()

#Wait for takeoff
while not takeoffEvent.isSet():
    takeoffEvent.wait(0.75)

#Main loop
while True:
    #Initialize timer for random noise
    randomNoiseInterval = random.uniform(0, 600)
    print("Next sound in", ((randomNoiseInterval + 300) / 60), "minutes!")
    timerThread = threading.Timer(300 + randomNoiseInterval, randomNoise)
    timerThread.start()
    print(timerThread.isDaemon())

    #Wait for random noise to play
    while not timerThread.finished.is_set():
        time.sleep(0.75)

    print("I just played a sound!")