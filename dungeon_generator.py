import random
import time


class DungeonGenerator:

    def __init__(self):
        self.width = None
        self.height = None
        self.multiple_solution = None

        self.x = 1
        self.y = 1
        self.isCompleted = True
        self.level = []

    def place_player(self):
        is_placed = False

        path_length = 0

        while not is_placed:
            # search in triangular pattern
            x = path_length//2
            y = path_length - x

            if self.level[y][x] == " ":
                self.level[y][x] = "P"
                is_placed = True
            else:
                path_length += 1

    def place_coins(self, coin_density: float):
        number_of_coins = coin_density * (self.width + self.height)/2

        number_of_coins *= random.random() * 0.5 + 0.75

        for i in range(int(number_of_coins)):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)

            while self.level[y][x] != " ":
                x = random.randint(1, self.width - 1)
                y = random.randint(1, self.height - 1)

            self.level[y][x] = "C"

    def create_dungeon(self, width, height=None, multiple_solution=True):
    
        # set dungeon width
        if width % 2 == 0:           # has to be 2n+1 because walls are cells
            print("width HAS to be odd, thus increasing width to", width + 1)
            self.width = width + 1
        else:
            self.width = width
        
        # set dungeon height
        if height is None:
            self.height = self.width
        else:
            if height % 2 == 0:           # has to be 2n+1 because walls are cells
                print("height HAS to be odd, thus increasing height to", height + 1)
                self.height = height + 1
            else:
                self.height = height
        
        self.multiple_solution = multiple_solution

        self.isCompleted = False

        # create level          "X" is Wall "@" is temp char to be changed in wall or Air
        self.level = []

        for y in range(self.height):
            if y == 0 or y == self.height - 1:
                self.level.append(["X" for x in range(self.width)])   # fills first and last row with walls
            else:
                # fills all other rows empty except left, right walls
                self.level.append(["X", *("@" for x in range(self.width - 2)), "X"])
            # printing the level
            print(self.level[y])

        # select starting pos
        self.x, self.y = (1, 1)
        self.level[self.y][self.x] = " "

        # starting generation
        while not self.isCompleted:

            # check for valid movement
            possible_move = self.check_move()
            if possible_move[4]:
                self.walk(possible_move)
            else:
                self.isCompleted = self.hunt()


        # create multiple solution by removing walls
        if multiple_solution:
            number_of_walls_to_delete = int((self.width*self.height)**0.5)

            for i in range(number_of_walls_to_delete):
                x_to_delete = random.randint(1, self.width - 1)
                y_to_delete = random.randint(1, self.height - 1)

                while self.level[y_to_delete][x_to_delete] != "@":
                    x_to_delete = random.randint(1, self.width - 1)
                    y_to_delete = random.randint(1, self.height - 1)

                #self.level[y_to_delete][x_to_delete] = " "

        # convert all @ to X

        for i in range(self.height):
            for j in range(self.width):
                if self.level[i][j] == "@":
                    self.level[i][j] = "X"

        # add player
        self.place_player()

        # add coins
        self.place_coins(0.2)

        for line in self.level:
            print(line)
        print("done")

        string_list = self.list2d_to_string_list()
        return string_list
    
    def list2d_to_string_list(self):
        string_list = []
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.level[y][x]
            string_list.append(line)
        return string_list

    def hunt(self):

        # suppose maze is complete
        isMazeCompleted = True

        # check every cell (only "odd" cells because walls are cells)
        for x in range(1, self.width - 1, 2):
            for y in range(1, self.height - 1, 2):
                if self.level[y][x] == "@":
                    # print("hunt: found an unexplored cell -> checking connection with main path")
                    isMazeCompleted = False

                    connections = self.check_connections(x, y)

                    if connections[4]:
                        # print(f"hunt: cell ({x}, {y}) is connected")
                        time.sleep(0.1)

                        self.x = x
                        self.y = y

                        # select random direction to connect
                        connect = random.randint(0, 3)
                        while not connections[connect]:
                            connect = random.randint(0, 3)

                        self.level[self.y][self.x] = " "

                        # connect to the main path
                        if connect == 0:   # up
                            self.level[self.y - 1][self.x] = " "

                        if connect == 1:   # down
                            self.level[self.y + 1][self.x] = " "

                        if connect == 2:   # left
                            self.level[self.y][self.x - 1] = " "

                        if connect == 3:   # right
                            self.level[self.y][self.x + 1] = " "

                        return False
        if isMazeCompleted:
            print("hunt: Maze is finished")
            return True
        else:
            print("hunt: Maze is not finished")
            return False


    def walk(self, possible_move):

        # print(f"walk: ({self.x}, {self.y}) --> ", end="")

        # select random direction to walk:  0 up, 1 down, 2 left, 3 right
        move = random.randint(0, 3)
        while not possible_move[move]:
            # pick again until move is valid
            move = random.randint(0, 3)

        if move == 0:   # up

            self.level[self.y - 1][self.x] = " "
            self.level[self.y - 2][self.x] = " "

            # move head two cells up
            self.y -= 2

        if move == 1:   # down
            self.level[self.y + 1][self.x] = " "
            self.level[self.y + 2][self.x] = " "

            # move head two cells down
            self.y += 2

        if move == 2:   # left
            self.level[self.y][self.x - 1] = " "
            self.level[self.y][self.x - 2] = " "

            # move head two cells left
            self.x -= 2

        if move == 3:   # right
            self.level[self.y][self.x + 1] = " "
            self.level[self.y][self.x + 2] = " "

            # move head two cells right
            self.x += 2

        # print(f"({self.x}, {self.y})")

    def check_move(self):

        # indice : 0 up, 1 down, 2 left, 3 right, 4 can move somewhere
        possible_moves = [False, False, False, False, False]

        # always checks 2 cells ahead, because walls are one cell thick

        # check up
        if self.y > 2:
            if self.level[self.y - 2][self.x] == "@":
                possible_moves[0] = True
                possible_moves[4] = True
        # check down
        if self.y < self.height - 2:
            if self.level[self.y + 2][self.x] == "@":
                possible_moves[1] = True
                possible_moves[4] = True
        # check left
        if self.x > 2:
            if self.level[self.y][self.x - 2] == "@":
                possible_moves[2] = True
                possible_moves[4] = True
        # check right
        if self.x < self.width - 2:
            if self.level[self.y][self.x + 2] == "@":
                possible_moves[3] = True
                possible_moves[4] = True

        return possible_moves

    def check_connections(self, x, y):

        # indice : 0 up, 1 down, 2 left, 3 right, 4 connected
        connections = [False, False, False, False, False]

        # always checks 2 cells ahead, because walls are one cell thick
        # check up
        if y > 2:
            if self.level[y - 2][x] == " ":
                connections[0] = True
                connections[4] = True
        # check down
        if y < self.height - 2:
            if self.level[y + 2][x] == " ":
                connections[1] = True
                connections[4] = True
        # check left
        if x > 2:
            if self.level[y][x - 2] == " ":
                connections[2] = True
                connections[4] = True
        # check right
        if x < self.width - 2:
            if self.level[y][x + 2] == " ":
                connections[3] = True
                connections[4] = True

        return connections


if __name__ == "__main__":
    dungeon_maker = DungeonGenerator()

    level = dungeon_maker.create_dungeon(25)
    for line in level:
        print(line)
