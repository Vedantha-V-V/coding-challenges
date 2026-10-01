import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from spaceship import Spaceship
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state,log_event

pygame.init()
dt = 0
clock = pygame.time.Clock()
# bg_music = pygame.mixer.Sound('res/music/music.mp3')
# bg_music.play(loops = -1)
# icon = pygame.image.load('res/logo.jpg')
# pygame.display.set_icon(icon)
pygame.display.set_caption('Asteroids')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Spaceship.containers = (updatable, drawable)
Asteroid.containers = (asteroids,updatable,drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots,updatable,drawable)
spaceship = Spaceship(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
asteroidfield = AsteroidField()
# asteroid = Asteroid(100,100,10)

while True:
    # asteroid.draw(screen)
    screen.fill("black")
    log_state()
    updatable.update(dt)
    for asteroid in asteroids:
        if asteroid.collide_with(spaceship):
            log_event('Player Hit')
            print('Game over!')
            exit()
        for shot in shots:
            if asteroid.collide_with(shot):
                asteroid.split()
                shot.kill()

    for item in drawable:
        item.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    dt = clock.tick(60)
    dt = dt/1000
    pygame.display.flip()
        