import os
import random
import pygame_sdl2 as pygame
import sys
import getch
import multiprocessing
import time
import signal

pygame.mixer.init()
path = os.environ['HOME'] +'/Music'

choice = 1

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

# Executed on Ctrl-C
def signal_handler(sig, frame):
	p.terminate()
	print('Ctrl+C detected: Exiting')
	os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

def loop(cho):
	while(True):
		char = getch.getch()
		try:
			cho.value = int(char)
		except ValueError:
			print("Invalid number. Try again...")

p = multiprocessing.Process(target=loop, args=(choice,))
p.start()

print("\nRandom music - 1, \nStop - 2, \nresume - 3, \nMute - 4, \nUnmute - 5, \nAutoplay - 6, \nExit - 7\n")

while True:
	ch = choice.value
	if ch == 1:
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		print("Playing:\n" + os.path.basename(filename))
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
		print("\nExiting...\n")
		p.terminate()
		os._exit(0)
		quit()
	if autoplay == True and pygame.mixer.music.get_busy() == 0:
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		print("Playing:\n" + os.path.basename(filename))
	choice.value = 0
	time.sleep(0.3)
