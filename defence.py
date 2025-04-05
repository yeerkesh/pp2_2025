import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")
clock = pygame.time.Clock()

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

current_tool = "rect" 
current_color = RED
brush_size = 4
eraser_size = 20

button_red = pygame.Rect(10, 550, 50, 30)
button_green = pygame.Rect(70, 550, 50, 30)
button_blue = pygame.Rect(130, 550, 50, 30)


def draw_buttons():
    pygame.draw.rect(screen, RED, button_red)
    pygame.draw.rect(screen, GREEN, button_green)
    pygame.draw.rect(screen, BLUE, button_blue)


def draw_instructions():
    font = pygame.font.SysFont("Verdana", 16)
    instructions = [
        "Tools: 1-Rectangle 2-Circle",
        "Click buttons to change colors",
    ]
    y = 5
    for line in instructions:
        text = font.render(line, True, BLACK)
        screen.blit(text, (5, y))
        y += 20

start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_1:
                current_tool = "rect"
            elif event.key == K_2:
                current_tool = "circle"
            

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_red.collidepoint(event.pos):
                    current_color = RED
                elif button_green.collidepoint(event.pos):
                    current_color = GREEN
                elif button_blue.collidepoint(event.pos):
                    current_color = BLUE
                
                else:
                    start_pos = event.pos
                    if current_tool in ["pen", "eraser"]:
                        draw_color = WHITE if current_tool == "eraser" else current_color
                        pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)

        if event.type == MOUSEMOTION:
            if event.buttons[0]:
                if current_tool in ["pen", "eraser"]:
                    draw_color = WHITE if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)

        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos
                if current_tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, 2)
                elif current_tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
                start_pos = None

    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_buttons()
    draw_instructions()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
