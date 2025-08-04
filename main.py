import pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGTH = 1280, 720
display_surface = pygame.dispay.set_mode(WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("space shooter")
running = true

while running:
  for event in pygame.event.get():
    if event type == pygame.QUIT:
    running = false
display_surface.fill('bleu')
pyga,e.display.update()
pygame.quit()
