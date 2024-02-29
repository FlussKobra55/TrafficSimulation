


import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    clock=pygame.time.Clock()

    # Create a Pygame window
    window_size = (400, 400)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Traffic Simulation')

    # Create a font object
    font = pygame.font.Font(None, 24)

    # button real situation
    btnRealSurf = pygame.Surface((200, 50))
    btnRealText = font.render("Realität", True, (255, 255, 255))
    btnRealText_rect = btnRealText.get_rect(center=(btnRealSurf.get_width()/2, btnRealSurf.get_height()/2))
    btnRealRect = pygame.Rect(100, 125, btnRealSurf.get_width(), btnRealSurf.get_height())

    # button 1 lane less situation
    btnLessSurf = pygame.Surface((200, 50))
    btnLessText = font.render("1 Spur weniger", True, (255, 255, 255))
    btnLessText_rect = btnLessText.get_rect(center=(btnLessSurf.get_width() / 2, btnLessSurf.get_height() / 2))
    btnLessRect = pygame.Rect(100, 190, btnLessSurf.get_width(), btnLessSurf.get_height())

    # button 1 lane more situation
    btnMoreSurf = pygame.Surface((200, 50))
    btnMoreText = font.render("1 Spur mehr", True, (255, 255, 255))
    btnMoreText_rect = btnMoreText.get_rect(center=(btnMoreSurf.get_width() / 2, btnMoreSurf.get_height() / 2))
    btnMoreRect = pygame.Rect(100, 255, btnMoreSurf.get_width(), btnMoreSurf.get_height())

    # button american situation
    btnUSASurf = pygame.Surface((200, 50))
    btnUSAText = font.render("Amerikanisch", True, (255, 255, 255))
    btnUSAText_rect = btnUSAText.get_rect(center=(btnUSASurf.get_width() / 2, btnUSASurf.get_height() / 2))
    btnUSARect = pygame.Rect(100, 320, btnUSASurf.get_width(), btnUSASurf.get_height())

    # Start the main loop
    while True:
        # Set the frame rate
        clock.tick(60)

        # Fill the display with color
        screen.fill((255, 255, 255))

        # Get events from the event queue
        for event in pygame.event.get():
            # Check for the quit event
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                sys.exit()

            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if btnRealRect.collidepoint(event.pos):
                    print("Button clicked!")
                if btnLessRect.collidepoint(event.pos):
                    print("test")
                if btnMoreRect.collidepoint(event.pos):
                    print("lalala")
                if btnUSARect.collidepoint(event.pos):
                    print("ölsad")

        # Check if the mouse is over the button. This will create the button hover effect
        if btnRealRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnRealSurf, (40, 150, 100), (1, 1, btnRealSurf.get_width(), btnRealSurf.get_height()))
        else:
            pygame.draw.rect(btnRealSurf, (255, 255, 255), (0, 0, btnRealSurf.get_width(), btnRealSurf.get_height()))
            pygame.draw.rect(btnRealSurf, (0, 0, 0), (1, 1, btnRealSurf.get_width()-2, btnRealSurf.get_height()-2))
            pygame.draw.rect(btnRealSurf, (255, 255, 255), (1, 1, btnRealSurf.get_width()-2, 1), 2)
            pygame.draw.rect(btnRealSurf, (0, 100, 0), (1, 48, btnRealSurf.get_width()-2, 10), 2)
            
        btnRealSurf.blit(btnRealText, btnRealText_rect)
        screen.blit(btnRealSurf, (btnRealRect.x, btnRealRect.y))
            
        if btnLessRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnLessSurf, (40, 150, 100), (1, 1, btnLessSurf.get_width(), btnLessSurf.get_height()))
        else:
            pygame.draw.rect(btnLessSurf, (255, 255, 255), (0, 0, btnLessSurf.get_width(), btnLessSurf.get_height()))
            pygame.draw.rect(btnLessSurf, (0, 0, 0), (1, 1, btnLessSurf.get_width()-2, btnLessSurf.get_height()-2))
            pygame.draw.rect(btnLessSurf, (255, 255, 255), (1, 1, btnLessSurf.get_width()-2, 1), 2)
            pygame.draw.rect(btnLessSurf, (0, 100, 0), (1, 48, btnLessSurf.get_width()-2, 10), 2)

        btnLessSurf.blit(btnLessText, btnLessText_rect)
        screen.blit(btnLessSurf, (btnLessRect.x, btnLessRect.y))
        
        if btnMoreRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnMoreSurf, (40, 150, 100), (1, 1, btnMoreSurf.get_width(), btnMoreSurf.get_height()))
        else:
            pygame.draw.rect(btnMoreSurf, (255, 255, 255), (0, 0, btnMoreSurf.get_width(), btnMoreSurf.get_height()))
            pygame.draw.rect(btnMoreSurf, (0, 0, 0), (1, 1, btnMoreSurf.get_width()-2, btnMoreSurf.get_height()-2))
            pygame.draw.rect(btnMoreSurf, (255, 255, 255), (1, 1, btnMoreSurf.get_width()-2, 1), 2)
            pygame.draw.rect(btnMoreSurf, (0, 100, 0), (1, 48, btnMoreSurf.get_width()-2, 10), 2)

        btnMoreSurf.blit(btnMoreText, btnMoreText_rect)
        screen.blit(btnMoreSurf, (btnMoreRect.x, btnMoreRect.y))
        
        if btnUSARect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnUSASurf, (40, 150, 100), (1, 1, btnUSASurf.get_width(), btnUSASurf.get_height()))
        else:
            pygame.draw.rect(btnUSASurf, (255, 255, 255), (0, 0, btnUSASurf.get_width(), btnUSASurf.get_height()))
            pygame.draw.rect(btnUSASurf, (0, 0, 0), (1, 1, btnUSASurf.get_width()-2, btnUSASurf.get_height()-2))
            pygame.draw.rect(btnUSASurf, (255, 255, 255), (1, 1, btnUSASurf.get_width()-2, 1), 2)
            pygame.draw.rect(btnUSASurf, (0, 100, 0), (1, 48, btnUSASurf.get_width()-2, 10), 2)

        btnUSASurf.blit(btnUSAText, btnUSAText_rect)
        screen.blit(btnUSASurf, (btnUSARect.x, btnUSARect.y))



        # Update the game state
        pygame.display.update()

if __name__ == '__main__':
    main()
