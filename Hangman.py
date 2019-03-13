# Pygame based on https://github.com/JCLOH98/Hangman-Pygame

import pygame
import sys
import random
import time
import re

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Hangman")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
LEFT_CLICK = (1, 0, 0)
RIGHT_CLICK = (0, 0, 1)

# 32 bit display
display = pygame.display.set_mode((500, 500), 0, 32)
display.fill(WHITE)

# TODO randomize words from dictionary
easy = ["BELL", "STAR", "PICNIC", "PIE", "HAT", "HEART", "FLAG"]
medium = ["CARPET", "POPCORN", "SEAFOOD", "DOORBELL", "COWBOY", "INSIDE", "OUTSIDE", "RAINBOW", "POSTMAN", "WATERMELON",
          "FOOTBALL", "STRAWBERRY"]
hard = ["BACKGROUND", "BOOKWORM", "FIREFIGHTER", "SOUNDPROOF", "THUNDERSTORM", "CAMPGROUND", "FRIENDSHIP", "SKYSCRAPER",
        "SUPERHUMAN", "FINGERPRINT", "MASTERPIECE", "LOUDSPEAKER"]
Color = ["BLACK", "WHITE", "RED", "GREEN", "BLUE", "GREY"]

Font = pygame.font.Font("freesansbold.ttf", 33)
Font2 = pygame.font.Font("freesansbold.ttf", 20)


def random_number(choice):
    random_num = 0
    if choice == 1:
        random_num = random.randint(0, len(easy) - 1)
    elif choice == 2:
        random_num = random.randint(0, len(medium) - 1)
    elif choice == 3:
        random_num = random.randint(0, len(hard) - 1)
    elif choice == 4:
        random_num = random.randint(0, len(Color) - 1)  # as elements of color is 0,1,2,3,4
    return random_num


def pick_from_list(number, choice):
    word = None
    if choice == 1:
        word = easy[number]
    elif choice == 2:
        word = medium[number]
    elif choice == 3:
        word = hard[number]
    elif choice == 4:
        word = Color[number]
    return word


def Hangman(condition):
    if condition == 0:
        pygame.draw.line(display, GREY, (10, 400), (300, 400), 8)  # baseline
        pygame.draw.line(display, GREY, (50, 50), (50, 400), 8)  # stick1
        pygame.draw.line(display, GREY, (50, 60), (250, 60), 8)  # stick2
        pygame.draw.line(display, GREY, (150, 60), (150, 100), 8)  # rope
        pygame.draw.circle(display, GREY, (150, 150), 50, 8)  # head
        pygame.draw.line(display, GREY, (150, 200), (150, 300), 8)  # body
        pygame.draw.line(display, GREY, (150, 210), (100, 250), 8)  # lefthand
        pygame.draw.line(display, GREY, (150, 210), (200, 250), 8)  # righthand
        pygame.draw.line(display, GREY, (150, 300), (100, 350), 8)  # leftleg
        pygame.draw.line(display, GREY, (150, 300), (200, 350), 8)  # rightleg

    elif condition == 1:
        pygame.draw.line(display, BLACK, (10, 400), (300, 400), 8)  # baseline
    elif condition == 2:
        pygame.draw.line(display, BLACK, (50, 50), (50, 400), 8)  # stick1
    elif condition == 3:
        pygame.draw.line(display, BLACK, (50, 60), (250, 60), 8)  # stick2
    elif condition == 4:
        pygame.draw.line(display, BLACK, (150, 60), (150, 100), 8)  # rope
    elif condition == 5:
        pygame.draw.circle(display, BLACK, (150, 150), 50, 8)  # head
    elif condition == 6:
        pygame.draw.line(display, BLACK, (150, 200), (150, 300), 8)  # body
    elif condition == 7:
        pygame.draw.line(display, BLACK, (150, 210), (100, 250), 8)  # lefthand
    elif condition == 8:
        pygame.draw.line(display, BLACK, (150, 210), (200, 250), 8)  # righthand
    elif condition == 9:
        pygame.draw.line(display, BLACK, (150, 300), (100, 350), 8)  # leftleg
    elif condition == 10:
        pygame.draw.line(display, BLACK, (150, 300), (200, 350), 8)  # rightleg
    elif condition == 11:  # GAME OVER
        pygame.draw.line(display, BLUE, (10, 400), (300, 400), 8)  # baseline
        pygame.draw.line(display, BLUE, (50, 50), (50, 400), 8)  # stick1
        pygame.draw.line(display, BLUE, (50, 60), (250, 60), 8)  # stick2
        pygame.draw.line(display, BLUE, (150, 60), (150, 100), 8)  # rope
        pygame.draw.circle(display, BLUE, (150, 150), 50, 8)  # head
        pygame.draw.line(display, BLUE, (150, 200), (150, 300), 8)  # body
        pygame.draw.line(display, BLUE, (150, 210), (100, 250), 8)  # lefthand
        pygame.draw.line(display, BLUE, (150, 210), (200, 250), 8)  # righthand
        pygame.draw.line(display, BLUE, (150, 300), (100, 350), 8)  # leftleg
        pygame.draw.line(display, BLUE, (150, 300), (200, 350), 8)  # rightleg


