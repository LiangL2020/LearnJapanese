"""
Date: 2/13/2025 
This file pops up a drawing panel for you to draw. 
- use 'C' to clear panel 
- use 'Q' to quit 
- use 'Enter' to save to file 
- use UP and DOWN to resize the brush 
"""
import os 
import pygame
import random

# definitions 
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROMAJI = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo",
    "n"
]
# ga, gi, gu, ge, go,
# za, ji, zu, ze, zo,
# da, ji, zu, de, do,
# ba, bi, bu, be, bo,
# pa, pi, pu, pe, po,
# kya, kyu, kyo,
# sha, shu, sho,
# cha, chu, cho,
# nya, nyu, nyo,
# hya, hyu, hyo,
# mya, myu, myo,
# rya, ryu, ryo,
# gya, gyu, gyo,
# ja, ju, jo,
# bya, byu, byo,
# pya, pyu, pyo

# variables
running = True
drawing = False 
radius = 5 
draw_color = BLACK 
last_pos = None 

romaji_count = {} 
current_romaji = random.choice(ROMAJI)

def draw_romaji():
    """Draws the current Romaji character at the top-center of the screen."""
    text_surface = font.render(current_romaji, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

    if current_romaji not in romaji_count:
        romaji_count[current_romaji] = 1
    else:
        romaji_count[current_romaji] += 1
    

# initialize pygame
pygame.init()

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Handwriting Panel")
screen.fill(WHITE)
font = pygame.font.Font(None, 50)
draw_romaji() 

data_dir = os.path.join('.', 'data', 'hiragana')
os.makedirs(data_dir, exist_ok=True)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # press 'C' to clear screen
                screen.fill(WHITE)
                draw_romaji() 
            elif event.key == pygame.K_UP:  # increase brush size
                radius = min(radius + 1, 8)
            elif event.key == pygame.K_DOWN:  # decrease brush size
                radius = max(3, radius - 1)
            elif event.key == pygame.K_q:  # press 'Q' to exit 
                running = False 
            elif event.key == pygame.K_RETURN:  # save drawing to file
                file_path = os.path.join(data_dir, f"{current_romaji}_{romaji_count[current_romaji]}.png")
                pygame.image.save(screen, file_path)
                current_romaji = random.choice(ROMAJI)
                screen.fill(WHITE)
                draw_romaji() 
                print(f"Drawing saved to {file_path}")
    
    # drawing with mouse movement
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, draw_color, last_pos, mouse_pos, radius * 2)
        last_pos = mouse_pos
    
    pygame.display.update()

pygame.quit()
