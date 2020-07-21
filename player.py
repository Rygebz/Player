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
oldfilename = "none"
choice = multiprocessing.Value('i', 0)
muted = "No"
paused = "No"
status = ""

def loop(cho):
	while(True):
		char = getch.getch()
		cho.value = int(char)

p = multiprocessing.Process(target=loop, args=(choice,))
p.start()

print("Random music - 1, Stop - 2, resume - 3, Mute - 4, Unmute - 5, Autoplay - 6, Exit - 7\n\n")
	
while(True):
	ch = choice.value
	if ch == 1:
		sys.stdout.write('\r'+ (20 + len(oldfilename)) * " ")
		oldfilename = filename
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		paused = "No"
	elif ch == 2:
		pygame.mixer.music.pause()
		paused = "Yes"
	elif ch == 3:
		pygame.mixer.music.unpause()
		paused = "No"
	elif ch == 4:
		pygame.mixer.music.set_volume(0.0)
		muted = "Yes"
	elif ch == 5:
		pygame.mixer.music.set_volume(1.0)
		muted = "No"
	elif ch == 6:
		autoplay = not autoplay
	elif ch == 7:	
		print("\nExiting...\n")
		p.terminate()
		os._exit(0)
		quit()
	if autoplay == True and pygame.mixer.music.get_busy() == 0:
		sys.stdout.write('\r'+ (20 + len(oldfilename)) * " ")
		oldfilename = filename
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		paused = "No"

	print("\033[F" + 36 * " ")
	print("\033[FMuted=" + muted + " Paused=" + paused + " Autoplay=" + repr(autoplay))
	# sys.stdout.write('\r'+ 10 * " ")
	status = "Playing: " + os.path.basename(filename)
	sys.stdout.write('\r'+ (5 + len(filename)) * " ")
	sys.stdout.write('\r'+status)
	choice.value = 0
	time.sleep(0.3)
