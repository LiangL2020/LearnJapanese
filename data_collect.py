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

# variables
running = True
drawing = False 
radius = 5 
draw_color = BLACK 
last_pos = None 

romaji = {
    'a': 4, 'i': 2, 'u': 2, 'e': 4, 'o': 3, 
    'ka': 3, 'ki': 2, 'ku': 3, 'ke': 6, 'ko': 3, 
    'sa': 5, 'shi': 3, 'su': 5, 'se': 4, 'so': 3, 
    'ta': 5, 'chi': 2, 'tsu': 6, 'te': 6, 'to': 4, 
    'na': 3, 'ni': 5, 'nu': 4, 'ne': 4, 'no': 3, 
    'ha': 4, 'hi': 5, 'fu': 3, 'he': 3, 'ho': 4, 
    'ma': 5, 'mi': 5, 'mu': 6, 'me': 3, 'mo': 5, 
    'ya': 6, 'yu': 4, 'yo': 3, 
    'ra': 5, 'ri': 6, 'ru': 5, 're': 3, 'ro': 2, 
    'wa': 2, 'wo': 5, 
    'n': 4}

def select_weighted_romaji():
    # total_count = sum(romaji.values()) + 1  
    weights = [1 / (count + 1) for count in romaji.values()]  
    return random.choices(list(romaji.keys()), weights=weights, k=1)[0]

current_romaji = select_weighted_romaji()
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


def draw_romaji():
    screen.fill(WHITE)
    text_surface = font.render(current_romaji, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

# initialize pygame
pygame.init()

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Handwriting Panel")
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
                draw_romaji() 
            elif event.key == pygame.K_UP:  # increase brush size
                radius = min(radius + 1, 8)
            elif event.key == pygame.K_DOWN:  # decrease brush size
                radius = max(3, radius - 1)
            elif event.key == pygame.K_q:  # press 'Q' to exit 
                running = False 
            elif event.key == pygame.K_RETURN:  # save drawing to file
                romaji[current_romaji] += 1
                file_path = os.path.join(data_dir, f"{current_romaji}_{romaji[current_romaji]}.png")
                pygame.image.save(screen, file_path)
                current_romaji = select_weighted_romaji()
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
print(romaji)