# Imports

import pygame
import sys
from tkinter import *
from tkinter import filedialog
from button import Button
import pywhatkit

# Setup

pygame.init()

WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image to ASCII")

# Global variables

BUTTON_SURFACE = pygame.image.load("assets/buttonbackground.png")
BACKGROUND_SURFACE = pygame.image.load("assets/background.png")

# Buttons

LOAD_BUTTON = Button(
	surface=BUTTON_SURFACE, pos=(WIDTH/2-220, 800), width=427, height=120, text_input="Load",
	font=pygame.font.Font("assets/EuclidFlexBold.ttf", 50), base_color="#6fffe9", hovering_color="white"
)

CONVERT_BUTTON = Button(
	surface=BUTTON_SURFACE, pos=(WIDTH/2+220, 800), width=427, height=120, text_input="Convert",
	font=pygame.font.Font("assets/EuclidFlexBold.ttf", 50), base_color="#6fffe9", hovering_color="white"
)

# Button function

def load_button():
	filedialogwindow = Tk()
	filedialogwindow.withdraw()
	filepath = filedialog.askopenfilename(title="Choose your Image")
	filedialogwindow.destroy()
	show_image(filepath)

# Main menu function

def main_menu():
	SCREEN.blit(BACKGROUND_SURFACE, (0, 0))
	LOAD_BUTTON = Button(
		surface=BUTTON_SURFACE, pos=(WIDTH/2, 800), width=427, height=120, text_input="Load",
		font=pygame.font.Font("assets/EuclidFlexBold.ttf", 50), base_color="#6fffe9", hovering_color="white"
	)
	while True:
		current_mouse_pos = pygame.mouse.get_pos()
		LOAD_BUTTON.update(SCREEN)
		LOAD_BUTTON.change_color(current_mouse_pos)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if LOAD_BUTTON.check_for_input(current_mouse_pos):
					load_button()
		

		pygame.display.update()


# Show Image Function

def show_image(file_path):
	SCREEN.blit(BACKGROUND_SURFACE, (0, 0))

	image_to_show = pygame.image.load(file_path)
	image_to_show = pygame.transform.smoothscale(image_to_show, (600/image_to_show.get_height()*image_to_show.get_width(), 600))
	image_rect = image_to_show.get_rect(center=(WIDTH/2, HEIGHT/2-100))

	while True:
		current_mouse_pos = pygame.mouse.get_pos()
		SCREEN.blit(image_to_show, image_rect)
		LOAD_BUTTON.update(SCREEN)
		CONVERT_BUTTON.update(SCREEN)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if LOAD_BUTTON.check_for_input(current_mouse_pos):
					load_button()
				if CONVERT_BUTTON.check_for_input(current_mouse_pos):
					filedialogwindow = Tk()
					filedialogwindow.withdraw()
					saveasfilepath = str(filedialog.asksaveasfilename(title="Save As"))
					filedialogwindow.destroy()
					pywhatkit.image_to_ascii_art(file_path, saveasfilepath)

		LOAD_BUTTON.change_color(current_mouse_pos)
		CONVERT_BUTTON.change_color(current_mouse_pos)
		pygame.display.update()

main_menu()