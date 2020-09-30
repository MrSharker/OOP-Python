from abc import abstractmethod


class Color():
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Board():                                          #Класс для создания поля и прорисовки фигур
    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        for i in range(8):
            self.board[1][i] = Pawn(Color.WHITE, 1, i)
            self.board[6][i] = Pawn(Color.BLACK, 6, i)
        self.board[0][0] = Rook(Color.WHITE, 0, 0)
        self.board[7][0] = Rook(Color.BLACK, 7, 0)
        self.board[0][7] = Rook(Color.WHITE, 0, 7)
        self.board[7][7] = Rook(Color.BLACK, 7, 7)

    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res

    def get_piece(self, x, y):                          #Функция для получения фигуры в клетке
        return self.board[y][x]

    def get_color(self, x, y):                          #Функция для получения цвета фигуры
        return self.get_piece(x, y).color

    def move_piece(self, x_from, y_from,):              #Функция для перемещения фигур на поле
        try:
            xy = self.get_piece(x_from, y_from).move(self.board)
            self.board[xy[1]][xy[0]] = self.board[y_from][x_from]
            self.board[y_from][x_from] = Empty()
            print(self)
        except:
            print("В этих координатах нет шахматной фигуры")


class Empty():                                          #Класс свободных клеток
    color = Color.EMPTY

    def move(self, board):
        raise Exception('Error !')

    def __str__(self):
        return '.'


class Piece():                                          #Класс шахматной фигуры(родительский)
    IMG = None

    def __init__(self, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_y
        self.pos_y = pos_x

    def __str__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]

    @abstractmethod
    def move(self, board):                              #Обастрактный метод, реализуемый в классах наследниках
        return []


class Pawn(Piece):                                      #Класс пешки, наследуемый от класса фигуры
    IMG = ('♙', '♟')

    def move(self, board):                              #Функция для движения пешки
        while True:
            print("Куда двигаем пешку? (x y)")
            xy = []
            xy = [int(i) for i in input().split()]
            if self.pos_x == xy[0] and self.pos_y != xy[1] and self.color == Color.WHITE and xy[1] < 7 \
                    and (xy[1] - self.pos_y) == 1:
                self.pos_y += 1
                break
            elif self.pos_x == xy[0] and self.pos_y != xy[1] and self.color == Color.BLACK and xy[1] > 1 \
                    and (self.pos_y - xy[1]) == 1:
                self.pos_y -= 1
                break
            else:
                print("Не правильный ход, попробуйте еще раз")
                continue
        return self.pos_x, self.pos_y


class Rook(Piece):                                      #Класс ладьи, наследуемый от класса фигуры
    IMG = ('♖', '♜')

    def move(self, board):                              #Функция для движения ладьи
        while True:
            print("Куда двигаем ладью? (x y)")
            xy = []
            xy = [int(i) for i in input().split()]
            if self.pos_x == xy[0] and self.pos_y != xy[1]:
                if self.color == Color.WHITE and 0 <= xy[1] <= 7:
                    self.pos_y = xy[1]
                    break
                elif self.color == Color.BLACK and 0 <= xy[1] <= 7:
                    self.pos_y = xy[1]
                    break
            elif self.pos_x != xy[0] and self.pos_y == xy[1]:
                if self.color == Color.BLACK and 0 <= xy[1] <= 7:
                    self.pos_x = xy[0]
                    break
                elif self.color == Color.WHITE and 0 <= xy[1] <= 7:
                    self.pos_y = xy[1]
                    break
            else:
                print("Не правильный ход, попробуйте еще раз")
                continue
        return self.pos_x, self.pos_y


b = Board()                                             #Проверка работы классов и их функций
print(b)
b.move_piece(4, 4)
b.move_piece(7, 7)
