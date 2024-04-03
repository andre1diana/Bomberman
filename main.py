import pygame
from player import Player
from map import Map

WIDTH, HEIGHT = 750, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")
pygame.font.init()
pygame.mixer.init()

FPS = 60

map1 = Map(WINDOW, "MAPS/map1.map")

background_music = pygame.mixer.Sound('RES/background.mp3')
background_music.set_volume(0.4)
death_player_sound = pygame.mixer.Sound('RES/bomberman-death-sound.mp3')


def start_menu():
    WINDOW.fill((0, 102, 51))
    start_image = pygame.transform.scale(pygame.image.load("RES/NeoStart.gif"), (300, 100))
    font = pygame.font.SysFont('Comic Sans MS', 40)
    quit_button = font.render('QUIT', False, (0, 0, 0))
    # pygame.draw.rect(WINDOW, (0, 0, 0), (150, 250, 300, 100))
    WINDOW.blit(start_image, (200, 250))
    WINDOW.blit(quit_button, (300, 450))
    pygame.display.update()


def game_is_over(number):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text1 = font.render('WINNER PLAYER 1', False, (255, 255, 255))
    text2 = font.render('WINNER PLAYER 2', False, (255, 255, 255))

    WINDOW.fill((0, 102, 51))
    font = pygame.font.SysFont('Comic Sans MS', 25)
    surface = font.render('GAME OVER', False, (0, 0, 0))
    if number == 1:
        WINDOW.blit(text1, (200, 250))
    else:
        WINDOW.blit(text2, (200, 250))

    WINDOW.blit(surface, (300, 400))
    pygame.display.update()


def paused():
    pause = True
    WINDOW.fill((204, 255, 229))
    font = pygame.font.SysFont('Comic Sans MS', 25)
    surface = font.render('RESUME', False, (0, 0, 0))
    WINDOW.blit(surface, (300, 300))
    pygame.display.update()
    while pause:
        for event1 in pygame.event.get():
            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_SPACE:
                    pause = False


def main():
    global player1, player2
    clock = pygame.time.Clock()
    run = True
    game_state = 'start_menu'

    while run:
        # background_music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if game_state == 'start_menu':
            start_menu()
            start_rect = pygame.Rect(200, 250, 300, 100)
            quit_rect = pygame.Rect(300, 450, 100, 50)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(pygame.mouse.get_pos()):
                        map1.draw_map()
                        player1 = Player(WINDOW, map1, "RES/RedRobot.png", map1.player1_x, map1.player1_y, 1)
                        player2 = Player(WINDOW, map1, "RES/BlueRobot.png", map1.player2_x, map1.player2_y, 2)
                        map1.add_players(player1, player2)
                        pygame.display.update()
                        game_state = 'game'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rect.collidepoint(pygame.mouse.get_pos()):
                        run = False

        elif game_state == 'game':
            clock.tick(FPS)
            keys_pressed = pygame.key.get_pressed()
            map1.update()
            player1.player_handle_movement(keys_pressed)
            player1.update()
            player2.player_handle_movement(keys_pressed)
            player2.update()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused()
                if event.type == pygame.QUIT:
                    run = False
            if player1.current_hp <= 10 or player2.current_hp <= 10:
                game_state = 'end'
                death_player_sound.play()
        elif game_state == 'end':
            if player1.current_hp <= 10:
                game_is_over(2)
            else:
                game_is_over(1)

    pygame.quit()


if __name__ == "__main__":
    main()
