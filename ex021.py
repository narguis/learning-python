# Play an mp3 file

import pygame

pygame.init()
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
