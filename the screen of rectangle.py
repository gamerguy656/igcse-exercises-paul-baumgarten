import pygame, time, random
from pygame.locals import*
def main():
    quit = False
    x = 0
    y = 0
    player_stand = pygame.image.load("move-t-pose.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (250, 250))
    while not quit:
        window.fill((64,255,255))
        keyspressed = pygame.key.get_pressed()
        the_rectangle = Rect(x ,y,100,100)
        pygame.draw.rect(window, (0,0,0), the_rectangle)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
        if keyspressed[ord("a")]:
                    x = x - 50
                    if x < 0:
                        x = 0
        if keyspressed[ord("d")]:
                    x = x + 50
                    if x > 1920-50:
                        x = 0
        if keyspressed[ord("w")]:
                    y = y - 50
                    if y < 0:
                        y = 0
        if keyspressed[ord("s")]:
                    y = y + 50
                    if y > 950:
                        y = 0
       
        pygame.display.update()
        clock.tick(25)
if __name__ == "__main__":
    width, height = 1920, 1000
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("the screen")
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    main()
    pygame.quit()