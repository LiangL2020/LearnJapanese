import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Drawing")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fill background with white
screen.fill(WHITE)

# Variables
running = True
drawing = False  # Track if mouse is pressed
draw_color = BLACK  # Default drawing color
radius = 5  # Brush size
last_pos = None  # Store last mouse position

# Main loop
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
            if event.key == pygame.K_c:  # Press 'C' to clear screen
                screen.fill(WHITE)
            elif event.key == pygame.K_UP:  # Increase brush size
                radius += 1
            elif event.key == pygame.K_DOWN:  # Decrease brush size
                radius = max(1, radius - 1)
    
    # Drawing with mouse movement
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, draw_color, last_pos, mouse_pos, radius * 2)
        last_pos = mouse_pos
    
    pygame.display.update()

pygame.quit()

# import pygame

# # Initialize pygame
# pygame.init()

# # Set up display
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mouse Drawing")

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Fill background with white
# screen.fill(WHITE)

# # Variables
# running = True
# drawing = False  # Track if mouse is pressed
# draw_color = BLACK  # Default drawing color
# radius = 5  # Brush size

# # Main loop
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             drawing = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             drawing = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_c:  # Press 'C' to clear screen
#                 screen.fill(WHITE)
#             elif event.key == pygame.K_UP:  # Increase brush size
#                 radius += 1
#             elif event.key == pygame.K_DOWN:  # Decrease brush size
#                 radius = max(1, radius - 1)
    
#     # Drawing with mouse movement
#     if drawing:
#         mouse_pos = pygame.mouse.get_pos()
#         pygame.draw.circle(screen, draw_color, mouse_pos, radius)
    
#     pygame.display.update()

# pygame.quit()

# import turtle as t

# # Initialize screen
# screen = t.Screen()
# screen.title("Handwriting Panel")
# screen.bgcolor("white")

# # Initialize the pen
# pen = t.Turtle()
# pen.speed(0)  # Fastest speed
# pen.width(5)  # Set pen thickness
# pen.color("black")
# # pen.hideturtle()
# pen.pendown()  # Ensure the pen is down to draw

# # Function to handle drawing
# def draw(x, y):
#     pen.ondrag(None)  # Temporarily disable dragging to prevent lag
#     pen.goto(x, y)
#     pen.ondrag(draw)  # Re-enable dragging

# # Function to clear the screen
# def clear():
#     pen.clear()

# # Bind events
# screen.listen()
# pen.ondrag(draw)  # Enable drawing when dragging the mouse
# screen.onscreenclick(lambda x, y: clear(), 3)  # Right-click to clear

# # Start event loop
# screen.mainloop()

# # import turtle

# # screen = turtle.Screen()
# # pen = turtle.Turtle()
# # pen.speed(0)  # Set drawing speed to fastest

# # def draw(x, y):
# #     pen.ondrag(None) # Prevent immediate retriggering during drag
# #     pen.setheading(pen.towards(x, y))
# #     pen.goto(x, y)
# #     pen.ondrag(draw) # Re-enable drawing on drag

# # def clear_screen(x, y):
# #     pen.clear()

# # screen.listen()
# # pen.ondrag(draw)
# # screen.onscreenclick(clear_screen, 3) # Clear screen on right click
# # screen.mainloop()