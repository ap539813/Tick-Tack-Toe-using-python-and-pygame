#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 04:10:22 2019

@author: ankush
"""

import pygame
pygame.init()

pygame.mixer.init()
# creating window

screen_width = 900
screen_height = 960
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake game")
X = pygame.image.load('X.jpg')
O = pygame.image.load('O.jpg')
red = (255, 0, 0)

# Game specific variables
start_on = True
turn = 0

def start_game():
    exit_game = False
    game_over = False
    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Snake Chan", 29)
    font2 = pygame.font.SysFont("Snake Chan", 45)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return exit_game, game_over, FPS, clock, font, font2, board

exit_game, game_over, FPS, clock, font, font2, board = start_game()

def win_check(player):
    print(board)
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return 'vertical'
        if board[i][0] == board[i][1] == board[i][2] == player:
            return 'horizontal'
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return 'diagonal'

    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 'draw'
    return False

def drawboard():
    pygame.draw.line(gameWindow, (0, 0, 0), (300, 0), (300, 900), 5)
    pygame.draw.line(gameWindow, (0, 0, 0), (600, 0), (600, 900), 5)
    pygame.draw.line(gameWindow, (0, 0, 0), (0, 300), (900, 300), 5)
    pygame.draw.line(gameWindow, (0, 0, 0), (0, 600), (900, 600), 5)
    pygame.draw.line(gameWindow, (0, 0, 0), (0, 900), (900, 900), 5)
    pygame.display.update()


def put_text(text, color, x, y, font):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


gameWindow.fill((255, 255, 255))
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = event.pos
            click_position = (300 * (click_position[0]//300), 300 * (click_position[1]//300))
            if turn == 0 and board[click_position[0]//300][click_position[1]//300] == 0:
                gameWindow.blit(X, click_position)
                board[click_position[0]//300][click_position[1]//300] = 'X'
                turn = 1
                if win_check('X') == 'draw':
                    drawboard()
                    put_text('match draw!. Press ENTER To Play More?', red, 10, 910, font)
                    game_over = True
                elif win_check('X'):
                    drawboard()
                    put_text('Player "X" WON!. Press ENTER To Play More?', red, 10, 910, font)
                    game_over = True

            elif turn == 1 and board[click_position[0]//300][click_position[1]//300] == 0:
                gameWindow.blit(O, click_position)
                board[click_position[0]//300][click_position[1]//300] = 'O'
                turn = 0
                if win_check('O'):
                    drawboard()
                    put_text('Player "O" WON!. Press ENTER To Play More?', red, 10, 910, font)
                    game_over = True
        pygame.display.update()
        clock.tick(FPS)
        while game_over == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit_game, game_over, FPS, clock, font, font2, board = start_game()
                        gameWindow.fill((255, 255, 255))
                    else:
                        game_over = False
                        exit_game = True
    drawboard()
    clock.tick(FPS)
pygame.quit()
