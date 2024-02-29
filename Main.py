import pygame
import sys
import os

from TrafficSituations.LeftTrafficCrossroad import leftTrafficCrossroad
from TrafficSituations.Crossroad1Lane import crossroad1Lane
from TrafficSituations.CrossRoad2Lane import crossroad2lane
from TrafficSituations.CrossRoad3Lane import crossroad3lane


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (50, 30)
    trafficLightModes = ["real", "onegreen", "sidebyside", "threegreen", "everythinggreen"]
    trafficLightMode = 0

    # Initialize Pygame
    pygame.init()

    clockMain = pygame.time.Clock()

    # Create a Pygame window
    windowSizeMain = (400, 400)
    screen = pygame.display.set_mode(windowSizeMain)
    pygame.display.set_caption('Traffic Simulation')

    # Create a font object
    font = pygame.font.Font(None, 24)

    # text description
    text_Descript = font.render("Wähle Modus der nächsten Simulation aus", False, (0, 0, 0))

    # button real situation
    btnRealSurf = pygame.Surface((200, 50))
    btnRealText = font.render("Realität", True, (255, 255, 255))
    btnRealText_rect = btnRealText.get_rect(center=(btnRealSurf.get_width() / 2, btnRealSurf.get_height() / 2))
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

    # button leftTraffic situation
    btnLeftSurf = pygame.Surface((200, 50))
    btnLeftText = font.render("Linksverkehr", True, (255, 255, 255))
    btnLeftText_rect = btnLeftText.get_rect(center=(btnLeftSurf.get_width() / 2, btnLeftSurf.get_height() / 2))
    btnLeftRect = pygame.Rect(100, 320, btnLeftSurf.get_width(), btnLeftSurf.get_height())

    # button traffic lights mode
    btnLightModeSurf = pygame.Surface((200, 50))
    btnLightModeText = font.render("Ampelmodus wechseln", True, (255, 255, 255))
    btnLightModeText_rect = btnLightModeText.get_rect(center=(btnLightModeSurf.get_width() / 2,
                                                              btnLightModeSurf.get_height() / 2))
    btnLightModeRect = pygame.Rect(100, 20, btnLightModeSurf.get_width(), btnLightModeSurf.get_height())

    # text traffic lights mode
    textLightMode = font.render(f"ausgewählter Modus: {trafficLightModes[trafficLightMode]}",
                                False, (0, 0, 0))

    # Start the main loop
    while True:

        # Set the frame rate
        clockMain.tick(60)

        # Fill the display with color
        screen.fill((255, 255, 255))

        # text description
        screen.blit(text_Descript, (30, 0))
        screen.blit(textLightMode, (80, 80))

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
                    crossroad2lane(trafficLightModes[trafficLightMode])
                if btnLessRect.collidepoint(event.pos):
                    crossroad1Lane(trafficLightModes[trafficLightMode])
                if btnMoreRect.collidepoint(event.pos):
                    crossroad3lane(trafficLightModes[trafficLightMode])
                if btnLeftRect.collidepoint(event.pos):
                    leftTrafficCrossroad(trafficLightModes[trafficLightMode])
                if btnLightModeRect.collidepoint(event.pos):
                    if trafficLightMode < 4:
                        trafficLightMode += 1
                    else:
                        trafficLightMode = 0

        # Check if the mouse is over the button. This will create the button hover effect
        if btnRealRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnRealSurf, (40, 150, 100), (1, 1, btnRealSurf.get_width(), btnRealSurf.get_height()))
        else:
            pygame.draw.rect(btnRealSurf, (255, 255, 255), (0, 0, btnRealSurf.get_width(), btnRealSurf.get_height()))
            pygame.draw.rect(btnRealSurf, (0, 0, 0), (1, 1, btnRealSurf.get_width() - 2, btnRealSurf.get_height() - 2))
            pygame.draw.rect(btnRealSurf, (255, 255, 255), (1, 1, btnRealSurf.get_width() - 2, 1), 2)
            pygame.draw.rect(btnRealSurf, (0, 100, 0), (1, 48, btnRealSurf.get_width() - 2, 10), 2)

        btnRealSurf.blit(btnRealText, btnRealText_rect)
        screen.blit(btnRealSurf, (btnRealRect.x, btnRealRect.y))

        if btnLessRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnLessSurf, (40, 150, 100), (1, 1, btnLessSurf.get_width(), btnLessSurf.get_height()))
        else:
            pygame.draw.rect(btnLessSurf, (255, 255, 255), (0, 0, btnLessSurf.get_width(), btnLessSurf.get_height()))
            pygame.draw.rect(btnLessSurf, (0, 0, 0), (1, 1, btnLessSurf.get_width() - 2, btnLessSurf.get_height() - 2))
            pygame.draw.rect(btnLessSurf, (255, 255, 255), (1, 1, btnLessSurf.get_width() - 2, 1), 2)
            pygame.draw.rect(btnLessSurf, (0, 100, 0), (1, 48, btnLessSurf.get_width() - 2, 10), 2)

        btnLessSurf.blit(btnLessText, btnLessText_rect)
        screen.blit(btnLessSurf, (btnLessRect.x, btnLessRect.y))

        if btnMoreRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnMoreSurf, (40, 150, 100), (1, 1, btnMoreSurf.get_width(), btnMoreSurf.get_height()))
        else:
            pygame.draw.rect(btnMoreSurf, (255, 255, 255), (0, 0, btnMoreSurf.get_width(), btnMoreSurf.get_height()))
            pygame.draw.rect(btnMoreSurf, (0, 0, 0), (1, 1, btnMoreSurf.get_width() - 2, btnMoreSurf.get_height() - 2))
            pygame.draw.rect(btnMoreSurf, (255, 255, 255), (1, 1, btnMoreSurf.get_width() - 2, 1), 2)
            pygame.draw.rect(btnMoreSurf, (0, 100, 0), (1, 48, btnMoreSurf.get_width() - 2, 10), 2)

        btnMoreSurf.blit(btnMoreText, btnMoreText_rect)
        screen.blit(btnMoreSurf, (btnMoreRect.x, btnMoreRect.y))

        if btnLeftRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnLeftSurf, (40, 150, 100), (1, 1, btnLeftSurf.get_width(), btnLeftSurf.get_height()))
        else:
            pygame.draw.rect(btnLeftSurf, (255, 255, 255), (0, 0, btnLeftSurf.get_width(), btnLeftSurf.get_height()))
            pygame.draw.rect(btnLeftSurf, (0, 0, 0), (1, 1, btnLeftSurf.get_width() - 2, btnLeftSurf.get_height() - 2))
            pygame.draw.rect(btnLeftSurf, (255, 255, 255), (1, 1, btnLeftSurf.get_width() - 2, 1), 2)
            pygame.draw.rect(btnLeftSurf, (0, 100, 0), (1, 48, btnLeftSurf.get_width() - 2, 10), 2)

        btnLeftSurf.blit(btnLeftText, btnLeftText_rect)
        screen.blit(btnLeftSurf, (btnLeftRect.x, btnLeftRect.y))
        
        if btnLightModeRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(btnLightModeSurf, (40, 150, 100), (1, 1, btnLightModeSurf.get_width(), btnLightModeSurf.get_height()))
        else:
            pygame.draw.rect(btnLightModeSurf, (255, 255, 255), (0, 0, btnLightModeSurf.get_width(), btnLightModeSurf.get_height()))
            pygame.draw.rect(btnLightModeSurf, (0, 0, 0), (1, 1, btnLightModeSurf.get_width() - 2, btnLightModeSurf.get_height() - 2))
            pygame.draw.rect(btnLightModeSurf, (255, 255, 255), (1, 1, btnLightModeSurf.get_width() - 2, 1), 2)
            pygame.draw.rect(btnLightModeSurf, (0, 100, 0), (1, 48, btnLightModeSurf.get_width() - 2, 10), 2)

        btnLightModeSurf.blit(btnLightModeText, btnLightModeText_rect)
        screen.blit(btnLightModeSurf, (btnLightModeRect.x, btnLightModeRect.y))

        textLightMode = font.render(f"ausgewählter Modus: {trafficLightModes[trafficLightMode]}",
                                    False, (0, 0, 0))



        # Update the game state
        pygame.display.update()


if __name__ == '__main__':
    main()
