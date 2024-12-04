import pygame

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
            game.game_initial_true = True

        elif leaderboard.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            print("leaderboard button pressed")

        elif settings.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            print("settings button pressed")

class Game:
    game_initial_true = False
    game_gameplay_true = False
    def __init__(self):
        pass

    
    def gameplay(self):
                game_surface = pygame.image.load('graphics/game.png').convert_alpha()
                screen.blit(game_surface,(0,0))
                backarrow = Button(50,120,'buttons/back_arrow.png')
                clean = Button(210,450 , 'buttons/clean_button.png')
                feed = Button(60,40,'buttons/feed_button.png')
                heal = Button(410,450,'buttons/heal_button.png')
                sleep = Button(410,40,'buttons/sleep_button.png')
                play = Button(220,40,'buttons/playbutton_button.png')
                pet = Button(60,450, 'buttons/pet_button.png')

                backarrow.draw()
                clean.draw()
                feed.draw()
                heal.draw()
                sleep.draw()
                play.draw()
                pet.draw()

                if backarrow.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
                    game.game_initial_true = False
                    game.game_gameplay_true = False         




    def initial_game_state(self):
        game_surface = pygame.image.load('graphics/menu.png').convert_alpha()
        screen.blit(game_surface,(0,0))

        play = Button(262,450,'buttons/play_button.png')
        play.draw()
        
        if play.collide() == True and event.type == pygame.MOUSEBUTTONDOWN:
            game.game_initial_true = False
            game.game_gameplay_true = True
            self.gameplay()

#Initialises pygame - sets an ingame clock (frame rate), initialises the screen + sets caption for game
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Virtual Pet")

menu = Menu()
game = Game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False            

    if game.game_initial_true == True:
        game.initial_game_state()
    elif game.game_gameplay_true == True:
        game.gameplay()
    else:
        menu.display()

    pygame.display.update()

    clock.tick(15)
