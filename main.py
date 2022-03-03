import pygame
import time
from copy import deepcopy
import random

turn = 0
gameover = 0
modeGame = 1
WIDTH = 1000
HEIGHT = 700
# pygame initializer
pygame.init()

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('OTHELLO')

# colour definition
white = (255, 255, 255)
black = (0, 0, 0)
green = (93, 200, 99)
grey = (100, 100, 100)
blue = (0, 0, 100)

# mohreha
square = 600 // 8

numberOfBlack = 0
numberOfWhite = 0
possibleMoveNumber = 0


class piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # starting point (50 ,50)
        self.x = (square * (self.col) + (square // 2) + 50)
        self.y = (square * (self.row) + (square // 2) + 50)

    def calc_pos(self):
        self.x = square * self.col + square // 2
        self.y = square * self.row + square // 2

    def draw(self, win):
        r = (square // 2) - 7
        pygame.draw.circle(screen, self.color, (self.x, self.y), r)

    def __repr__(self):
        return str("W" if self.color == white else "B" if self.color == black else " ")


# Game board
class board:

    def __init__(self):
        self.board = []

    def get_board(self):
        return self.board

    def changeturn(self):
        global turn
        turn = (turn + 1) % 2

    def ai_move(self, board):
        self = board[0]
        return (board[0])

    def create_board(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                if i == 3 and j == 3:
                    self.board[i].append(piece(i, j, white))
                elif i == 3 and j == 4:
                    self.board[i].append(piece(i, j, black))
                elif i == 4 and j == 3:
                    self.board[i].append(piece(i, j, black))
                elif i == 4 and j == 4:
                    self.board[i].append(piece(i, j, white))
                else:
                    self.board[i].append(piece(i, j, None))

    def draw(self, win):
        # win.fill(green)
        x_d = 75
        y_d = 75
        x_s = 50
        y_s = 50
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(screen, black, [x_s, y_s, x_d, y_d], 1)
                x_s += x_d
            y_s += y_d
            x_s = 50
        pygame.draw.rect(screen, black, [50, 50, 600, 600], 2)
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color != None and self.board[i][j].color != grey:
                    pygame.draw.circle(screen, self.board[i][j].color, (self.board[i][j].x, self.board[i][j].y),
                                       (square // 2) - 7)

    def possiblemove(self, turn1):
        global gameover
        global turn
        global possibleMoveNumber
        possibleMoveNumber = 0
        global numberOfBlack
        numberOfBlack = 0
        global numberOfWhite
        numberOfWhite = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color != None and self.board[i][j] != grey:
                    if turn1 == 0:
                        if self.board[i][j].color == white:
                            numberOfWhite += 1
                        if self.board[i][j].color == black:
                            numberOfBlack += 1
                            # left
                            for x in range(j - 1, -1, -1):
                                color_black = self.board[i][x].color == black;
                                if color_black:
                                    break
                                color_grey_None = self.board[i][x].color == None or self.board[i][x].color == grey
                                if color_grey_None:
                                    if self.board[i][x + 1].color == white:
                                        self.board[i][x].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # right
                            for x in range(j + 1, 8, +1):
                                if self.board[i][x].color == black:
                                    break
                                color_grey_None = self.board[i][x].color == None or self.board[i][x].color == grey
                                if color_grey_None:
                                    if self.board[i][x - 1].color == white:
                                        self.board[i][x].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # up
                            for x in range(i - 1, -1, -1):
                                if self.board[x][j].color == black:
                                    break
                                color_grey_None = self.board[x][j].color == None or self.board[x][j].color == grey
                                if color_grey_None:
                                    if self.board[x + 1][j].color == white:
                                        self.board[x][j].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # down
                            for x in range(i + 1, 8, 1):
                                if self.board[x][j].color == black:
                                    break
                                color_grey_None = self.board[x][j].color == None or self.board[x][j].color == grey
                                if color_grey_None:
                                    if self.board[x - 1][j].color == white:
                                        self.board[x][j].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # leftup
                            tempi = i - 1
                            tempj = j - 1
                            while tempi >= 0 and tempj >= 0:
                                if self.board[tempi][tempj].color == black:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi + 1][tempj + 1].color == white:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi -= 1
                                tempj -= 1
                            # rightup
                            tempi = i - 1
                            tempj = j + 1
                            while tempi >= 0 and tempj < 8:
                                if self.board[tempi][tempj].color == black:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi + 1][tempj - 1].color == white:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi -= 1
                                tempj += 1
                            # rightdown
                            tempi = i + 1
                            tempj = j + 1
                            while tempi < 8 and tempj < 8:
                                if self.board[tempi][tempj].color == black or self.board[tempi][tempj].color == grey:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi - 1][tempj - 1].color == white:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi += 1
                                tempj += 1
                            # leftdown
                            tempi = i + 1
                            tempj = j - 1
                            while tempi < 8 and tempj >= 0:
                                if self.board[tempi][tempj].color == black:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi - 1][tempj + 1].color == white:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi += 1
                                tempj -= 1
                    if turn1 == 1:
                        if self.board[i][j].color == black:
                            numberOfBlack += 1
                        if self.board[i][j].color == white:
                            numberOfWhite += 1
                            # left
                            for x in range(j - 1, -1, -1):
                                if self.board[i][x].color == white:
                                    break
                                color_grey_None = self.board[i][x].color == None or self.board[i][x].color == grey
                                if color_grey_None:
                                    if self.board[i][x + 1].color == black:
                                        self.board[i][x].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # right
                            for x in range(j + 1, 8, +1):
                                if self.board[i][x].color == white:
                                    break
                                color_grey_None = self.board[i][x].color == None or self.board[i][x].color == grey
                                if color_grey_None:
                                    if self.board[i][x - 1].color == black:
                                        self.board[i][x].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # up
                            for x in range(i - 1, -1, -1):
                                if self.board[x][j].color == white:
                                    break
                                color_grey_None = self.board[x][j].color == None or self.board[x][j].color == grey
                                if color_grey_None:
                                    if self.board[x + 1][j].color == black:
                                        self.board[x][j].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # down
                            for x in range(i + 1, 8, 1):
                                if self.board[x][j].color == white:
                                    break
                                color_grey_None = self.board[x][j].color == None or self.board[x][j].color == grey
                                if color_grey_None:
                                    if self.board[x - 1][j].color == black:
                                        self.board[x][j].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                            # leftup
                            tempi = i - 1
                            tempj = j - 1
                            while tempi >= 0 and tempj >= 0:
                                if self.board[tempi][tempj].color == white:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi + 1][tempj + 1].color == black:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi -= 1
                                tempj -= 1
                            # rightup
                            tempi = i - 1
                            tempj = j + 1
                            while tempi >= 0 and tempj < 8:
                                if self.board[tempi][tempj].color == white:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi + 1][tempj - 1].color == black:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi -= 1
                                tempj += 1
                            # rightdown
                            tempi = i + 1
                            tempj = j + 1
                            while tempi < 8 and tempj < 8:
                                if self.board[tempi][tempj].color == white:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi - 1][tempj - 1].color == black:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi += 1
                                tempj += 1
                            # leftdown
                            tempi = i + 1
                            tempj = j - 1
                            while tempi < 8 and tempj >= 0:
                                if self.board[tempi][tempj].color == white:
                                    break
                                color_grey_None = self.board[tempi][tempj].color == None or self.board[tempi][
                                    tempj].color == grey
                                if color_grey_None:
                                    if self.board[tempi - 1][tempj + 1].color == black:
                                        self.board[tempi][tempj].color = grey
                                        possibleMoveNumber += 1
                                        break
                                    else:
                                        break
                                tempi += 1
                                tempj -= 1

    # if possibleMoveNumber == 0:
    #    gameover+=1
    #   self.changeturn();
    # else :
    #   gameover=0
    # if not possibleMoveNumber:
    #   gameover += 1
    #  self.changeturn()
    # else:
    #   gameover = 0

    def hint(self):
        global turn
        global gameover
        global modeGame
        possiblemovebool = False
        self.possiblemove(turn)
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color == grey:
                    possiblemovebool = True
                    if turn == 0:
                        pygame.draw.circle(screen, (100, 100, 100),
                                           ((square * (j) + (square // 2) + 50), (square * (i) + (square // 2) + 50)),
                                           (square // 2) - 7)
                    elif turn == 1:
                        pygame.draw.circle(screen, (100, 0, 0),
                                           ((square * (j) + (square // 2) + 50), (square * (i) + (square // 2) + 50)),
                                           (square // 2) - 7)
        if possiblemovebool == False:
            if modeGame == 2 or turn == 0:
                self.changeturn()
            gameover += 1
            return possiblemovebool
        else:
            gameover = 0
            return possiblemovebool

    def delet(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color == grey:
                    self.board[i][j].color = None

    def change_color(self, i, j, clr):
        self.board[i][j].color = clr

    def evaluate(self):
        global possibleMoveNumber
        global numberOfBlack
        global numberOfWhite
        corw = 0
        corb = 0
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for i in corners:
            if self.board[i[0]][i[1]].color != None:
                if self.board[i[0]][i[1]].color == white:
                    corw += 1
                elif self.board[i[0]][i[1]].color == black:
                    corb += 1
        self.possiblemove(1)
        mobw = possibleMoveNumber
        self.delet()
        self.possiblemove(0)
        mobb = possibleMoveNumber
        numb = numberOfBlack
        numw = numberOfWhite
        self.delet()
        eval = (corw - corb) * 1000 + (mobw - mobb) * 15 + (numw - numb) * 10 + random.randint(-20, 20) * 0.15
        return eval
        # return random.randint(-100, 100)

    def game_over(self):
        global gameover
        if gameover > 1:
            return False
        else:
            return True

    def add(self, i, j, color):
        global turn
        global modeGame
        if self.board[i][j].color == grey:
            self.board[i][j] = piece(i, j, color)
            self.delet()
            # right
            for x in range(j - 1, -1, -1):
                if self.board[i][x].color == None:
                    break
                if self.board[i][x].color == color:
                    for t in range(x, j, 1):
                        self.change_color(i, t, color)
                    break
            # left
            for x in range(j + 1, 8, 1):
                if self.board[i][x].color == None:
                    break
                if self.board[i][x].color == color:
                    for t in range(j, x, 1):
                        self.change_color(i, t, color)
                    break
            # down
            for x in range(i - 1, -1, -1):
                if self.board[x][j].color == None:
                    break
                if self.board[x][j].color == color:
                    for t in range(x, i, 1):
                        self.change_color(t, j, color)
                    break
            # up
            for x in range(i + 1, 8, 1):
                if self.board[x][j].color == None:
                    break
                if self.board[x][j].color == color:
                    for t in range(i, x, 1):
                        self.change_color(t, j, color)
                    break
            # rightdown
            tempi = i - 1
            tempj = j - 1
            while tempi >= 0 and tempj >= 0:
                if self.board[tempi][tempj].color == None:
                    break
                if self.board[tempi][tempj].color == color:
                    while tempi < i:
                        self.change_color(tempi + 1, tempj + 1, color)
                        tempi += 1
                        tempj += 1
                    break
                tempi -= 1
                tempj -= 1
            # leftdown
            tempi = i - 1
            tempj = j + 1
            while tempi >= 0 and tempj < 8:
                if self.board[tempi][tempj].color == None:
                    break
                if self.board[tempi][tempj].color == color:
                    while tempi < i:
                        self.change_color(tempi + 1, tempj - 1, color)
                        tempi += 1
                        tempj -= 1
                    break
                tempi -= 1
                tempj += 1
            # rightup
            tempi = i + 1
            tempj = j - 1
            while tempi < 8 and tempj >= 0:
                if self.board[tempi][tempj].color == None:
                    break
                if self.board[tempi][tempj].color == color:
                    while tempi > i and tempj < j:
                        self.change_color(tempi - 1, tempj + 1, color)
                        tempi -= 1
                        tempj += 1
                    break
                tempi += 1
                tempj -= 1
            # rightdown
            tempi = i + 1
            tempj = j + 1
            while tempi < 8 and tempj < 8:
                if self.board[tempi][tempj].color == None:
                    break
                if self.board[tempi][tempj].color == color:
                    while tempi > i:
                        self.change_color(tempi, tempj, color)
                        tempi -= 1
                        tempj -= 1
                    break
                tempi += 1
                tempj += 1
            if modeGame == 2 or turn == 0:
                self.changeturn()

    def simulate_move(self, move, game):
        global turn
        self.add(move.row, move.col, white if turn == 1 else black)
        return self

    def get_all_moves(self, turn, game):
        validmoves = []
        moves = []
        self.possiblemove(turn)
        for i in range(8):
            for j in range(8):
                if self.board[i][j].color == grey:
                    validmoves.append(self.board[i][j])

        for move in validmoves:
            temp_board = deepcopy(self)
            new_board = temp_board.simulate_move(move, game)
            moves.append([new_board, move])
        self.delet()
        return moves


def get_from_mouse(pos):
    x, y = pos
    row = (x + 25) // 75
    col = (y + 25) // 75
    return row, col


def corner(list):
    yes = []
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for i in list:
        if (i[1].row, i[1].col) in corners:
            yes.append(i)
    if len(yes) != 0:
        return yes
    return list


def alphabeta(board, depth, max_player, game, alpha, beta):
    if depth == 0 or not board.hint():
        return board.evaluate(), board

    if max_player:
        maxeval = float('-inf')
        best_move = None
        moves = board.get_all_moves(1, game)
        moves = corner(moves)
        moves = mapper(moves, 1, depth)
        for move in moves:
            evaluation = alphabeta(move[1][0], depth - 1, False, game, alpha, beta)[0]
            maxeval = max(maxeval, evaluation)
            alpha = max(evaluation, alpha)
            if maxeval == evaluation:
                best_move = move
            if alpha >= beta:
                # maxeval = float('inf')
                # best_move = game
                break
        return maxeval, best_move
    else:
        mineval = float('inf')
        best_move = None
        moves = board.get_all_moves(0, game)
        moves = corner(moves)
        moves = mapper(moves, 0, depth)

        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

        for move in moves:
            evaluation = alphabeta(move[1][0], depth - 1, True, game, alpha, beta)[0]
            mineval = min(mineval, evaluation)
            beta = min(beta, evaluation)
            if mineval == evaluation:
                best_move = move
            if alpha >= beta:
                # mineval = float('-inf')
                # best_move = game
                break

        return mineval, best_move


def mapper(list, turn, depth):
    map = []
    point = 0
    score = [[16.16, -3.3, 0.99, 0.43, 0.43, 0.99, -3.3, 16.16],
             [-4.12, -1.81, -8.08, -0.27, -0.27, -8.08, -1.81, -4.12],
             [1.33, -0.04, 0.51, 0.07, 0.07, 0.51, -0.04, 1.33],
             [0.63, -0.18, -0.04, -0.01, -0.01, -0.04, -0.18, 0.63],
             [0.63, -0.18, -0.04, -0.01, -0.01, -0.04, -0.18, 0.63],
             [1.33, -0.04, 0.51, 0.07, 0.07, 0.51, -0.04, 1.33],
             [-4.12, -1.81, -8.08, -0.27, -0.27, -8.08, -1.81, -4.12],
             [16.16, -3.3, 0.99, 0.43, 0.43, 0.99, -3.3, 16.16]
             ]
    for board in list:
        for i in range(8):
            for j in range(8):
                if board[0].board[i][j].color != None:
                    point += score[i][j] if board[0].board[i][j].color == white else -1 * score[i][j]

        map.append((point, board))
        point = 0

    def sortSecond(val):
        return val[0]

    if turn == 1:
        map.sort(key=sortSecond, reverse=True)
    else:
        map.sort(key=sortSecond)
    if depth == 1:
        return map[0:5]
    else:
        return map[0:3]
    return map


def minimax(board, depth, max_player, game):
    if depth == 0 or not board.hint():
        return board.evaluate(), board

    if max_player:
        maxeval = float('-inf')
        best_move = None
        for move in board.get_all_moves(1, game):
            evaluation = minimax(move[0], depth - 1, False, game)[0]
            maxeval = max(maxeval, evaluation)
            if maxeval == evaluation:
                best_move = move
        return maxeval, best_move
    else:
        mineval = float('inf')
        best_move = None
        for move in board.get_all_moves(0, game):
            evaluation = minimax(move[0], depth - 1, True, game)[0]
            mineval = min(mineval, evaluation)
            if mineval == evaluation:
                best_move = move
        return mineval, best_move


FPS = 60


def main1player():
    global modeGame
    modeGame = 1
    b = board()
    # Game loop
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 60)
    font2 = pygame.font.Font('freesansbold.ttf', 40)
    b.create_board()
    running = True
    while running:
        # clock.tick(FPS)
        if turn == 1:
            # for i in range(8):
            # print(b.board[i])
            mydepth = 10
            value, newboard = alphabeta(b, mydepth, True, b, float('-inf'), float('+inf'))[1]
            # value, newboard = minimax(b, mydepth, True, b)
            b = b.ai_move(newboard)
            # print("-------------------------------------------------------------------------------")
            # print()
            # for i in range(8):
            #   print(b.board[i])
            # print("-------------------------------------------------------------------------------")
            pygame.draw.circle(screen, (0, 0, 200), (
                (square * (newboard[1].col) + (square // 2) + 50), (square * (newboard[1].row) + (square // 2) + 50)),
                               (square // 2) - 7)
            pygame.display.update()
            time.sleep(0.5)
            b.changeturn()
        b.hint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 650 and pos[0] > 49:
                    if pos[1] < 650 and pos[1] > 49:
                        col, row = get_from_mouse(pos)
                        if turn == 0:
                            b.add(row - 1, col - 1, black)
                            pygame.display.update()

        screen.fill(green)
        text1 = font.render("{}".format(numberOfBlack), True, black, None)
        textRect1 = text1.get_rect()
        textRect1.center = (700, 350)
        text2 = font.render("{}".format(numberOfWhite), True, white, None)
        textRect2 = text2.get_rect()
        textRect2.center = (700, 425)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        nobat = font2.render("TURN = {}".format("Black" if turn == 0 else "White"), True, black if turn == 0 else white,
                             None)
        nobatrect = nobat.get_rect()
        nobatrect.center = (800, 100)
        screen.blit(nobat, nobatrect)
        b.draw(screen)
        b.hint()
        pygame.display.update()

        if running:
            running = b.game_over()
    time.sleep(3)
    font = pygame.font.Font('freesansbold.ttf', 60)
    if numberOfBlack > numberOfWhite:
        text = font.render("Winner is Black", True, green, blue)

    elif numberOfBlack < numberOfWhite:
        text = font.render("Winner is White", True, green, blue)

    else:
        text = font.render("GAME TIE", True, green, blue)

    textRect = text.get_rect()
    textRect.center = (500, 350)
    screen.fill(green)
    screen.blit(text, textRect)
    pygame.display.update()

    time.sleep(3)
    pygame.quit()


# --------------------------------------------------------------------------------------------------------------------
def main2player():
    global modeGame
    modeGame = 2
    b = board()
    # Game loop
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 60)
    font2 = pygame.font.Font('freesansbold.ttf', 40)
    b.create_board()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 650 and pos[0] > 49:
                    if pos[1] < 650 and pos[1] > 49:
                        col, row = get_from_mouse(pos)
                        if turn == 0:
                            b.add(row - 1, col - 1, black)

                        elif turn == 1:
                            b.add(row - 1, col - 1, white)

        screen.fill(green)

        text1 = font.render("{}".format(numberOfBlack), True, black, None)
        textRect1 = text1.get_rect()
        textRect1.center = (700, 350)
        text2 = font.render("{}".format(numberOfWhite), True, white, None)
        textRect2 = text2.get_rect()
        textRect2.center = (700, 425)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        nobat = font2.render("TURN = {}".format("Black" if turn == 0 else "White"), True, black if turn == 0 else white,
                             None)
        nobatrect = nobat.get_rect()
        nobatrect.center = (800, 100)
        screen.blit(nobat, nobatrect)
        b.draw(screen)
        b.hint()
        if running:
            running = b.game_over()

        pygame.display.update()
    font = pygame.font.Font('freesansbold.ttf', 60)
    if numberOfBlack > numberOfWhite:
        text = font.render("Winner is Black", True, green, blue)

    elif numberOfBlack < numberOfWhite:
        text = font.render("Winner is White", True, green, blue)

    else:
        text = font.render("GAME TIE", True, green, blue)

    textRect = text.get_rect()
    textRect.center = (500, 350)
    screen.fill(green)
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


def menu():
    color = (255, 255, 255)
    width = screen.get_width()
    height = screen.get_height()

    # defining a font
    smallfont = pygame.font.SysFont('MachineGunk', 60)
    Welcom = pygame.font.SysFont('MachineGunk', 100)

    # this font
    text1 = smallfont.render('1 player', True, color)
    text2 = smallfont.render('2 player', True, color)
    wel = Welcom.render("OTHELLO ", True, (0, 0, 0))
    RUN = True
    while RUN:
        screen.fill((0, 100, 60))
        mouse = pygame.mouse.get_pos()

        if width / 2 - 100 <= mouse[0] <= width / 2 + 100 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, (0, 0, 0), [width / 2 - 120, height / 2, 230, 55])

        if width / 2 - 100 <= mouse[0] <= width / 2 + 80 and height / 2 - 100 <= mouse[1] <= height / 2 - 50:
            pygame.draw.rect(screen, (0, 0, 0), [width / 2 - 120, height / 2 - 100, 230, 55])

        screen.blit(wel, (width / 2 - 150, height / 2 - 300))
        screen.blit(text1, (width / 2 - 100, height / 2 - 100))
        screen.blit(text2, (width / 2 - 100, height / 2))

        pygame.display.update()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                RUN = False
                break

            if ev.type == pygame.MOUSEBUTTONDOWN:

                if width / 2 - 100 <= mouse[0] <= width / 2 + 100 and height / 2 <= mouse[1] <= height / 2 + 40:
                    RUN = False
                    main2player()
                elif width / 2 - 100 <= mouse[0] <= width / 2 + 80 and height / 2 - 100 <= mouse[1] <= height / 2 - 50:
                    RUN = False
                    main1player()


menu()
