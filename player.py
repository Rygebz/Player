import os
import random
import pygame_sdl2 as pygame
import sys
import getch
import multiprocessing
import time

pygame.mixer.init()
path = os.environ['HOME'] +'/music'

def music_load(path):
	music = []
	for filename in os.listdir(path):
		if filename.endswith('.ogg'):
			music.append(os.path.join(path, filename))
	return music


music = music_load(path)
choice_music = random.randrange(0, len(music))
pygame.mixer.music.load(music[choice_music])
autoplay = False
filename = "none"
choice = multiprocessing.Value('i', 0)

def loop(cho):
	while(True):
		char = getch.getch()
		cho.value = int(char)

p = multiprocessing.Process(target=loop, args=(choice,))
p.start()

print("Random music - 1, Stop - 2, resume - 3, Mute - 4, Unmute - 5, Autoplay - 6, Exit - 7\n")
	
while(True):
	ch = choice.value
	if ch == 1:
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		print("Playing:\n" + filename)
	elif ch == 2:
		pygame.mixer.music.pause()
		print("Music is paused")
	elif ch == 3:
		pygame.mixer.music.unpause()
		print("Music is unpaused")
	elif ch == 4:
		pygame.mixer.music.set_volume(0.0)
		print("Music is muted")
	elif ch == 5:
		pygame.mixer.music.set_volume(1.0)
		print("Music is unmuted")
	elif ch == 6:
		autoplay = not autoplay
		print("Autoplay set to " + repr(autoplay))
	elif ch == 7:	
		sys.exit()
	if autoplay == True and pygame.mixer.music.get_busy() == 0:
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		print("Playing:\n" + filename)
	choice.value = 0
	time.sleep(0.3)
