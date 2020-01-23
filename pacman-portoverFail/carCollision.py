import pygame

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed

        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        # Instead we could load a proper picture of a car...
        self.image = pygame.image.load("res/sprite/pacman-d 1.gif").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])


pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 720
SCREENHEIGHT = 540

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

playerCar1 = Car(RED, 20, 30, 20)
playerCar1.rect.x = 200
playerCar1.rect.y = 300

playerCar2 = Car(PURPLE, 20, 30, 20)
playerCar2.rect.x = 170
playerCar2.rect.y = 300

# Add the car to the list of objects
all_sprites_list.add(playerCar1)
all_sprites_list.add(playerCar2)


# Allowing the user to close the window...
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar1.moveRight(5)
    if keys[pygame.K_UP]:
        playerCar1.moveForward(5)
    if keys[pygame.K_DOWN]:
        playerCar1.moveBackward(5)
    if keys[pygame.K_a]:
        playerCar2.moveLeft(5)
    if keys[pygame.K_d]:
        playerCar2.moveRight(5)
    if keys[pygame.K_w]:
        playerCar2.moveForward(5)
    if keys[pygame.K_s]:
        playerCar2.moveBackward(5)

    car_collision_list = pygame.sprite.spritecollide(playerCar1, [playerCar2], False)
    for car in car_collision_list:
        print("Car crash!")
        # End Of Game
        #carryOn = False

    # Game Logic
    all_sprites_list.update()

    # Drawing on Screen
    screen.fill(GREEN)
    # Draw The Road
    pygame.draw.rect(screen, GREY, [40, 0, 200, 300])
    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, 300], 5)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()
