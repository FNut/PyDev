import pygame
import COVID19Py
pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('COVID-19')
covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()
font = pygame.font.SysFont('None', 30)
news = font.render(str(latest), True, (0,255,0))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display.blit(news, (0,0))
    pygame.display.update()
pygame.quit()
