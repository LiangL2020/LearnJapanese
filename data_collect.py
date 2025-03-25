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
    'a': 13, 'i': 15, 'u': 10, 'e': 11, 'o': 11, 
    'ka': 12, 'ki': 13, 'ku': 10, 'ke': 12, 'ko': 12, 
    'sa': 12, 'shi': 12, 'su': 10, 'se': 12, 'so': 14, 
    'ta': 13, 'chi': 14, 'tsu': 13, 'te': 14, 'to': 14, 
    'na': 13, 'ni': 13, 'nu': 13, 'ne': 13, 'no': 14, 
    'ha': 12, 'hi': 13, 'fu': 14, 'he': 12, 'ho': 13, 
    'ma': 11, 'mi': 15, 'mu': 11, 'me': 13, 'mo': 12, 
    'ya': 13, 'yu': 11, 'yo': 17, 
    'ra': 13, 'ri': 11, 'ru': 13, 're': 13, 'ro': 12, 
    'wa': 13, 'wo': 14, 'n': 13}

def select_weighted_romaji():
    filtered_romaji = {k: v for k, v in romaji.items() if v < 10}  # Exclude v+ counts
    if not filtered_romaji:
        pygame.quit()
        print(romaji)
        print("All romaji have reached v samples. Resetting counts.")
        for k in romaji.keys():
            romaji[k] = 0  # Reset counts
        filtered_romaji = romaji  # Use all again

    weights = [1 / (count + 1) for count in filtered_romaji.values()]
    return random.choices(list(filtered_romaji.keys()), weights=weights, k=1)[0]

# def select_weighted_romaji():
#     # total_count = sum(romaji.values()) + 1  
#     weights = [1 / (count + 1) for count in romaji.values()]  
#     return random.choices(list(romaji.keys()), weights=weights, k=1)[0]

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