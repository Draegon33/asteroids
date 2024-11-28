# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.init()

  timer = pygame.time.Clock()
  dt = 0



  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  bullets = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  game_running = True

  while(game_running):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    #player.update(dt)
    for i in updatable:
      i.update(dt)

    for i in asteroids:
      if i.collision(player):
        print("Game Over!")
        game_running = False

    screen.fill((0,0,0))

    #player.draw(screen)
    for i in drawable:
      i.draw(screen)

    pygame.display.flip()

    dt = timer.tick(60) / 1000

  pygame.quit()

if __name__ == "__main__":
    main()