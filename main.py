import pygame
from os.path import join
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
display_surface = pygame.dispay.set_mode(WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("space shooter")
running = true

surf = pygame.surface(100,200)
surf.fill('orange')
x = 100
# importer img du player
player_surf = pygame.image.load(join('../imgs/player.png')).convert_alpha()
star_surf = pygame.image.load(join('../imgs/star.png')).convert_alpha()
star_positions = [(x,y) for i in range(20)]
while running:
  for event in pygame.event.get():
    if event type == pygame.QUIT:
    running = false
display_surface.fill('bleu')
x += 0.2
display_surface.blit(player_surf, x,150)
for i in range(20):
display_surface.blit(star_surf, randit(0, WINDOW_WIDTH),randit(0, WINDOW_HEIGTH))
pygame.display.update()
pygame.quit()
