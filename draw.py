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
    "a": 3, "i": 0, "u": 0, "e": 1, "o": 2,
    "ka": 1, "ki": 0, "ku": 0, "ke": 1, "ko": 0,
    "sa": 2, "shi": 1, "su": 0, "se": 0, "so": 0,
    "ta": 3, "chi": 0, "tsu": 0, "te": 3, "to": 1,
    "na": 0, "ni": 0, "nu": 1, "ne": 1, "no": 1,
    "ha": 0, "hi": 2, "fu": 1, "he": 1, "ho": 1,
    "ma": 4, "mi": 3, "mu": 1, "me": 0, "mo": 1,
    "ya": 0, "yu": 0, "yo": 2,
    "ra": 4, "ri": 1, "ru": 2, "re": 1, "ro": 0,
    "wa": 1, "wo": 1,
    "n": 2
}
current_romaji = random.choice(list(romaji.keys()))
romaji[current_romaji] += 1
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
                file_path = os.path.join(data_dir, f"{current_romaji}_{romaji[current_romaji]}.png")
                pygame.image.save(screen, file_path)
                current_romaji = random.choice(list(romaji.keys()))
                romaji[current_romaji] += 1
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