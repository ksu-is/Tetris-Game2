import pygame
import sys
from game import Game
from colors import Colors


pygame.init()

#Game fonts
title_font = pygame.font.Font('titlefont.otf', 45)
game_font = pygame.font.Font('gamefont.otf', 35)
game_over_font = pygame.font.Font('gamefont.otf', 25)

#Score And Game-over Text and title
score_surface = game_font.render("SCORE", True, Colors.white)
next_surface = game_font.render("NEXT", True, Colors.white)
game_over_surface = game_over_font.render("GAME OVER", True, Colors.red)
title_surface = title_font.render("TETRIS", True, Colors.cyan)

#rectangle score screen
score_rect = pygame.Rect(345, 445, 120, 120)
next_rect = pygame.Rect(320, 220, 170, 170)
title_rect = pygame.Rect(315, 25, 180, 50)

#create game window
screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Game 2.0")

clock = pygame.time.Clock()

#Adding a new Background
background_img = pygame.image.load('background2.jpg')

#create game object
game = Game()

#create event that is triggered every time the game needs to be updated (200 milliseconds)
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

#adding game loop for consistency in all players
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #to detect block movement using keyboard,call game.py
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()                
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        
    #Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.yellow)
    
    screen.fill(Colors.black)
    #Adding image to background
    screen.blit(background_img, (0, 0))
    #Adding scoreboard backgroud
    screen.blit(score_surface, (345, 405, 50, 50))
    screen.blit(next_surface,(355, 180, 45, 50))
    screen.blit(title_surface,(315, 25, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (325, 575, 25, 25))
    #Score-background Shapes
    pygame.draw.rect(screen, Colors.light_grey, score_rect, 0, 15)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_grey, next_rect, 0, 15)  
    
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
    