def PreHangMan():
    pygame.draw.line(display, GREEN, (10, 400), (190, 400), 8)  # baseline
    pygame.draw.line(display, GREEN, (30, 90), (30, 400), 8)  # stick1
    pygame.draw.line(display, GREEN, (30, 100), (160, 100), 8)  # stick2
    pygame.draw.line(display, GREEN, (100, 100), (100, 120), 8)  # rope
    pygame.draw.circle(display, GREEN, (100, 170), 50, 8)  # head
    pygame.draw.line(display, GREEN, (100, 220), (100, 320), 8)  # body
    pygame.draw.line(display, GREEN, (100, 230), (50, 270), 8)  # lefthand
    pygame.draw.line(display, GREEN, (100, 230), (150, 270), 8)  # righthand
    pygame.draw.line(display, GREEN, (100, 320), (50, 360), 8)  # leftleg
    pygame.draw.line(display, GREEN, (100, 320), (150, 360), 8)  # rightleg


def StartScreen():
    display.blit(pygame.font.Font("freesansbold.ttf", 40).render("HANGMAN", True, BLACK), (20, 20))
    display.blit(Font2.render("by JCLOH", True, BLACK), (60, 60))
    display.blit(Font.render("Level Difficulty", True, BLACK), (200, 150))
    display.blit(Font2.render("1-Easy", True, BLACK), (200, 200))
    display.blit(Font2.render("2-Medium", True, BLACK), (200, 250))
    display.blit(Font2.render("3-Hard", True, BLACK), (200, 300))
    display.blit(Font2.render("4-Color", True, GREY), (200, 350))


