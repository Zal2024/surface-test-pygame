#test

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

block = pygame.Surface((100, 100))
block.fill("green")

while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
    pygame.quit()
    exit()
 
 screen.blit(block,(50, 50))
 
 #Draw all the element
 #Update everything
 pygame.display.update()
 clock.tick(60)