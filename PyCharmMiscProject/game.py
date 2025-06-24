# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Omkar')
    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Omkars game')
    #player=pygame.draw.circle(screen,'blue')
    player= pygame.Rect(10,10,50,50)

    def draw():
        screen.fill('cyan')
        pygame.draw.rect(screen,'black',player)
    pygame.display.set_caption("My Pygame Window")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         player.y = max(player.y - 5,0)
            #
            #     if event.key == pygame.K_DOWN:
            #         player.y = min(player.y + 5,height)
            #     if event.key == pygame.K_RIGHT:
            #         player.x = min(player.x + 5,height)
            #
            #     if event.key == pygame.K_LEFT:
            #         player.x = max(player.x - 5,0)

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            player.y = max(player.y - 1, 0)
        if key[pygame.K_DOWN]:
            player.y = min(player.y + 1,height)
        if key[pygame.K_RIGHT]:
            player.x = min(player.x + 1,height)
        if key[pygame.K_LEFT]:
            player.x = max(player.x - 1,0)





        draw()
        pygame.display.update()
        pygame.display.flip()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