def main():
    the_choice = 0

    StartScreen()
    PreHangMan()

    # background music
    pygame.mixer.music.load('Music/KM/Two_Finger_Johnny.mp3')
    pygame.mixer.music.play(-1, 0)

    in_menu = True
    while in_menu:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                # print(in_menu)
                if event.key == K_1 or event.key == 257:  # 257 is 1 in numpad
                    the_choice = 1
                    in_menu = False
                    break
                elif event.key == K_2 or event.key == 258:  # 258 is 2 in numpad
                    the_choice = 2
                    in_menu = False
                    break
                elif event.key == K_3 or event.key == 259:  # 259 is 3 in numpad
                    the_choice = 3
                    in_menu = False
                    break
                elif event.key == K_4 or event.key == 260:  # 260 is 4 in numpad
                    the_choice = 4
                    in_menu = False
                    break

            elif event.type == MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pressed())
                if pygame.mouse.get_pressed() != (0, 0, 0):  # Scroller of mouse
                    pygame.mixer.Sound('Music/Mouse_Click_Fast.wav').play()

                # Easy
                if 200 < pygame.mouse.get_pos()[0] < 265 and 200 < pygame.mouse.get_pos()[1] < 215:
                    the_choice = 1
                    in_menu = False
                    break
                # Medium
                elif 200 < pygame.mouse.get_pos()[0] < 295 and 250 < pygame.mouse.get_pos()[1] < 265:
                    the_choice = 2
                    in_menu = False
                    break
                # Hard
                elif 200 < pygame.mouse.get_pos()[0] < 265 and 300 < pygame.mouse.get_pos()[1] < 315:
                    the_choice = 3
                    in_menu = False
                    break
                # Color
                elif 200 < pygame.mouse.get_pos()[0] < 270 and 350 < pygame.mouse.get_pos()[1] < 365:
                    the_choice = 4
                    in_menu = False
                    break

        if the_choice != 0:
            display.fill(WHITE)

        pygame.display.update()
        pygame.time.Clock().tick(30)  # 30fps

    # This is to make sure the word and random number is constant
    the_num = random_number(the_choice)
    the_word = pick_from_list(the_num, the_choice)
    print(the_word)

    empty_list = []
    for i in range(len(the_word)):
        empty_list.append('-')

    hidden = Font.render("".join(empty_list), True, BLACK)
    hidden_rect = hidden.get_rect()
    hidden_rect.center = (350, 250)
    display.blit(hidden, hidden_rect)

    condition = 0  # if condition is 10, then end game
    off = 0  # quit game at game over and congrats

    the_time = 0
    start = time.time()  # current time

    display.blit(Font2.render("Time(s):", True, BLACK), (300, 10))

    last_key_pressed = ""

    display.blit(pygame.font.Font("freesansbold.ttf", 15).render("Press 0 to quit game", True, BLACK), (20, 10))

    while True:
        Hangman(condition)
        end = time.time()  # end time
        if int(end) - int(start) == 1:
            pygame.draw.rect(display, WHITE, (385, 0, 100, 50))  # hide time
            the_time = the_time + 1
            # print(the_time, 'seconds has passed')
            timer = Font2.render(str(the_time), True, BLACK)
            display.blit(timer, (400, 10))
            start = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                pygame.mixer.Sound('Music/Keyboard.wav').play()

                # if exit key is pressed
                last_key_pressed = event.key
                pygame.draw.rect(display, WHITE, (220, 200, 280, 100))  # hide word
                pygame.draw.rect(display, WHITE, (260, 50, 200, 100))  # hide invalid input

                # This is use to check if it changes the ASCII int value to the char
                if re.search("[a-z]", chr(event.key)):
                    if (chr(event.key).upper() in the_word) or (chr(event.key).lower() in the_word):  # letter in word
                        for i in range(len(the_word)):
                            if (the_word[i] == (chr(event.key)).upper()) or (the_word[i] == (chr(event.key)).lower()):
                                empty_list[i] = the_word[i]

                    else:
                        condition = condition + 1  # letter not in word

                    hidden = Font.render("".join(empty_list), True, BLACK)
                    hidden_rect = hidden.get_rect()
                    hidden_rect.center = (350, 250)
                    display.blit(hidden, hidden_rect)

                else:
                    if event.key == K_0 or event.key == 256:  # 256 is 0 in numpad
                        display.blit(Font.render("EXIT?", True, RED), (340, 220))
                        display.blit(Font2.render("Yes", True, BLUE), (340, 270))
                        display.blit(Font2.render("No", True, BLUE), (415, 270))
                    else:
                        input = Font2.render("INVALID INPUT!!!", True, RED)
                        input_rect = input.get_rect()
                        input_rect.center = (350, 100)
                        display.blit(input, input_rect)
                        display.blit(hidden, hidden_rect)

            elif event.type == KEYUP:
                pygame.draw.rect(display, WHITE, (260, 50, 200, 100))  # hide invalid input

            elif event.type == MOUSEBUTTONDOWN:
                # print("mouse pressed")
                # print(pygame.mouse.get_pressed())
                if pygame.mouse.get_pressed() != (0, 0, 0):  # Scroller of mouse
                    pygame.mixer.Sound('Music/Mouse_Click_Fast.wav').play()

                if last_key_pressed == K_0 or last_key_pressed == 256:  # 256 is 0 in numpad
                    if pygame.mouse.get_pressed() == LEFT_CLICK:
                        # Yes
                        if 340 < pygame.mouse.get_pos()[0] < 385 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.draw.rect(display, WHITE, (340, 270, 35, 25))  # hide yes
                            display.blit(Font2.render("Yes", True, GREEN), (340, 270))
                            # print(pygame.mouse.get_pos())
                            print("YES")

                        # NO
                        elif 415 < pygame.mouse.get_pos()[0] < 450 and 270 < pygame.mouse.get_pos()[1] < 285:
                            pygame.draw.rect(display, WHITE, (415, 270, 35, 25))  # hide no
                            display.blit(Font2.render("No", True, GREEN), (415, 270))
                            # print(pygame.mouse.get_pos())
                            print("NO")

            elif event.type == MOUSEBUTTONUP:  # Yes
                if last_key_pressed == K_0 or last_key_pressed == 256:  # 256 is 0 in numpad
                    # Yes
                    if 340 < pygame.mouse.get_pos()[0] < 385 and 270 < pygame.mouse.get_pos()[1] < 285:

                        # quit game
                        pygame.quit()
                        sys.exit()

                    # No
                    elif 415 < pygame.mouse.get_pos()[0] < 450 and 270 < pygame.mouse.get_pos()[1] < 285:
                        pygame.draw.rect(display, WHITE, (415, 270, 35, 25))  # hide no
                        display.blit(Font2.render("No", True, GREEN), (415, 270))
                        pygame.draw.rect(display, WHITE, (300, 200, 200, 100))  # hide exit, yes,no

                        hidden = Font.render("".join(empty_list), True, BLACK)
                        hidden_rect = hidden.get_rect()
                        hidden_rect.center = (400, 250)
                        display.blit(hidden, hidden_rect)

                        last_key_pressed = ""

                    else:
                        pygame.draw.rect(display, WHITE, (340, 270, 35, 25))  # hide yes
                        display.blit(Font2.render("Yes", True, BLUE), (340, 270))
                        pygame.draw.rect(display, WHITE, (415, 270, 35, 25))  # hide no
                        display.blit(Font2.render("No", True, BLUE), (415, 270))

        # Check if the word is word and the condition
        if condition == 10:
            display.fill(WHITE)
            Hangman(condition + 1)
            Over = Font2.render("GAME OVER!!!", True, RED)
            OverRect = Over.get_rect()
            OverRect.center = (400, 250)
            display.blit(Over, OverRect)
            off = 1

            # stop the BGM
            pygame.mixer.music.stop()

            pygame.mixer.music.load('Music/KM/Loping_Sting.mp3')
            pygame.mixer.music.play(0, 0)

        elif the_word == "".join(empty_list):
            display.fill(WHITE)
            Cong = Font.render("CONGRATS!!!", True, GREEN)
            CongRect = Cong.get_rect()
            CongRect.center = (250, 220)
            display.blit(Cong, CongRect)

            Word = Font2.render("The word is:", True, BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (250, 250)
            display.blit(Word, WordRect)

            Word2 = Font.render(the_word, True, BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (250, 285)
            display.blit(Word2, Word2Rect)

            off = 1

            # stop the BGM
            pygame.mixer.music.stop()

            pygame.mixer.music.load('Music/KM/Loping_Sting.mp3')
            pygame.mixer.music.play(0, 0)

        pygame.display.update()
        pygame.time.Clock().tick(30)  # 30fps

        if off == 1:
            # wait 5 seconds
            time.sleep(5)
            # quit game
            pygame.quit()
            sys.exit()


main()
