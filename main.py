import pygame
from sys import exit

#game variables
GAME_WIDTH = 1000
GAME_HEIGHT = 775
Menu = True
selected = False
extra = False
difficulty = "none"
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Touhou")
clock = pygame.time.Clock()

COLOUR_TEXT = ("#000000")
COLOUR_SEL = ("#ffffff")

class Player():
    def __init__(self, char, hitbox, speed, focus_speed):
        self.char = char
        self.hitbox = hitbox
        self.speed = speed
        self.focus_speed = focus_speed

class Enemy():
    def __init__(self, type, hurtbox):
        self.type = type
        self.hurtbox = hurtbox

class Bullet():
    def __init__(self, hitbox, sprite):
        self.hitbox = hitbox
        self.sprite = sprite

player_hitbox = pygame.draw.circle(window, ("#ffffff"), (300,600), 4)

def draw():
    window.fill((20, 18, 167))
    pygame.draw.rect(window, (2, 239, 238), player_hitbox)

menu_state = "main menu"

menu_buttons = ["Start", "Extra Start", "Practice", "Options", "Quit"]
Characters = ["Reimu Hakurei", "Marisa Kirisame", "Sakuya Izayoi", "Sanae Kochiya", "Youmu Konpaku"]
difficulties = ["Easy", "Normal", "Hard", "Lunatic"]
selected_index = 0
char_index = 0
diffi_index = 0
def draw_main_menu():
    window.fill("#590461")

font = pygame.font.Font(None, 50)
last_input_time = 0
input_delay = 200

while Menu == True:
    current_time = pygame.time.get_ticks()
    draw_main_menu()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if menu_state == "main menu":

        if current_time - last_input_time > input_delay:

            if keys[pygame.K_UP]:
                selected_index = (selected_index - 1) % len(menu_buttons)
                last_input_time = current_time
                if extra == False and selected_index == 1:
                    selected_index = 0

            if keys[pygame.K_DOWN]:
                selected_index = (selected_index + 1) % len(menu_buttons)
                last_input_time = current_time
                if extra == False and selected_index == 1:
                    selected_index = 2

            if keys[pygame.K_z]:
                if selected_index == 0:
                    menu_state = "character select"
                elif selected_index == 1:
                    menu_state = "character select 2"
                elif selected_index == 2:
                    menu_state = "practice"
                elif selected_index == 3:
                    menu_state = "options"
                elif selected_index == 4:
                    pygame.quit()
                    exit()
                last_input_time = current_time

        for i, option in enumerate(menu_buttons):
            if i == selected_index:
                text_colour = COLOUR_SEL
                display_text = f"{option}"
            elif option == "Extra Start" and extra == False:
                text_colour = ("#838383")
                display_text = "Extra Start"
            else:
                text_colour = COLOUR_TEXT
                display_text = option

            text_surface = font.render(display_text, True, text_colour)

            text_rect = text_surface.get_rect(
                center=(800, 200 + i * 100)
            )
            window.blit(text_surface, text_rect)

            print (selected_index)

    elif menu_state == "character select":

        if current_time - last_input_time > input_delay:

            if keys[pygame.K_x]:
                menu_state = "main menu"
                last_input_time = current_time

            if keys[pygame.K_UP]:
                char_index = (char_index - 1) % len(Characters)
                last_input_time = current_time

            if keys[pygame.K_DOWN]:
                char_index = (char_index + 1) % len(Characters)
                last_input_time = current_time

            if keys[pygame.K_z]:
                if char_index == 0:
                    Character = Player("Reimu", 3, 5, 2.5)
                    menu_state = "difficulty select"
                elif char_index == 1:
                    Character = Player("Marisa", 4, 7, 3)
                    menu_state = "difficulty select"
                elif char_index == 2:
                    Character = Player("Sakuya", 4, 6, 4)
                    menu_state = "difficulty select"
                elif char_index == 3:
                    Character = Player("Sanae", 4, 5, 3)
                    menu_state = "difficulty select"
                elif char_index == 4:
                    Character = Player("Youmu", 4, 8, 4)
                    menu_state = "difficulty select"
                last_input_time = current_time

        for i, option in enumerate(Characters):
            if i == char_index:
                text_colour = COLOUR_SEL
                display_text = f"{option}"
            else:
                text_colour = COLOUR_TEXT
                display_text = option

            text_surface = font.render(display_text, True, text_colour)

            text_rect = text_surface.get_rect(
                center=(200, 90 + i * 150)
            )
            window.blit(text_surface, text_rect)

            print (char_index)

    elif menu_state == "difficulty select":

        if current_time - last_input_time > input_delay:

            if keys[pygame.K_x]:
                menu_state = "character select"
                last_input_time = current_time

            if keys[pygame.K_LEFT]:
                diffi_index = (diffi_index - 1) % len(difficulties)
                last_input_time = current_time

            if keys[pygame.K_RIGHT]:
                diffi_index = (diffi_index + 1) % len(difficulties)
                last_input_time = current_time

            if keys[pygame.K_z]:
                if diffi_index == 0:
                    difficulty = "Easy"
                    menu_state = "game"
                    break
                elif diffi_index == 1:
                    difficulty = "Normal"
                    menu_state = "game"
                    break
                elif diffi_index == 2:
                    difficulty = "Hard"
                    menu_state = "game"
                    break
                elif diffi_index == 3:
                    difficulty = "Lunatic"
                    menu_state = "game"
                    break
                last_input_time = current_time

        for i, option in enumerate(difficulties):
            if i == diffi_index:
                text_colour = COLOUR_SEL
                display_text = f"{option}"
            else:
                text_colour = COLOUR_TEXT
                display_text = option

            text_surface = font.render(display_text, True, text_colour)

            text_rect = text_surface.get_rect(
                center=(100 + i * 255, GAME_HEIGHT // 2)
            )
            window.blit(text_surface, text_rect)
        
    pygame.display.update()
    clock.tick(60)

stage = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_z]:
        pass

    if not keys[pygame.K_LSHIFT]:

        if player_hitbox.x > 600:
            player_hitbox.x -= Character.speed
        if player_hitbox.x < 0:
            player_hitbox.x += Character.speed

        if player_hitbox.y > 775:
            player_hitbox.y -= Character.speed
        if player_hitbox.y < 0:
            player_hitbox.y += Character.speed

        if keys[pygame.K_UP]:
            player_hitbox.y -= Character.speed
        if keys[pygame.K_DOWN]:
            player_hitbox.y += Character.speed
        if keys[pygame.K_LEFT]:
            player_hitbox.x -= Character.speed
        if keys[pygame.K_RIGHT]:
            player_hitbox.x += Character.speed
     
    if keys[pygame.K_LSHIFT]:

        if player_hitbox.x > 600:
            player_hitbox.x -= Character.focus_speed
        if player_hitbox.x < 0:
            player_hitbox.x += Character.focus_speed

        if player_hitbox.y > 775:
            player_hitbox.y -= Character.focus_speed
        if player_hitbox.y < 0:
            player_hitbox.y += Character.focus_speed

        if keys[pygame.K_UP]:
            player_hitbox.y -= Character.focus_speed
        if keys[pygame.K_DOWN]:
            player_hitbox.y += Character.focus_speed
        if keys[pygame.K_LEFT]:
            player_hitbox.x -= Character.focus_speed
        if keys[pygame.K_RIGHT]:
            player_hitbox.x += Character.focus_speed

        while stage == 1:
            if clock.tick() - 1800 > 0:
                pass

            elif clock.tick() - 1800 < 0:
                pass

    draw()
    pygame.display.update()
    clock.tick(60) #60 frames per second (fps)