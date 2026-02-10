import pygame
import time

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

pygame.mixer.music.load('sound/music.mp3')   # or .wav / .ogg
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(loops=-1)             # loop forever (remove -1 to play once)

print("Playing... press Ctrl+C to stop")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("Stopped")