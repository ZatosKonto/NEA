import pygame
from sys import exit

class Button:
    def __init__(self, x, y, image):
        #constructing button, takes the x and y cords + image of png file
        self.x = x
        self.y = y
        self.image = image
        #loads image as a surface
        self.surface = pygame.image.load(self.image).convert_alpha()
        #converts into a rectangle - gives it properties to allow for collision function to work effectively
        self.rect = self.surface.get_rect(center = (self.x,self.y))

    def draw(self):
        #displays button ontowards the screen
        screen.blit(self.surface, self.rect)

    def collide(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True

class Menu:
    def __init__(self):
        pass

    #displays the entire menu screen to the user
    def display(self):
        
        #display background screen - as a surface (acts as the base layer)
        menu_surface = pygame.image.load('graphics/menu.png').convert_alpha()
        screen.blit(menu_surface, (0,0))

        #creates all buttons the user can interact with on the menu screen
        play = Button(262,331,'buttons/play_button.png')
        leaderboard = Button(262,390, 'buttons/leaderboard_button.png')
        settings = Button(262,450, 'buttons/settings_button.png')

        #uses .draw() method made in button object to display the buttons to the user - menu screen is created :)
        play.draw()
        leaderboard.draw()
        settings.draw()
        
        if play.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            game.self_operating = True

        elif leaderboard.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            print("leaderboard button pressed")

        elif settings.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            print("settings button pressed")

class Game:
    self_game_initialise_on_off = False
    self_gameplay_on_off = False

    def __init__(self):
        pass
    
    def gameplay(self):
        while True:
            game_surface = pygame.image.load('graphics/game.png').convert_alpha()
            screen.blit(game_surface,(0,0))


    def game_state(self):
        game_surface = pygame.image.load('graphics/menu.png').convert_alpha()
        screen.blit(game_surface,(0,0))

        play = Button(262,450,'buttons/play_button.png')
        
        play.draw()
        if play.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
              self.gameplay()


#Initialises pygame - sets an ingame clock (frame rate), initialises the screen + sets caption for game
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Virtual Pet")

menu = Menu()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()            
    
    if game.self_operating == True:
        game.game_state()
    else:
        menu.display()

    pygame.display.update()

    clock.tick(15)
