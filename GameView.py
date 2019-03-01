#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pygame

from GameBoard import *


class GameView:
    IMAGE_DIRECTORY = "images"

    def __init__(self):
        self.gamer = 1
        self.gameBoard = GameBoard()
        self.pyGame = pygame
        pygame.init()
        pygame.display.set_caption('tic-tac-toe')
        self.board_picture = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "board.png"))
        taille_plateau_de_jeu = self.board_picture.get_size()

        print('taille plateau de jeu')
        print(taille_plateau_de_jeu)
        print(taille_plateau_de_jeu[0])
        print(taille_plateau_de_jeu[1])

        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.board_picture, (0, 0))
        pygame.display.flip()

        self.yellowChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "cross.png"))
        self.redChip = pygame.image.load(os.path.join(GameView.IMAGE_DIRECTORY, "round.png"))
        self.font = pygame.font.Font("freesansbold.ttf", 15)

    def determine_column(self, x):
        column = x + 8.75
        column /= 97
        if column < GameBoard.BOARD_WIDTH:
            return int(column)
        else:
            return GameBoard.BOARD_WIDTH-1

    def determine_line(self, y):
        line = y + 8.4
        line /= 97
        if line < GameBoard.BOARD_LENGTH:
            return int(line)
        else:
            return GameBoard.BOARD_LENGTH-1

    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.board_picture, (0, 0))

        game_board_game_state = self.gameBoard.board

        self.gameBoard.display()
        for i in range(len(game_board_game_state)):
            for j in range(len(game_board_game_state[i])):
                if game_board_game_state[i][j] == GameBoard.YELLOW_CHIP:
                    self.screen.blit(self.yellowChip, (8.75 + 97 * j, 8.4 + 97.5 * i))
                pygame.display.flip()
                if game_board_game_state[i][j] == GameBoard.RED_CHIP:
                    self.screen.blit(self.redChip, (8.75 + 97 * j, 8.4 + 97.5 * i+1))
                pygame.display.flip()

