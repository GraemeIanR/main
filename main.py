import pygame
from sys import exit

#game variables
GAME_WIDTH = 1000
GAME_HEIGHT = 775
selected = False
extra = False
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Touhou")
clock = pygame.time.Clock()

player_hitbox = pygame.draw.circle(window, ("#ffffff"), (0,0), 7)

text_colour = ("#000000")

COLOUR_TEXT = ("#000000")
COLOUR_SEL = ("#ffffff")

class Player():
    def __init__(self, char, hitbox, speed, focus_speed):
        self.char = char
        self.hitbox = hitbox
        self.speed = speed
        self.focus_speed = focus_speed

def draw():
    window.fill((20, 18, 167))
    pygame.draw.rect(window, (2, 239, 238), player_hitbox)

menu_state = "main menu"

menu_buttons = ["Start", "Extra Start", "Practice", "Options", "Quit"]
selected_index = 0

def selection(index):
    if index == 0:
        menu_state = "character select"
    elif index == 1:
        menu_state = "character select 2"
    elif index == 2:
        menu_state = "practice"
    elif index == 3:
        menu_state = "options"
    elif index == 4:
        pygame.quit()
        exit()
        sys.exit()

def draw_main_menu():
    window.fill("#590461")

font = pygame.font.Font(None, 50)

while menu_state == "main menu":

    draw_main_menu()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if event.type == pygame.KEYDOWN:

        if keys[pygame.K_UP]:
            selected_index = (selected_index - 1) % len(menu_buttons)

        if keys[pygame.K_DOWN]:
            selected_index = (selected_index + 1) % len(menu_buttons)

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
                break

    for i, option in enumerate(menu_buttons):
        if i == selected_index:
            text_colour = COLOUR_SEL
            display_text = f"{option}"
        else:
            text_colour = COLOUR_TEXT
            display_text = option

        text_surface = font.render(display_text, True, text_colour)

        text_rect = text_surface.get_rect(
            center=(600, 200 + i * 80)
        )
        window.blit(text_surface, text_rect)

        print (selected_index)

        if menu_state != "main menu":
            break
        
    pygame.display.update()
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        Character = Player("Reimu", 7, 5, 2)
        selected = True

    if keys[pygame.K_m]:
        Character = Player("Marisa", 7, 7, 4)
        selected = True

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

    draw()
    pygame.display.update()
    clock.tick(60) #60 frames per second (fps)