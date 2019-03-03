#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

from GameView import *


class Game:
    NUMBER_OF_CHIPS = GameBoard.BOARD_SIZE

    def __init__(self):
        self.gamer = 1
        self.playedChips = 0
        self.potentialWinner = False
        self.gameView = GameView()

    def get_gamer(self):
        if self.playedChips % 2 == 0:
            gamer_id = GameBoard.ROUND_CHIP
        else:
            gamer_id = GameBoard.CROSS_CHIP
        return gamer_id

    def display_winner(self):
        if self.gamer == "" or self.gamer is None:
            return "personne n'a gagne"
        else:
            return self.gamer + " a gagne"

    def start(self):
        self.gameView.gameBoard.display()
        while self.potentialWinner != GameBoard.ROUND_CHIP_STRING \
                and self.potentialWinner != GameBoard.CROSS_CHIP_STRING \
                and self.playedChips < Game.NUMBER_OF_CHIPS:
            time.sleep(0.05)
            for event in self.gameView.pyGame.event.get():
                if event.type == self.gameView.pyGame.MOUSEBUTTONUP:
                    gamer = self.get_gamer()
                    print("gamer")
                    print(gamer)

                    print("PLAYED_CHIPS: "+str(self.playedChips))

                    y, x = self.gameView.pyGame.mouse.get_pos()
                    print("UX__X,Y: "+str(x)+","+str(y))

                    column = self.gameView.determine_column(x)
                    line = self.gameView.determine_line(y)
                    print("MODEL__X,Y: "+str(line)+","+str(column))

                    successfully_chip_putted_on_board = self.gameView.gameBoard.put_chip(column, line, gamer)
                    if successfully_chip_putted_on_board:
                        print('PUT CHIP SUCCESSFULLY')
                        self.playedChips += 1

                    self.potentialWinner = self.gameView.gameBoard.get_winner()
                    print("GAGNANT ? : " + str(self.potentialWinner))
                    self.gameView.render()
                    self.gameView.pyGame.display.flip()

                if event.type == self.gameView.pyGame.QUIT:
                    sys.exit(0)
