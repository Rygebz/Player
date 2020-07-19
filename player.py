import os
import random
import pygame_sdl2 as pygame
import sys
import getch

pygame.mixer.init()
path = os.environ['HOME'] +'/music'

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

print("Random music - 1, Next song - 2, Stop - 3, resume - 4, Mute - 5, Unmute - 6, Exit - 7: \n")
while(choice != 0):
	choice = getch.getch()
	if choice == '1':
		filename = random.choice(music)
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
		print("Playing:\n" + filename)
	elif choice == '2':
		choice_music = random.randrange(0, len(music))
		pygame.mixer.music.load(music[choice_music])
		pygame.mixer.music.play()
		print("Playing:\n" + filename)
	elif choice == '3':
		pygame.mixer.music.pause()
		print("Music is paused")
	elif choice == '4':
		pygame.mixer.music.unpause()
		print("Music is unpaused")
	elif choice == '5':
		pygame.mixer.music.set_volume(0.0)
	elif choice == '6':
		pygame.mixer.music.set_volume(1.0)
	elif choice == '7':
		sys.exit()
	#elif choice == '9':	
		#Autoplay
