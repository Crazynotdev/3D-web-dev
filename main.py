import pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
display_surface = pygame.dispay.set_mode(WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("space shooter")
running = true

surf = pygame.surface(100,200)
surf.fill('orange')
x = 100
# importer img du player
player_surf = pygame.image.load('../imgs/player.png')

while running:
  for event in pygame.event.get():
    if event type == pygame.QUIT:
    running = false
display_surface.fill('bleu')
x += 0.2
display_surface.blit((surf, x,150))
pygame.display.update()
pygame.quit()
