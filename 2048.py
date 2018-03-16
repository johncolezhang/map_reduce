from random import choice


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def invert(matrix):
    return list(map(lambda row: row[::-1], matrix))

class Grid(object):
    def __init__(self):
        self.row = 4
        self.column = 4
        self.win_score = 2048
        self.current_score = 0
        self.grid = [[0 for i in range(self.row)] for j in range(self.column)]
        self.start()


    def start(self):
        self.current_score = 0
        self.initial_point()
        self.initial_point()


    def initial_point(self):
        """
        initial random number in random grid
        """
        new_number = choice([4] * 2 + [2] * 8)
        (i, j) = choice([(i, j) for i in range(self.row) for j in range(self.column) if self.grid[i][j] == 0])
        self.grid[i][j] = new_number


    def movable(self, direction):
        def left_movable_row(row):
            def left_movable_unit(u):
                # there's a empty when left move
                if row[u] == 0 and row[u + 1] != 0:
                    return True
                # there's a merge when left move
                if row[u] != 0 and row[u] == row[u + 1]:
                    return True
                return False

            return any(left_movable_unit(u) for u in range(self.column - 1))

        check = dict()
        # can left move or not
        check[ord('a')] = check[ord('A')] = lambda grid: any(map(left_movable_row, grid))
        # invert grid, right move equals left move
        check[ord('d')] = check[ord('D')] = lambda grid: check[ord('a')](invert(grid))
        # clockwise rotation, left move equals up move
        check[ord('w')] = check[ord('W')] = lambda grid: check[ord('a')](transpose(grid))
        # clockwise rotation, down move equals right move, left move equals invert of right move
        check[ord('s')] = check[ord('S')] = lambda grid: check[ord('d')](transpose(grid))
        return check[direction](self.grid)



    def move(self, direction):
        def left_move_row(row):
            # values in this row
            short_row = [i for i in row if i != 0]
            new_row, i = [], 0
            while i < len(short_row) - 1:
                # not equal, i + 1
                if short_row[i] != short_row[i + 1]:
                    new_row.append(short_row[i])
                    i += 1
                # equals, value*2, current_value increase, i move 2 index
                else:
                    new_row.append(short_row[i] * 2)
                    self.current_score += short_row[i] * 2
                    i += 2
            # finish merge
            if i == len(short_row) - 1:
                new_row.append(short_row[i])
            return new_row + [0] * (len(row) - len(new_row))

        moves = dict()
        moves[ord('a')] = moves[ord('A')] = lambda matrix: list(map(left_move_row, matrix))
        moves[ord('d')] = moves[ord('D')] = lambda matrix: invert(moves[ord('a')](invert(matrix)))
        moves[ord('w')] = moves[ord('W')] = lambda matrix: transpose(moves[ord('a')](transpose(matrix)))
        moves[ord('s')] = moves[ord('S')] = lambda matrix: transpose(moves[ord('d')](transpose(matrix)))

        if self.movable(direction):
            self.grid = moves[direction](self.grid)
            self.initial_point()
            return True
        else:
            return False


    def is_win(self):
        return any(any(i >= self.win_score for i in row) for row in self.grid)



    def is_lose(self):
        return not any(self.movable(ord(d)) for d in 'wasd')


    def get_maximum(self):
        maximum = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] > maximum:
                    maximum = self.grid[i][j]
        return maximum


    def help(self):
        """
        find a direct that player can get highest value in grid
        :return: direction
        """
        maximum = 0
        direction = ''
        if self.movable(ord('a')):
            self.move(ord('a'))
            if self.get_maximum() > maximum:
                maximum = self.get_maximum()
                direction = 'a'
            self.move(ord('d'))

        if self.movable(ord('d')):
            self.move(ord('d'))
            if self.get_maximum() > maximum:
                maximum = self.get_maximum()
                direction = 'd'
            self.move(ord('a'))

        if self.movable(ord('w')):
            self.move(ord('w'))
            if self.get_maximum() > maximum:
                maximum = self.get_maximum()
                direction = 'w'
            self.move(ord('s'))

        if self.movable(ord('s')):
            self.move(ord('s'))
            if self.get_maximum() > maximum:
                direction = 's'
            self.move(ord('w'))
        return direction



