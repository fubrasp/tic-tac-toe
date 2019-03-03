#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GameBoard:
    EMPTY_BOX = 0
    CROSS_CHIP = -1
    ROUND_CHIP = 1
    BOARD_WIDTH = 3
    ROUND_WIN = BOARD_WIDTH
    CROSS_WIN = -BOARD_WIDTH
    BOARD_LENGTH = BOARD_WIDTH
    BOARD_SIZE = BOARD_LENGTH * BOARD_WIDTH
    CROSS_CHIP_STRING = "cross"
    ROUND_CHIP_STRING = "round"

    def __init__(self):
        # COLUMN
        # WIDTH
        self.board = [
            [GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX],#L L
            [GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX],#E I
            [GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX, GameBoard.EMPTY_BOX],#N N
        ]                                                                   #GTH E

    def get_horizontal_winner(self):
        for index_line in range(0, GameBoard.BOARD_LENGTH):
            sum_current_line = 0
            for index_column in range(0, GameBoard.BOARD_WIDTH):
                print(str(index_line)+"-"+str(index_column))
                sum_current_line += self.board[index_line][index_column]
            if sum_current_line == GameBoard.ROUND_WIN:
                return GameBoard.ROUND_CHIP_STRING
            if sum_current_line == GameBoard.CROSS_WIN:
                return GameBoard.CROSS_CHIP_STRING
        return ""

    def get_vertical_winner(self):
        for index_column in range(0, GameBoard.BOARD_WIDTH):
            sum_current_column = 0
            for index_line in range(0, GameBoard.BOARD_LENGTH):
                sum_current_column += self.board[index_line][index_column]
            if sum_current_column == GameBoard.ROUND_WIN:
                return GameBoard.ROUND_CHIP_STRING
            if sum_current_column == GameBoard.CROSS_WIN:
                return GameBoard.CROSS_CHIP_STRING
        return ""

    def get_diagonals_winner(self):
        sum_first_diagonal = 0
        for index in range(0, GameBoard.BOARD_WIDTH):
            sum_first_diagonal += self.board[index][index]

        # FIXME
        sum_second_diagonal = self.board[0][2] + self.board[1][1] + self.board[2][0]

        if sum_first_diagonal == GameBoard.ROUND_WIN or sum_second_diagonal == GameBoard.ROUND_WIN:
            return GameBoard.ROUND_CHIP_STRING
        if sum_first_diagonal == GameBoard.CROSS_WIN or sum_second_diagonal == GameBoard.CROSS_WIN:
            return GameBoard.CROSS_CHIP_STRING
        return ""

    def get_winner(self):
        gamer = self.get_horizontal_winner()
        print("H_W: "+str(gamer))
        if gamer != "":
            return gamer
        gamer = self.get_vertical_winner()
        print("V_W: "+str(gamer))
        if gamer != "":
            return gamer
        gamer = self.get_diagonals_winner()
        print("DG_W: "+str(gamer))
        if gamer != "":
            return gamer

    def put_chip(self, line, column, gamer):
        if self.board[line][column] == GameBoard.EMPTY_BOX:
            if gamer == GameBoard.ROUND_CHIP:
                self.board[line][column] = GameBoard.ROUND_CHIP
                return True
            else:
                self.board[line][column] = GameBoard.CROSS_CHIP
                return True
        return False

    def display(self):
        print("\n")
        for line in range(len(self.board)):
            for column in range(len(self.board[line])):
                print(self.board[line][column], end=' ')
            print()
        print("\n")

    def reverse_game_board(self):
        reversed_game_board = []
        for row in range(GameBoard.BOARD_LENGTH, 0, -1):
            reversed_game_board.append(self.board[row])
        return reversed_game_board
