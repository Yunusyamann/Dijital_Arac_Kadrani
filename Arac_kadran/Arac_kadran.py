import pygame
import sys
import math
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dijital Araç Kadranı')
font = pygame.font.Font(None, 32)
large_font = pygame.font.Font(None, 48)

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
RED = (255, 60, 60)
GRAY = (100, 100, 100)
NEEDLE_COLOR = (255, 0, 0)
BLUE = (0, 120, 255)
GREEN = (0, 200, 0)

center_x, center_y = 400, 350
needle_length = 110
max_speed = 40
radius = 140

speed_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 35, 30, 25, 20, 15, 10, 5, 0]

voltage = 12.7
current = 3.5
battery_percentage = 75

def draw_speedometer(speed):
    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius + 10, 4)
    for i in range(0, max_speed + 1, 5):
        angle = math.radians(180 - (i / max_speed * 180))
        tick_x = center_x + (needle_length + 20) * math.cos(angle)
        tick_y = center_y - (needle_length + 20) * math.sin(angle)
        pygame.draw.line(screen, GRAY, 
                         (center_x + (needle_length - 20) * math.cos(angle),
                          center_y - (needle_length - 20) * math.sin(angle)),
                         (tick_x, tick_y), 2)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(tick_x, tick_y))
        screen.blit(text, text_rect)
    
    angle = math.radians(180 - (speed / max_speed * 180))
    needle_x = center_x + needle_length * math.cos(angle)
    needle_y = center_y - needle_length * math.sin(angle)
    pygame.draw.line(screen, NEEDLE_COLOR, (center_x, center_y), (needle_x, needle_y), 5)
    pygame.draw.circle(screen, NEEDLE_COLOR, (center_x, center_y), 8)

    speed_display = large_font.render(f'{speed} km/h', True, GREEN)
    screen.blit(speed_display, (center_x - speed_display.get_width() // 2, center_y + 100))

def draw_status_panel():
    pygame.draw.rect(screen, BLUE, (30, 30, 240, 140), border_radius=10)
    voltage_text = font.render(f'Voltaj: {voltage:.1f} V', True, WHITE)
    current_text = font.render(f'Akım: {current:.1f} A', True, WHITE)
    battery_text = font.render(f'Pil: %{battery_percentage}', True, WHITE)
    screen.blit(voltage_text, (50, 50))
    screen.blit(current_text, (50, 90))
    screen.blit(battery_text, (50, 130))

for speed in speed_values:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    draw_speedometer(speed)
    draw_status_panel()
    pygame.display.flip()
    time.sleep(0.5)
