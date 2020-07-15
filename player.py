import os
import random
import pygame
import sys

pygame.mixer.init()
path = '/home/patross2004/Music/'

choice = 1

def music_load(path):
	music = []
	for filename in os.listdir(path):
		if filename.endswith('.mp3'):
			music.append(os.path.join(path, filename))
	return music


music = music_load(path)
choice_music = random.randrange(1, len(music))
pygame.mixer.music.load(music[choice_music])

while(choice != 0):
	print("Random music - 1, Next song - 2, Previous song - 3, Stop - 4, resume - 5, Mute - 6, Unmute - 7, Exit - 8: \n")
	print("Enter your choice: ")
	choice = input(">")
	if choice == '1':
                filename = random.choice(music)
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
	elif choice == '2':
		choice_music = random.randrange(0, len(music))
		pygame.mixer.music.load(music[choice_music])
		pygame.mixer.music.play()
	elif choice == '3':
		choice_music -= 1
		choice_music = random.randrange(0, len(music))
		pygame.mixer.music.load(music[choice_music])
		pygame.mixer.music.play()
	elif choice == '4':
		pygame.mixer.music.pause()
		print("Music is paused")
	elif choice == '5':
		pygame.mixer.music.unpause()
		print("Music is unpaused")
	elif choice == '6':
		pygame.mixer.music.set_volume(0.0)
	elif choice == '7':
		pygame.mixer.music.set_volume(1.0)
	elif choice == '8':
		sys.exit()
	#elif choice == '9':	
		#Autoplay
